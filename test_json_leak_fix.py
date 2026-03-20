"""
Test: JSON Leak Fix for Kannada Teacher Responses
==================================================
Verifies the clean_teacher_message fix prevents raw JSON from leaking
into teacher messages displayed to students.

Two suites:
  Suite A  Synthetic bug simulation using mocks
  Suite B  Live end-to-end: 10 turns on litmus_indicator_kn in Kannada

Usage:
    python test_json_leak_fix.py

LangSmith tracing:
    Each run is traced under the project defined in .env
    (LANGCHAIN_PROJECT=simulation_to_concept_modified).
    Suite A and Suite B each appear as child spans under a single
    top-level "test_json_leak_fix" run, making results visible to
    the whole team in LangSmith.
"""

import sys
import uuid
import re
import time

# ── Load .env FIRST so LangSmith env vars are set before any import ──────────
# This must happen before importing langsmith, langchain, or the graph modules.
sys.path.insert(0, ".")
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import langsmith

PASS_COUNT = 0
FAIL_COUNT = 0
_results = []   # (label, passed)


def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {label}")
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {label}")
        if detail:
            print(f"         {detail[:200]}")
    _results.append((label, condition))


def has_json_leak(text):
    if not text:
        return False
    leaks = [
        '"teacher_message"',
        '"suggests_param_change"',
        '"param_to_change"',
        '"change_reason"',
    ]
    return any(k in text for k in leaks)


def section(title):
    print()
    print("=" * 65)
    print(f"  {title}")
    print("=" * 65)


# ── Top-level LangSmith trace wraps everything ────────────────────────────────
# Child traces (suite_a, suite_b, and all LangGraph node spans) are automatically
# parented to this run because LangSmith propagates the active context in-thread.
_run_id = str(uuid.uuid4())
_top_run = langsmith.trace(
    name="test_json_leak_fix",
    run_type="chain",
    metadata={
        "test_file": "test_json_leak_fix.py",
        "fix": "clean_teacher_message JSON leak prevention",
        "simulation": "litmus_indicator_kn",
        "language": "kannada",
        "run_id": _run_id,
    },
)
top_run = _top_run.__enter__()


# ======================================================================
# SUITE A: Synthetic unit tests for clean_teacher_message
# ======================================================================

section("SUITE A: Unit tests for clean_teacher_message()")

from nodes.teacher import clean_teacher_message

