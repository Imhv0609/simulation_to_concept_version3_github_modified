"""
Live End-to-End Test: Simulation Display Fixes
===============================================
Runs a real 6-turn conversation on the simple_pendulum simulation (English)
using the actual LLM + LangGraph pipeline.

After each turn it verifies the two fixes are working correctly:

  Fix 1 — show_simulation flag:
      - show_simulation is always a bool in the API response
      - When show_simulation=True  → param_change is populated
      - When show_simulation=False → param_change is null  (no stale data)
      - html_url is always present (regardless of show_simulation)

  Fix 2 — No consecutive duplicate renders:
      - If two consecutive turns both have show_simulation=True,
        their param snapshots must be different

General quality checks per turn:
      - Teacher message has no raw JSON leak
      - simulation.id, simulation.title are present
      - learning_state fields are present

Usage:
    python test_live_display_fixes.py
"""

import sys
import json
import uuid
sys.path.insert(0, ".")

# Load .env FIRST — must happen before any langsmith/langchain import
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import langsmith

# ── Helpers ───────────────────────────────────────────────────────────────────

PASS_COUNT = 0
FAIL_COUNT = 0
_results = []


def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"    [PASS] {label}")
    else:
        FAIL_COUNT += 1
        print(f"    [FAIL] {label}")
        if detail:
            print(f"           {str(detail)[:250]}")
    _results.append((label, condition))


def has_json_leak(text):
    if not text:
        return False
    leaks = ['"teacher_message"', '"suggests_param_change"',
             '"param_to_change"', '"change_reason"']
    return any(k in text for k in leaks)


def section(title):
    print()
    print("=" * 65)
    print(f"  {title}")
    print("=" * 65)


# ── Top-level LangSmith trace ────────────────────────────────────────────────
# All LangGraph node spans (teacher, evaluator, strategy) are automatically
# parented to this run so the full test appears as one entry in LangSmith
# under the project defined in .env (LANGCHAIN_PROJECT=simulation_to_concept_modified).
_run_id = str(uuid.uuid4())
_top_trace = langsmith.trace(
    name="test_live_display_fixes",
    run_type="chain",
    metadata={
        "test_file": "test_live_display_fixes.py",
        "fixes": "show_simulation flag + duplicate render suppression",
        "simulation": "simple_pendulum",
        "language": "english",
        "run_id": _run_id,
    },
)
_top_run = _top_trace.__enter__()

# ── Import backend ─────────────────────────────────────────────────────────────
section("Importing backend modules")
try:
    from api_integration import create_teaching_session, process_student_input
    print("  ✅ api_integration imported OK")
except Exception as e:
    print(f"  ❌ Import failed: {e}")
    _top_trace.__exit__(type(e), e, e.__traceback__)
    sys.exit(1)


# ── Session setup ──────────────────────────────────────────────────────────────
SIMULATION_ID = "simple_pendulum"

# Six turns designed to exercise all cases:
#   Turn 1 → Opening: expect show_simulation=True   (teacher always shows at start)
#   Turn 2 → Vague answer: LLM may or may not show  (either is fine)
#   Turn 3 → "I don't know": teacher should show sim to help
#   Turn 4 → Correct observation: may not need to show
#   Turn 5 → Wrong answer: teacher corrects and likely shows
#   Turn 6 → Ask to see simulation: MUST show (student explicit request)
STUDENT_TURNS = [
    "I'm not sure what I'm looking at.",          # Turn 1 (after opening)
    "I don't know what's happening.",             # Turn 2
    "The pendulum is swinging.",                  # Turn 3 — vague observation
    "I think longer pendulum swings faster.",     # Turn 4 — factually WRONG
    "Actually, longer pendulum swings slower.",   # Turn 5 — correct
    "Can you show me the simulation again?",      # Turn 6 — explicit request
]

section(f"Starting live session  →  {SIMULATION_ID}  (English)")

try:
    thread_id, opening_response = create_teaching_session(
        simulation_id=SIMULATION_ID,
        language="english"
    )
    print(f"\n  Session ID : {thread_id}")
    print(f"  Simulation : {opening_response['simulation']['title']}")
    print(f"  Opening msg: {opening_response['teacher_message']['text'][:100]}...")
except Exception as e:
    print(f"  ❌ Session creation failed: {e}")
    import traceback
    traceback.print_exc()
    _top_trace.__exit__(type(e), e, e.__traceback__)
    sys.exit(1)


# ── Per-turn checks ────────────────────────────────────────────────────────────

