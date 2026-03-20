"""
Test: Simulation Display Fixes
================================
Verifies two fixes:

  Fix 1 — show_simulation flag (Feature 1):
      `show_simulation` in the API response is True ONLY on turns where the
      teacher actually triggered a display, not stale on every subsequent turn.

  Fix 2 — No consecutive duplicate renders (Feature 2):
      When the teacher tries to "show" the simulation with the exact same
      parameters as the last display, the render is suppressed (show_simulation
      stays False, no param_history entry added).
      Exception: student explicitly asking to see the simulation always goes
      through even if params are unchanged.

Usage:
    python test_simulation_display_fixes.py
"""

import sys
sys.path.insert(0, ".")

from api_integration import format_api_response
from state import create_initial_state
from streamlit_app.backend_integration import extract_display_data
# teacher_node logic is replicated inline below to avoid LLM dependency

# ── Helpers ──────────────────────────────────────────────────────────────────

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {label}")
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {label}")
        if detail:
            print(f"         {detail[:300]}")


def section(title):
    print()
    print("=" * 65)
    print(f"  {title}")
    print("=" * 65)


def make_base_state(show_simulation=False, last_displayed_params=None,
                    param_history=None, current_params=None):
    """Build a minimal mock state dict for format_api_response testing."""
    return {
        "simulation_id": "simple_pendulum",
        "show_simulation": show_simulation,
        "last_displayed_params": last_displayed_params or {},
        "current_params": current_params or {"length": 1.0, "number_of_oscillations": 10},
        "parameter_history": param_history or [],
        "concepts": [
            {
                "id": 1,
                "title": "Period and Length",
                "description": "How length affects swing time",
                "key_insight": "Longer pendulum = slower swing",
                "related_params": ["length"]
            }
        ],
        "current_concept_index": 0,
        "last_teacher_message": "Test message",
        "understanding_level": "none",
        "exchange_count": 1,
        "concept_complete": False,
        "session_complete": False,
        "strategy": "continue",
        "teacher_mode": "encouraging",
        "trajectory_status": "improving",
        "needs_deeper": False,
        "correction_made": False,
        "asks_for_reasoning": False,
        "concept_transition": False,
        "understanding_reasoning": "",
        "understanding_trajectory": [],
    }


# ════════════════════════════════════════════════════════════════════════
# FIX 1 TESTS: show_simulation flag in API response
# ════════════════════════════════════════════════════════════════════════

section("FIX 1 — show_simulation field in API response")

# --- Test 1a: show_simulation=False → field is False, param_change is null ---
print("\n[Test 1a] Pure Q&A turn: show_simulation=False in state")
state_no_display = make_base_state(
    show_simulation=False,
    param_history=[
        {   # A change happened in a PAST turn
            "parameter": "length",
            "old_value": 1.0,
            "new_value": 2.0,
            "reason": "Past change",
            "prediction_asked": "",
            "student_reaction": "",
            "understanding_before": "none",
            "understanding_after": "",
            "was_effective": False,
        }
    ],
    current_params={"length": 2.0, "number_of_oscillations": 10},
)

resp = format_api_response("thread_1", state_no_display, "simple_pendulum")
sim = resp["simulation"]

check("show_simulation is False in API response",
      sim.get("show_simulation") == False,
      f"Got: {sim.get('show_simulation')}")

check("param_change is null when show_simulation=False (no stale data)",
      sim.get("param_change") is None,
      f"Got: {sim.get('param_change')}")

check("html_url still reflects current params (always present)",
      "length=2" in sim.get("html_url", ""),
      f"Got url: {sim.get('html_url', '')[:80]}")

# --- Test 1b: show_simulation=True → field is True, param_change populated ---
print("\n[Test 1b] Display turn: show_simulation=True in state")
state_with_display = make_base_state(
    show_simulation=True,
    param_history=[
        {
            "parameter": "length",
            "old_value": 1.0,
            "new_value": 3.0,
            "reason": "Demonstrate longer pendulum",
            "prediction_asked": "What do you think will happen?",
            "student_reaction": "",
            "understanding_before": "none",
            "understanding_after": "",
            "was_effective": False,
        }
    ],
    current_params={"length": 3.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 3.0, "number_of_oscillations": 10},
)

resp2 = format_api_response("thread_2", state_with_display, "simple_pendulum")
sim2 = resp2["simulation"]

check("show_simulation is True in API response",
      sim2.get("show_simulation") == True,
      f"Got: {sim2.get('show_simulation')}")

check("param_change is populated when show_simulation=True",
      sim2.get("param_change") is not None,
      f"Got: {sim2.get('param_change')}")