with langsmith.trace(
    name="suite_a_unit_tests",
    run_type="chain",
    metadata={"suite": "A", "description": "Synthetic unit tests for clean_teacher_message"},
) as suite_a_run:

    # A1: Normal clean Kannada message must be unchanged
    m = "ಚೆನ್ನಾಗಿ ಗಮನಿಸಿದ್ದೀಯ! OBSERVE: ಈಗ ಪರದೆಯ ಮೇಲೆ ಗಮನಿಸು."
    check("A1  Clean message unchanged", clean_teacher_message(m) == m)

    # A2: Exact bug scenario from screenshot
    buggy1 = (
        "ಚೆನ್ನಾಗಿ ಗಮನಿಸಿದ್ದೀಯ ಗೆಳೆಯ! ಪ್ರತ್ಯಾಮ್ಲಗಳು ಗುಲಾಬಿ ಸಾರವನ್ನು "
        "ಹಸಿರು ಬಣ್ಣಕ್ಕೆ ತಿರುಗಿಸುತ್ತವೆ. OBSERVE: ಈಗ ಪರದೆಯ ಮೇಲೆ ಗಮನಿಸು.\n\n"
        "{\n"
        '    "teacher_message": "ಚೆನ್ನಾಗಿ ಗಮನಿಸಿದ್ದೀಯ",\n'
        '    "suggests_param_change": true,\n'
        '    "param_to_change": "initialState",\n'
        '    "new_value": "basic",\n'
        '    "change_reason": "ಕಾರಣ",\n'
        '    "prediction_question": null\n'
        "}"
    )
    r2 = clean_teacher_message(buggy1)
    check("A2  Screenshot payload: JSON stripped", not has_json_leak(r2), repr(r2[:100]))
    check("A2  Screenshot payload: prose preserved", "ಚೆನ್ನಾಗಿ ಗಮನಿಸಿದ್ದೀಯ ಗೆಳೆಯ" in r2)

    # A3: Fenced ```json block variant
    buggy2 = (
        "ಆಮ್ಲಗಳು ನೀಲಿ ಲಿಟ್ಮಸ್ ಅನ್ನು ಕೆಂಪಾಗಿಸುತ್ತವೆ. OBSERVE: ಈಗ ಗಮನಿಸು.\n\n"
        "```json\n"
        '{\n    "teacher_message": "ಆಮ್ಲಗಳು",\n    "suggests_param_change": true\n}\n'
        "```"
    )
    r3 = clean_teacher_message(buggy2)
    check("A3  Fenced code block stripped", not has_json_leak(r3), repr(r3[:100]))
    check("A3  Prose before block preserved", "ಆಮ್ಲಗಳು ನೀಲಿ ಲಿಟ್ಮಸ್" in r3)

    # A4: Only suggests_param_change key (no teacher_message key)
    buggy3 = (
        "ತಟಸ್ಥ ದ್ರಾವಣದಲ್ಲಿ ಯಾವ ಬಣ್ಣವೂ ಬದಲಾಗುವುದಿಲ್ಲ.\n\n"
        '{\n    "suggests_param_change": false,\n    "param_to_change": null\n}'
    )
    r4 = clean_teacher_message(buggy3)
    check("A4  Partial JSON (only suggests_param_change) stripped", not has_json_leak(r4))
    check("A4  Prose preserved", "ತಟಸ್ಥ ದ್ರಾವಣ" in r4)

    # A5: Empty string
    check("A5  Empty string returns empty", clean_teacher_message("") == "")

    # A6: None
    check("A6  None input returns None", clean_teacher_message(None) is None)

    # A7: Already-clean value unchanged
    cv = "ಆಮ್ಲಗಳು ಕೆಂಪು ಬಣ್ಣ ನೀಡುತ್ತವೆ. PREDICT: ಏನಾಗುತ್ತದೆ?"
    check("A7  Clean extracted value unchanged", clean_teacher_message(cv) == cv)

    # A8: Curly braces in normal text must NOT be stripped
    math_msg = "Chemistry: {H+} ions cause litmus to turn red. OBSERVE: what do you see?"
    r8 = clean_teacher_message(math_msg)
    check("A8  Curly braces in normal text not stripped", "H+" in r8, repr(r8[:100]))

    # A9: Simulate fallback path (parse_json_safe failed, whole raw content stored)
    raw = (
        "ಚೆನ್ನಾಗಿ ಕೇಳಿದೆ! ಲಿಟ್ಮಸ್ ಒಂದು ಸಂಪೂರ್ಣ ಸೂಚಕ.\n\n"
        "{\n"
        '    "teacher_message": "ಚೆನ್ನಾಗಿ ಕೇಳಿದೆ!",\n'
        '    "suggests_param_change": false,\n'
        '    "param_to_change": null,\n'
        '    "new_value": null,\n'
        '    "change_reason": null,\n'
        '    "prediction_question": null\n'
        "}"
    )
    salvaged = clean_teacher_message(raw)
    fallback_msg = clean_teacher_message({"teacher_message": salvaged}.get("teacher_message", raw))
    check("A9  Fallback path: no JSON leak in final message", not has_json_leak(fallback_msg))
    check("A9  Fallback path: prose preserved", "ಚೆನ್ನಾಗಿ ಕೇಳಿದೆ" in fallback_msg)

    # Record suite outcome in LangSmith span
    suite_a_pass = sum(1 for _, p in _results if p)
    suite_a_total = len(_results)
    suite_a_run.outputs = {"passed": suite_a_pass, "total": suite_a_total, "failed": suite_a_total - suite_a_pass}