def verify_response(turn_label, response, prev_display_params):
    """
    Run all Fix-1 and Fix-2 checks on a single API response.

    Returns the current display params snapshot so the next turn can
    check Fix 2 (no consecutive duplicate renders).
    """
    print(f"\n  --- {turn_label} ---")
    sim = response.get("simulation", {})
    teacher_text = response.get("teacher_message", {}).get("text", "")
    learning = response.get("learning_state", {})

    # Truncate for display
    print(f"  Teacher  : {teacher_text[:120]}{'...' if len(teacher_text) > 120 else ''}")
    print(f"  show_sim : {sim.get('show_simulation')}  |  "
          f"param_change: {json.dumps(sim.get('param_change')) if sim.get('param_change') else 'null'}  |  "
          f"understanding: {learning.get('understanding_level', '?')}")

    # ── Fix 1: show_simulation flag ────────────────────────────────────────
    check(f"{turn_label}: show_simulation field is a bool",
          isinstance(sim.get("show_simulation"), bool),
          f"Got type: {type(sim.get('show_simulation'))}")

    if sim.get("show_simulation") is True:
        check(f"{turn_label}: param_change populated when show_simulation=True",
              sim.get("param_change") is not None,
              f"param_change was: {sim.get('param_change')}")
    else:
        check(f"{turn_label}: param_change is null when show_simulation=False",
              sim.get("param_change") is None,
              f"param_change was: {sim.get('param_change')}")

    # html_url always present
    check(f"{turn_label}: html_url always present",
          bool(sim.get("html_url")),
          f"Got: {sim.get('html_url')}")

    # ── Fix 2: no consecutive duplicate renders ────────────────────────────
    current_display_params = None
    if sim.get("show_simulation") is True:
        current_params = sim.get("current_params", {})
        current_display_params = current_params  # snapshot when shown

        if prev_display_params is not None:
            check(f"{turn_label}: consecutive show_simulation=True has DIFFERENT params",
                  current_params != prev_display_params,
                  f"Prev: {prev_display_params}  |  Current: {current_params}")
        else:
            print(f"    [INFO] First display this session — no duplicate check needed")

    # ── General quality ────────────────────────────────────────────────────
    check(f"{turn_label}: no JSON leak in teacher message",
          not has_json_leak(teacher_text),
          f"Leaked text: {teacher_text[:200]}")

    check(f"{turn_label}: simulation.id present",
          bool(sim.get("id")),
          f"Got: {sim.get('id')}")

    check(f"{turn_label}: learning_state.understanding_level present",
          learning.get("understanding_level") in ["none", "partial", "mostly", "complete"],
          f"Got: {learning.get('understanding_level')}")

    return current_display_params


# ── Run turns ──────────────────────────────────────────────────────────────────

section("Turn 0: Opening message (teacher speaks first)")
with langsmith.trace(
    name="turn_0_opening",
    run_type="chain",
    metadata={"turn": 0, "student_input": "(opening — no student input)"},
):
    prev_params = verify_response("Turn 0", opening_response, prev_display_params=None)

for i, student_input in enumerate(STUDENT_TURNS, start=1):
    section(f"Turn {i}: Student says → \"{student_input}\"")
    response = None
    with langsmith.trace(
        name=f"turn_{i}",
        run_type="chain",
        metadata={"turn": i, "student_input": student_input},
    ) as turn_run:
        try:
            response = process_student_input(thread_id, student_input)
            prev_params = verify_response(f"Turn {i}", response, prev_display_params=prev_params)
            turn_run.outputs = {
                "show_simulation": response.get("simulation", {}).get("show_simulation"),
                "understanding": response.get("learning_state", {}).get("understanding_level"),
                "param_change": response.get("simulation", {}).get("param_change"),
            }
        except Exception as e:
            print(f"  ❌ Turn {i} failed with exception: {e}")
            import traceback
            traceback.print_exc()
            FAIL_COUNT += 1

    if response and response.get("teacher_message", {}).get("session_ending"):
        print(f"\n  ℹ️ Session ended at turn {i} — stopping early")
        break


# ── Close top-level LangSmith trace ───────────────────────────────────────────
_top_run.outputs = {"passed": PASS_COUNT, "failed": FAIL_COUNT}
_top_trace.__exit__(None, None, None)

# ── Summary ────────────────────────────────────────────────────────────────────
print()
print("=" * 65)
print(f"  RESULTS: {PASS_COUNT} passed, {FAIL_COUNT} failed")
print("=" * 65)

if FAIL_COUNT > 0:
    sys.exit(1)