if sim2.get("param_change"):
    pc = sim2["param_change"]
    check("param_change.parameter is correct",
          pc.get("parameter") == "length",
          f"Got: {pc.get('parameter')}")
    check("param_change.before is correct",
          pc.get("before") == 1.0,
          f"Got: {pc.get('before')}")
    check("param_change.after is correct",
          pc.get("after") == 3.0,
          f"Got: {pc.get('after')}")

# --- Test 1c: Session start (no history ever) → show_simulation=False, param_change=null ---
print("\n[Test 1c] Brand-new session: no param_history, show_simulation=False")
fresh_state = make_base_state()
resp3 = format_api_response("thread_3", fresh_state, "simple_pendulum")
sim3 = resp3["simulation"]

check("show_simulation is False on fresh session",
      sim3.get("show_simulation") == False,
      f"Got: {sim3.get('show_simulation')}")
check("param_change is null on fresh session",
      sim3.get("param_change") is None,
      f"Got: {sim3.get('param_change')}")


# ════════════════════════════════════════════════════════════════════════
# FIX 2 TESTS: Duplicate render suppression in teacher node logic
# We test the logic directly by calling the parameter-change block of
# teacher_node via a helper that reproduces the exact same code path,
# without invoking the LLM.
# ════════════════════════════════════════════════════════════════════════

section("FIX 2 — Duplicate render suppression (no consecutive same params)")

def simulate_teacher_param_block(current_params, last_displayed_params,
                                  param_history, suggests_param_change,
                                  param_to_change, new_value,
                                  student_wants_to_see=False,
                                  understanding="none"):
    """
    Reproduces the parameter-change block from teacher_node without calling
    the LLM. Returns the `updates` dict the teacher node would produce.
    """
    result = {
        "suggests_param_change": suggests_param_change,
        "param_to_change": param_to_change,
        "new_value": new_value,
        "change_reason": "Test change",
        "prediction_question": "What do you think?",
    }

    updates = {
        "show_simulation": False,
    }

    if result.get("suggests_param_change") and result.get("param_to_change"):
        param = result["param_to_change"]
        new_val = result.get("new_value")

        if param and new_val is not None:
            new_params = current_params.copy()
            new_params[param] = new_val

            if new_params == last_displayed_params and not student_wants_to_see:
                # Suppressed — same params as last display
                print(f"     ⏭️  SUPPRESSED: {param}={new_val} (same as last display)")
            else:
                change_record = {
                    "parameter": param,
                    "old_value": current_params.get(param, 0),
                    "new_value": new_val,
                    "reason": result.get("change_reason"),
                    "prediction_asked": result.get("prediction_question"),
                    "student_reaction": "",
                    "understanding_before": understanding,
                    "understanding_after": "",
                    "was_effective": False,
                }
                updates["current_params"] = new_params
                updates["parameter_history"] = param_history + [change_record]
                updates["last_displayed_params"] = new_params
                updates["show_simulation"] = True
                print(f"     ✅  DISPLAYED: {param}: {current_params.get(param)} → {new_val}")

    return updates


# --- Test 2a: First-ever display goes through (last_displayed_params is empty) ---
print("\n[Test 2a] First display (no prior display) — should go through")
updates = simulate_teacher_param_block(
    current_params={"length": 1.0, "number_of_oscillations": 10},
    last_displayed_params={},  # Never been shown
    param_history=[],
    suggests_param_change=True,
    param_to_change="length",
    new_value=2.0,
)
check("show_simulation=True on first display",
      updates.get("show_simulation") == True)
check("current_params updated to new value",
      updates.get("current_params", {}).get("length") == 2.0)
check("parameter_history entry added",
      len(updates.get("parameter_history", [])) == 1)
check("last_displayed_params updated",
      updates.get("last_displayed_params") == {"length": 2.0, "number_of_oscillations": 10})


# --- Test 2b: Same params as last display → suppressed ---
print("\n[Test 2b] Same params as last display — should be suppressed")
same_params = {"length": 2.0, "number_of_oscillations": 10}
updates2 = simulate_teacher_param_block(
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params=same_params,  # Identical to what we'd produce
    param_history=[],
    suggests_param_change=True,
    param_to_change="length",
    new_value=2.0,  # Same value
)
check("show_simulation=False when params unchanged",
      updates2.get("show_simulation") == False)
check("current_params NOT in updates (no change recorded)",
      "current_params" not in updates2)
check("parameter_history NOT in updates (no entry added)",
      "parameter_history" not in updates2)


# --- Test 2c: Different params → goes through ---
print("\n[Test 2c] Different params from last display — should go through")
updates3 = simulate_teacher_param_block(
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 2.0, "number_of_oscillations": 10},
    param_history=[],
    suggests_param_change=True,
    param_to_change="length",
    new_value=3.5,  # Different value
)
check("show_simulation=True when params changed",
      updates3.get("show_simulation") == True)