# ======================================================================
# SUITE B: Live end-to-end — litmus_indicator_kn in Kannada
# ======================================================================

section("SUITE B: End-to-end  litmus_indicator_kn  Kannada  10 turns")

BACKEND_OK = False
try:
    from simulations_config import get_simulation
    from state import create_initial_state
    from graph import start_session, continue_session
    BACKEND_OK = True
    print("  Backend imported OK")
except Exception as e:
    print(f"  Backend import failed: {e}")
    print("  Skipping Suite B")

SIMULATION_ID = "litmus_indicator_kn"

if BACKEND_OK:
    sim_config = get_simulation(SIMULATION_ID)
    if not sim_config:
        print(f"  Simulation '{SIMULATION_ID}' not found. Skipping Suite B.")
        BACKEND_OK = False

# 10 realistic student turns covering correct/wrong/question/vague responses
STUDENT_TURNS = [
    "ಗೊತ್ತಿಲ್ಲ",
    "ಕೆಂಪು ಬಣ್ಣ ಕಾಣಿಸುತ್ತದೆ",
    "ಆಮ್ಲ ಕೆಂಪು ಬಣ್ಣ ನೀಡುತ್ತದೆ",
    "ಪ್ರತ್ಯಾಮ್ಲ ಕೂಡ ಕೆಂಪು ಬಣ್ಣ ನೀಡುತ್ತದೆ",
    "ಏಕೆ ಬಣ್ಣ ಬದಲಾಗುತ್ತದೆ?",
    "ಪ್ರತ್ಯಾಮ್ಲ ಕೆಂಪು ಲಿಟ್ಮಸ್ ಅನ್ನು ನೀಲಿಗೆ ಬದಲಿಸುತ್ತದೆ",
    "ಹೌದು ನೋಡಿದೆ",
    "ತಟಸ್ಥ ದ್ರಾವಣದಲ್ಲಿ ಏನಾಗುತ್ತದೆ?",
    "ಯಾವ ಬಣ್ಣವೂ ಬದಲಾಗುವುದಿಲ್ಲ",
    "ಲಿಟ್ಮಸ್ ಸಂಪೂರ್ಣ ಸೂಚಕ ಏಕೆ ಎಂದು ಅರ್ಥವಾಯಿತು",
]