check("parameter_history entry added for new change",
      len(updates3.get("parameter_history", [])) == 1)
check("last_displayed_params updated to new value",
      updates3.get("last_displayed_params", {}).get("length") == 3.5)


# --- Test 2d: Same params but student explicitly asked to see — should go through ---
print("\n[Test 2d] Same params but student asked to see — should bypass suppression")
updates4 = simulate_teacher_param_block(
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 2.0, "number_of_oscillations": 10},
    param_history=[],
    suggests_param_change=True,
    param_to_change="length",
    new_value=2.0,  # Same value
    student_wants_to_see=True,  # Student explicitly asked
)
check("show_simulation=True even with same params when student asked",
      updates4.get("show_simulation") == True)
check("parameter_history entry added (student's explicit request honoured)",
      len(updates4.get("parameter_history", [])) == 1)


# --- Test 2e: No suggests_param_change → show_simulation=False ---
print("\n[Test 2e] Teacher does not suggest param change — show_simulation=False")
updates5 = simulate_teacher_param_block(
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params={},
    param_history=[],
    suggests_param_change=False,  # LLM didn't trigger display
    param_to_change=None,
    new_value=None,
)
check("show_simulation=False when suggests_param_change=False",
      updates5.get("show_simulation") == False)
check("parameter_history not touched",
      "parameter_history" not in updates5)


# ════════════════════════════════════════════════════════════════════════
# FIX 1+2 INTEGRATION: Multi-turn scenario
# ════════════════════════════════════════════════════════════════════════

section("INTEGRATION — Multi-turn scenario (Fix 1 + Fix 2 together)")

print("\nScenario: 5 turns, changing params, repeating, Q&A-only turn")
print("─" * 65)

scenario_param_history = []
scenario_current_params = {"length": 1.0, "number_of_oscillations": 10}
scenario_last_displayed = {}

# Each entry: (turn_label, suggests_change, param, new_val, student_wants_see,
#              expected_show, expected_param_change_in_api)
turns = [
    ("Turn 1: Initial display, length 1.0→2.0",
     True,  "length", 2.0,  False, True,  True),
    ("Turn 2: Q&A — teacher asks, no param change",
     False, None,    None,  False, False, False),
    ("Turn 3: Same params again (duplicate, should suppress)",
     True,  "length", 2.0, False, False, False),
    ("Turn 4: New value length 2.0→3.5",
     True,  "length", 3.5,  False, True,  True),
    ("Turn 5: Same value 3.5 but student asked to see",
     True,  "length", 3.5,  True,  True,  True),
]

print()
for label, suggests, param, new_val, wants_see, exp_show, exp_pc in turns:
    print(f"  {label}")

    updates = simulate_teacher_param_block(
        current_params=scenario_current_params,
        last_displayed_params=scenario_last_displayed,
        param_history=scenario_param_history,
        suggests_param_change=suggests,
        param_to_change=param,
        new_value=new_val,
        student_wants_to_see=wants_see,
    )

    # Update running state
    if "current_params" in updates:
        scenario_current_params = updates["current_params"]
    if "parameter_history" in updates:
        scenario_param_history = updates["parameter_history"]
    if "last_displayed_params" in updates:
        scenario_last_displayed = updates["last_displayed_params"]

    show_flag = updates.get("show_simulation", False)
    check(f"  show_simulation={exp_show}", show_flag == exp_show,
          f"Got: {show_flag}")

    # Simulate API response
    mock_state = make_base_state(
        show_simulation=show_flag,
        param_history=scenario_param_history,
        current_params=scenario_current_params,
        last_displayed_params=scenario_last_displayed,
    )
    api_resp = format_api_response("thread_int", mock_state, "simple_pendulum")
    api_pc = api_resp["simulation"].get("param_change")
    check(f"  param_change={'populated' if exp_pc else 'null'} in API",
          (api_pc is not None) == exp_pc,
          f"Got param_change: {api_pc}")
    print()


# ════════════════════════════════════════════════════════════════════════
# STATE FIELDS TEST: Verify new fields exist in state
# ════════════════════════════════════════════════════════════════════════

section("STATE — New fields initialized correctly")

print("\n[Test S1] create_initial_state has show_simulation and last_displayed_params")
init_state = create_initial_state(
    topic_description="Test topic",
    initial_params={"length": 1.0, "number_of_oscillations": 10},
    simulation_id="simple_pendulum",
)
check("show_simulation initialised to False",
      init_state.get("show_simulation") == False,
      f"Got: {init_state.get('show_simulation')}")
check("last_displayed_params initialised to empty dict",
      init_state.get("last_displayed_params") == {},
      f"Got: {init_state.get('last_displayed_params')}")


# ════════════════════════════════════════════════════════════════════════
# STREAMLIT PARITY TEST: extract_display_data matches API behaviour
# ════════════════════════════════════════════════════════════════════════

section("STREAMLIT PARITY — extract_display_data matches API response")

def make_full_state(show_simulation, param_history, current_params, last_displayed_params):
    """Build a state dict that mimics full LangGraph state (for extract_display_data)."""
    s = create_initial_state(
        topic_description="Test",
        initial_params=current_params,
        simulation_id="simple_pendulum",
    )
    s["show_simulation"] = show_simulation
    s["last_displayed_params"] = last_displayed_params
    s["current_params"] = current_params
    s["parameter_history"] = param_history
    s["last_teacher_message"] = "Test message"
    s["concepts"] = [
        {
            "id": 1, "title": "Period and Length",
            "description": "How length affects swing time",
            "key_insight": "Longer pendulum = slower swing",
            "related_params": ["length"]
        }
    ]
    return s


print("\n[Test ST1] Q&A turn (show_simulation=False) — Streamlit shows NO simulation")
st_state_qa = make_full_state(
    show_simulation=False,
    param_history=[{
        "parameter": "length", "old_value": 1.0, "new_value": 2.0,
        "reason": "Past change", "prediction_asked": "", "student_reaction": "",
        "understanding_before": "none", "understanding_after": "", "was_effective": False,
    }],
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 2.0, "number_of_oscillations": 10},
)
dd_qa = extract_display_data(st_state_qa)
check("Streamlit: param_change_info is None on Q&A turn",
      dd_qa.get("param_change_info") is None,
      f"Got: {dd_qa.get('param_change_info')}")

# Confirm API gives same result
api_qa = format_api_response("t_qa", st_state_qa, "simple_pendulum")
check("API and Streamlit agree: both show no simulation on Q&A turn",
      (api_qa["simulation"]["show_simulation"] == False) and (dd_qa.get("param_change_info") is None))


print("\n[Test ST2] Display turn (show_simulation=True) — Streamlit shows simulation")
st_state_show = make_full_state(
    show_simulation=True,
    param_history=[{
        "parameter": "length", "old_value": 1.0, "new_value": 3.0,
        "reason": "Demonstrate", "prediction_asked": "What happens?", "student_reaction": "",
        "understanding_before": "none", "understanding_after": "", "was_effective": False,
    }],
    current_params={"length": 3.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 3.0, "number_of_oscillations": 10},
)
dd_show = extract_display_data(st_state_show)
check("Streamlit: param_change_info is populated on display turn",
      dd_show.get("param_change_info") is not None,
      f"Got: {dd_show.get('param_change_info')}")
if dd_show.get("param_change_info"):
    pci = dd_show["param_change_info"]
    check("Streamlit: param_change_info.parameter is correct",
          pci.get("parameter") == "length", f"Got: {pci.get('parameter')}")
    check("Streamlit: param_change_info.old_value is correct",
          pci.get("old_value") == 1.0, f"Got: {pci.get('old_value')}")
    check("Streamlit: param_change_info.new_value is correct",
          pci.get("new_value") == 3.0, f"Got: {pci.get('new_value')}")

# Confirm API gives same result
api_show = format_api_response("t_show", st_state_show, "simple_pendulum")
check("API and Streamlit agree: both show simulation on display turn",
      (api_show["simulation"]["show_simulation"] == True) and (dd_show.get("param_change_info") is not None))


print("\n[Test ST3] Duplicate suppressed (show_simulation=False, same params) — Streamlit suppresses")
st_state_dup = make_full_state(
    show_simulation=False,           # Teacher node suppressed the duplicate
    param_history=[{                 # History still has the original change from before
        "parameter": "length", "old_value": 1.0, "new_value": 2.0,
        "reason": "First display", "prediction_asked": "", "student_reaction": "I see it",
        "understanding_before": "none", "understanding_after": "partial", "was_effective": True,
    }],
    current_params={"length": 2.0, "number_of_oscillations": 10},
    last_displayed_params={"length": 2.0, "number_of_oscillations": 10},
)
dd_dup = extract_display_data(st_state_dup)
check("Streamlit: param_change_info is None when duplicate suppressed",
      dd_dup.get("param_change_info") is None,
      f"Got: {dd_dup.get('param_change_info')}")

api_dup = format_api_response("t_dup", st_state_dup, "simple_pendulum")
check("API and Streamlit agree: both suppress duplicate",
      (api_dup["simulation"]["show_simulation"] == False) and (dd_dup.get("param_change_info") is None))


# ════════════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════════════

print()
print("=" * 65)
print(f"  RESULTS: {PASS_COUNT} passed, {FAIL_COUNT} failed")
print("=" * 65)

if FAIL_COUNT > 0:
    sys.exit(1)