if BACKEND_OK:
    _suite_b_start = len(_results)  # snapshot index to count B-only results
    thread_id = f"test_leak_{uuid.uuid4().hex[:8]}"
    print(f"  Simulation : {sim_config['title']}")
    print(f"  Thread ID  : {thread_id}")
    print()

    with langsmith.trace(
        name="suite_b_end_to_end",
        run_type="chain",
        metadata={
            "suite": "B",
            "simulation_id": SIMULATION_ID,
            "simulation_title": sim_config["title"],
            "language": "kannada",
            "session_id": thread_id,   # ← enables LangSmith Threads grouping
            "thread_id": thread_id,
            "num_planned_turns": len(STUDENT_TURNS),
            "description": "Live end-to-end conversation test on litmus_indicator_kn",
        },
    ) as suite_b_run:

        # Turn 0: opening message (no student input — teacher opens first)
        print("  [Turn 0] Starting session...")
        try:
            initial_state = create_initial_state(
                topic_description=sim_config["description"],
                initial_params=sim_config["initial_params"].copy(),
                simulation_id=SIMULATION_ID,
                language="kannada",
            )
            with langsmith.trace(
                name="turn_00_opening",
                run_type="chain",
                metadata={"session_id": thread_id, "turn": 0, "role": "teacher"},
            ) as t0_run:
                t0_run.add_inputs({"student_message": "(session start)"})
                for _attempt in range(3):
                    try:
                        state = start_session(initial_state, thread_id)
                        break
                    except Exception as _e:
                        if _attempt < 2 and "429" in str(_e):
                            time.sleep(5 * (_attempt + 1))
                        else:
                            raise
                opening = state.get("last_teacher_message", "")
                t0_run.outputs = {"teacher_message": opening}
                t0_run.add_metadata({"has_json_leak": has_json_leak(opening)})
            leak = has_json_leak(opening)
            check("Turn 0  Opening message: no JSON leak", not leak,
                  repr(opening[:80]) if leak else "")
            if opening:
                print(f"         Preview: {opening[:90].replace(chr(10), ' ')}...")
        except Exception as e:
            check("Turn 0  No exception during start_session", False, str(e))
            BACKEND_OK = False

        for i, student_input in enumerate(STUDENT_TURNS, start=1):
            if not BACKEND_OK:
                break
            print(f"\n  [Turn {i}] Student: \"{student_input}\"")
            try:
                # Each turn is its own child span → visible as a thread message in LangSmith
                with langsmith.trace(
                    name=f"turn_{i:02d}",
                    run_type="chain",
                    metadata={"session_id": thread_id, "turn": i, "role": "student→teacher"},
                ) as turn_run:
                    turn_run.add_inputs({"student_message": student_input})
                    for _attempt in range(3):
                        try:
                            state = continue_session(student_input, thread_id)
                            break
                        except Exception as _e:
                            if _attempt < 2 and "429" in str(_e):
                                time.sleep(5 * (_attempt + 1))
                            else:
                                raise
                    msg = state.get("last_teacher_message", "")
                    leak = has_json_leak(msg)
                    turn_run.outputs = {"teacher_message": msg}
                    turn_run.add_metadata({
                        "has_json_leak": leak,
                        "session_complete": bool(state.get("session_complete")),
                        "quiz_mode": bool(state.get("quiz_mode")),
                    })
                check(f"Turn {i:02d}  Teacher message: no JSON leak", not leak,
                      repr(msg[:120]) if leak else "")
                if msg:
                    print(f"         Preview: {msg[:90].replace(chr(10), ' ')}...")
                if state.get("session_complete") or state.get("quiz_mode"):
                    print(f"  Session ended at turn {i} (complete/quiz). Remaining turns skipped.")
                    break
                time.sleep(3)   # avoid 429 rate-limit across turns
            except Exception as e:
                check(f"Turn {i:02d}  No exception", False, str(e))

        # Record suite B outcome in LangSmith span
        suite_b_results = _results[_suite_b_start:]
        suite_b_pass = sum(1 for _, p in suite_b_results if p)
        suite_b_total = len(suite_b_results)
        suite_b_run.outputs = {
            "passed": suite_b_pass,
            "total": suite_b_total,
            "failed": suite_b_total - suite_b_pass,
        }

    # ======================================================================
    # Summary — also written to the top-level LangSmith span
    # ======================================================================

# ======================================================================
# Summary -- also written to the top-level LangSmith span
# ======================================================================

section("SUMMARY")
total = PASS_COUNT + FAIL_COUNT
print(f"  Passed : {PASS_COUNT}/{total}")
print(f"  Failed : {FAIL_COUNT}/{total}")
print()
if FAIL_COUNT == 0:
    print("  All checks passed. JSON leak fix is working correctly.")
else:
    print("  Some checks failed. Review output above.")
print()

# Write final outcome and close the top-level LangSmith run
top_run.outputs = {
    "passed": PASS_COUNT,
    "failed": FAIL_COUNT,
    "total": total,
    "all_passed": FAIL_COUNT == 0,
    "fix_verified": FAIL_COUNT == 0,
}
_top_run.__exit__(None, None, None)

# Print the LangSmith URL so the team can open it directly
try:
    trace_url = top_run.get_url()
    print(f"  LangSmith trace : {trace_url}")
except Exception:
    pass
print()

sys.exit(0 if FAIL_COUNT == 0 else 1)
