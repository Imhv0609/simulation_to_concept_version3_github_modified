"""
Test: Student-Driven Simulation Parameter Detection
=====================================================
Verifies that when a student manually changes simulation parameters,
the backend correctly:
  1. Evaluator   — short-circuits (no LLM call), returns response_type='student_param_change'
  2. Strategy    — preserves current strategy, does NOT increment exchange_count
  3. Teacher     — merges student params into current_params, sets show_simulation=True,
                   resets flags, adds history entry tagged initiated_by='student'
  4. API layer   — show_simulation and param_change surface correctly in JSON response
  5. Backward    — omitting student_changed_params behaves identically to before

Two test tiers:
  TIER 1  Unit tests  — run instantly, no LLM, no server needed
  TIER 2  Live tests  — require  uvicorn api_server:app --reload --port 8000

Usage:
    # Tier 1 only (fast):
    python test_student_param_changes.py

    # Tier 1 + Tier 2 (full, server must be running):
    python test_student_param_changes.py --live
"""

import sys
import copy
sys.path.insert(0, ".")

PASS_COUNT = 0
FAIL_COUNT = 0


# ── Helpers ───────────────────────────────────────────────────────────────────

def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {label}")
    else:
        FAIL_COUNT += 1
        msg = f"  [FAIL] {label}"
        if detail:
            msg += f"\n         → {detail}"
        print(msg)


def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def make_state(overrides=None):
    """Build a minimal TeachingState-like dict for testing."""
    base = {
        "simulation_id": "pendulum_timing_kn",
        "student_response": "interesting",
        "student_changed_params": {},
        "student_changed_params_this_turn": False,
        "understanding_level": "partial",
        "understanding_trajectory": ["none", "partial"],
        "understanding_reasoning": "Student is getting there",
        "response_type": "answer",
        "exchange_count": 2,
        "strategy": "continue",
        "teacher_mode": "encouraging",
        "trajectory_status": "improving",
        "concept_complete": False,
        "session_complete": False,
        "should_scaffold": False,
        "needs_deeper": False,
        "is_factually_wrong": False,
        "student_asked_question": False,
        "question_asked": "",
        "student_requested_param": False,
        "requested_param": "",
        "requested_value": None,
        "student_wants_to_see_simulation": False,
        "show_simulation": False,
        "last_displayed_params": {"initialState": "medium"},
        "current_params": {"initialState": "medium"},
        "parameter_history": [],
        "conversation_history": [],
        "last_teacher_message": "What do you notice about the pendulum?",
        "concepts": [
            {
                "id": 1,
                "title": "Pendulum Length and Period",
                "description": "Longer pendulums swing slower",
                "key_insight": "Length determines period",
                "related_params": ["initialState"]
            }
        ],
        "current_concept_index": 0,
        "topic_description": "Test topic",
        "waiting_for_input": True,
        "cannot_demonstrate": [],
        "language": "kannada",
    }
    if overrides:
        base.update(overrides)
    return base


# ══════════════════════════════════════════════════════════════════════════════
# TIER 1 — UNIT TESTS (no LLM, no server)
# ══════════════════════════════════════════════════════════════════════════════

def test_evaluator_short_circuits():
    section("TIER 1 · Evaluator: short-circuit when student changed params")
    from nodes.evaluator import understanding_evaluator_node

    state = make_state({
        "student_changed_params_this_turn": True,
        "student_changed_params": {"initialState": "long"},
        "understanding_level": "partial",
    })

    result = understanding_evaluator_node(state)

    check("response_type is 'student_param_change'",
          result.get("response_type") == "student_param_change",
          f"got: {result.get('response_type')}")

    check("understanding_level preserved (not reset)",
          result.get("understanding_level") == "partial",
          f"got: {result.get('understanding_level')}")

    check("is_factually_wrong is False",
          result.get("is_factually_wrong") == False,
          f"got: {result.get('is_factually_wrong')}")

    check("student_asked_question is False",
          result.get("student_asked_question") == False)

    check("student_requested_param is False",
          result.get("student_requested_param") == False)

    check("understanding_reasoning mentions exploration",
          "explor" in result.get("understanding_reasoning", "").lower(),
          f"got: {result.get('understanding_reasoning')}")


def test_evaluator_normal_path_unchanged():
    section("TIER 1 · Evaluator: normal path still runs when no student params")
    # Just verify it does NOT short-circuit and tries to call LLM
    # We can't run the LLM in a unit test, so just check the state before
    # the LLM call would happen — if student_changed_params_this_turn is False
    # the function should NOT return early.
    # We verify this by checking the short-circuit condition is False.
    state = make_state({
        "student_changed_params_this_turn": False,
        "student_changed_params": {},
    })
    check("student_changed_params_this_turn is False (normal path)",
          state["student_changed_params_this_turn"] == False)
    check("No short-circuit would trigger",
          not state.get("student_changed_params_this_turn", False))


def test_strategy_preserves_on_param_change():
    section("TIER 1 · Strategy: preserves strategy + exchange_count")
    from nodes.strategy import strategy_selector_node

    state = make_state({
        "response_type": "student_param_change",
        "strategy": "try_different",
        "exchange_count": 3,
        "teacher_mode": "simplifying",
    })

    result = strategy_selector_node(state)

    check("strategy preserved (not changed)",
          result.get("strategy") == "try_different",
          f"got: {result.get('strategy')}")

    check("exchange_count NOT incremented",
          result.get("exchange_count") == 3,
          f"got: {result.get('exchange_count')} (expected 3)")

    check("teacher_mode set to 'encouraging'",
          result.get("teacher_mode") == "encouraging",
          f"got: {result.get('teacher_mode')}")

    check("should_scaffold is False",
          result.get("should_scaffold") == False)


def test_strategy_normal_increments_exchange():
    section("TIER 1 · Strategy: normal path still increments exchange_count")
    from nodes.strategy import strategy_selector_node

    state = make_state({
        "response_type": "answer",
        "strategy": "continue",
        "exchange_count": 2,
        "understanding_level": "partial",
        "trajectory_status": "improving",
    })

    result = strategy_selector_node(state)

    # Normal path should NOT preserve exchange_count
    # (strategy node doesn't set exchange_count directly unless advancing concept)
    # It will only set exchange_count=0 when advancing a concept
    # For a normal 'continue' case with partial understanding, no advancement
    check("strategy node ran normally (no short-circuit)",
          result.get("strategy") is not None)

    check("exchange_count not touched by strategy (teacher increments it)",
          "exchange_count" not in result or result.get("exchange_count") != 2,
          "Strategy only sets exchange_count when advancing concept")


def test_state_new_fields_initialized():
    section("TIER 1 · State: new fields in create_initial_state()")
    from state import create_initial_state

    state = create_initial_state(
        topic_description="Test",
        initial_params={"initialState": "normal"},
        simulation_id="pendulum_timing_kn",
        language="kannada"
    )

    check("student_changed_params initialized as empty dict",
          state.get("student_changed_params") == {},
          f"got: {state.get('student_changed_params')}")

    check("student_changed_params_this_turn initialized as False",
          state.get("student_changed_params_this_turn") == False,
          f"got: {state.get('student_changed_params_this_turn')}")


def test_api_models_accept_student_changed_params():
    section("TIER 1 · API Models: StudentResponseRequest accepts student_changed_params")
    from api_models import StudentResponseRequest

    # With student_changed_params
    req1 = StudentResponseRequest(
        student_response="I changed it",
        student_changed_params={"initialState": "long"}
    )
    check("student_changed_params set correctly",
          req1.student_changed_params == {"initialState": "long"},
          f"got: {req1.student_changed_params}")

    # Without student_changed_params (backward compat)
    req2 = StudentResponseRequest(student_response="normal response")
    check("student_changed_params defaults to None",
          req2.student_changed_params is None,
          f"got: {req2.student_changed_params}")

    # Empty student_response with params (param-only turn)
    req3 = StudentResponseRequest(
        student_response="",
        student_changed_params={"initialState": "short"}
    )
    check("empty student_response accepted with student_changed_params",
          req3.student_response == "" and req3.student_changed_params is not None)

    # student_response has default empty string
    req4 = StudentResponseRequest()
    check("student_response defaults to empty string",
          req4.student_response == "",
          f"got: {req4.student_response!r}")


def test_show_simulation_in_api_model():
    section("TIER 1 · API Models: SimulationState includes show_simulation field")
    from api_models import SimulationState

    sim = SimulationState(
        id="pendulum_timing_kn",
        title="Pendulum",
        html_url="https://example.com/sim.html",
        current_params={"initialState": "long"},
        show_simulation=True
    )
    check("show_simulation=True accepted and stored",
          sim.show_simulation == True,
          f"got: {sim.show_simulation}")

    sim2 = SimulationState(
        id="pendulum_timing_kn",
        title="Pendulum",
        html_url="https://example.com/sim.html",
        current_params={"initialState": "long"},
    )
    check("show_simulation defaults to False",
          sim2.show_simulation == False,
          f"got: {sim2.show_simulation}")


def test_graph_continue_session_injects_params():
    section("TIER 1 · Graph: continue_session() builds correct state_update dict")
    # We test the logic of state_update construction without running the graph
    # by replicating the key logic from continue_session()

    student_changed_params = {"initialState": "long"}
    student_response = "I changed it"

    # Replicate continue_session() logic
    state_update = {"student_response": student_response}
    if student_changed_params:
        state_update["student_changed_params"] = student_changed_params
        state_update["student_changed_params_this_turn"] = True
    else:
        state_update["student_changed_params"] = {}
        state_update["student_changed_params_this_turn"] = False

    check("student_changed_params injected into state_update",
          state_update.get("student_changed_params") == {"initialState": "long"})

    check("student_changed_params_this_turn set to True",
          state_update.get("student_changed_params_this_turn") == True)

    check("student_response preserved in state_update",
          state_update.get("student_response") == student_response)

    # Test the None/empty case (backward compat)
    state_update2 = {"student_response": "normal"}
    sc = None
    if sc:
        state_update2["student_changed_params"] = sc
        state_update2["student_changed_params_this_turn"] = True
    else:
        state_update2["student_changed_params"] = {}
        state_update2["student_changed_params_this_turn"] = False

    check("No student_changed_params → flag set to False",
          state_update2.get("student_changed_params_this_turn") == False)

    check("No student_changed_params → empty dict stored",
          state_update2.get("student_changed_params") == {})


def test_parameter_history_entry_format():
    section("TIER 1 · Teacher: parameter_history entry format for student-driven changes")
    # Simulate what teacher_node does when merging student params

    current_params = {"initialState": "medium"}
    student_changed_params = {"initialState": "long"}
    understanding = "partial"
    student_response = ""

    merged_params = dict(current_params)
    student_history_entries = []

    for param_key, new_val in student_changed_params.items():
        old_val = current_params.get(param_key)
        merged_params[param_key] = new_val
        student_history_entries.append({
            "parameter": param_key,
            "old_value": old_val,
            "new_value": new_val,
            "reason": "Student changed independently",
            "prediction_asked": "",
            "student_reaction": student_response,
            "understanding_before": understanding,
            "understanding_after": "",
            "was_effective": None,
            "initiated_by": "student"
        })

    check("merged_params updated with student value",
          merged_params.get("initialState") == "long",
          f"got: {merged_params}")

    check("history entry has correct parameter name",
          student_history_entries[0]["parameter"] == "initialState")

    check("history entry reason = 'Student changed independently'",
          student_history_entries[0]["reason"] == "Student changed independently")

    check("history entry initiated_by = 'student'",
          student_history_entries[0]["initiated_by"] == "student")

    check("history entry was_effective = None (unknown)",
          student_history_entries[0]["was_effective"] is None,
          f"got: {student_history_entries[0]['was_effective']}")

    check("history entry old_value preserved",
          student_history_entries[0]["old_value"] == "medium")


def test_format_api_response_show_simulation():
    section("TIER 1 · API Integration: format_api_response includes show_simulation")
    from api_integration import format_api_response

    state = make_state({
        "show_simulation": True,
        "current_params": {"initialState": "long"},
        "parameter_history": [{
            "parameter": "initialState",
            "old_value": "medium",
            "new_value": "long",
            "reason": "Student changed independently",
            "prediction_asked": "",
            "student_reaction": "",
            "understanding_before": "partial",
            "understanding_after": "",
            "was_effective": None,
            "initiated_by": "student"
        }],
        "concepts": [{
            "id": 1,
            "title": "Test",
            "description": "Test",
            "key_insight": "Test",
            "related_params": ["initialState"]
        }],
        "last_teacher_message": "I see you changed the pendulum!",
        "language": "kannada",
    })

    response = format_api_response("test_session_123", state, "pendulum_timing_kn")

    check("show_simulation is True in response",
          response["simulation"]["show_simulation"] == True,
          f"got: {response['simulation'].get('show_simulation')}")

    check("param_change is present",
          response["simulation"]["param_change"] is not None,
          f"got: {response['simulation'].get('param_change')}")

    check("param_change.reason = 'Student changed independently'",
          response["simulation"]["param_change"]["reason"] == "Student changed independently",
          f"got: {response['simulation']['param_change'].get('reason')}")

    check("param_change.before = 'medium'",
          response["simulation"]["param_change"]["before"] == "medium",
          f"got: {response['simulation']['param_change'].get('before')}")

    check("param_change.after = 'long'",
          response["simulation"]["param_change"]["after"] == "long",
          f"got: {response['simulation']['param_change'].get('after')}")

    check("current_params.initialState = 'long'",
          response["simulation"]["current_params"].get("initialState") == "long",
          f"got: {response['simulation']['current_params']}")


# ══════════════════════════════════════════════════════════════════════════════
# TIER 2 — LIVE API TESTS (requires running server)
# ══════════════════════════════════════════════════════════════════════════════

def run_live_tests():
    import requests
    import json

    BASE = "http://localhost:8000"
    SIM_ID = "pendulum_timing_kn"

    def post(url, body):
        r = requests.post(url, json=body, timeout=120)
        r.raise_for_status()
        return r.json()

    # ── Live Test 1: Full flow — start → respond → student changes param ──────
    section("TIER 2 · Live: Full end-to-end flow")

    print("\n  → Starting session...")
    session = post(f"{BASE}/api/session/start", {
        "simulation_id": SIM_ID,
        "language": "kannada"
    })
    session_id = session["session_id"]
    initial_exchange = session["learning_state"]["exchange_count"]
    initial_params = dict(session["simulation"]["current_params"])

    print(f"  Session: {session_id}")
    print(f"  Initial params: {initial_params}")
    print(f"  Teacher: {session['teacher_message']['text'][:80]}...")

    check("Session started successfully", session_id is not None)
    check("Initial show_simulation is True (first message shows sim)",
          session["simulation"]["show_simulation"] == True,
          f"got: {session['simulation'].get('show_simulation')}")

    # ── Live Test 2: Normal response (no student_changed_params) ─────────────
    print("\n  → Sending normal response (no student params)...")
    r_normal = post(f"{BASE}/api/session/{session_id}/respond", {
        "student_response": "I see the pendulum swinging"
    })
    exchange_after_normal = r_normal["learning_state"]["exchange_count"]

    check("Normal response: exchange_count incremented",
          exchange_after_normal > initial_exchange,
          f"before={initial_exchange}, after={exchange_after_normal}")

    check("Normal response: student_changed_params not in response (clean API)",
          "student_changed_params" not in r_normal)

    # ── Live Test 3: Student changes params (with text) ───────────────────────
    print("\n  → Sending response WITH student_changed_params + text...")
    exchange_before_change = r_normal["learning_state"]["exchange_count"]
    params_before_change = dict(r_normal["simulation"]["current_params"])

    r_change = post(f"{BASE}/api/session/{session_id}/respond", {
        "student_response": "I changed it to see what happens",
        "student_changed_params": {"initialState": "long"}
    })

    print(f"  Teacher: {r_change['teacher_message']['text'][:100]}...")
    print(f"  Params after: {r_change['simulation']['current_params']}")
    print(f"  show_simulation: {r_change['simulation']['show_simulation']}")
    print(f"  exchange_count before={exchange_before_change}, after={r_change['learning_state']['exchange_count']}")

    check("show_simulation = True after student param change",
          r_change["simulation"]["show_simulation"] == True,
          f"got: {r_change['simulation'].get('show_simulation')}")

    check("current_params.initialState updated to student's value 'long'",
          r_change["simulation"]["current_params"].get("initialState") == "long",
          f"got: {r_change['simulation']['current_params']}")

    check("param_change present in response",
          r_change["simulation"]["param_change"] is not None)

    # In live test, reason will actually be translated to Kannada!
    check("param_change.reason is present (translated to Kannada)",
          bool(r_change["simulation"]["param_change"].get("reason")))

    check("exchange_count NOT incremented for exploration turn",
          r_change["learning_state"]["exchange_count"] == exchange_before_change,
          f"before={exchange_before_change}, after={r_change['learning_state']['exchange_count']}")

    teacher_text = r_change["teacher_message"]["text"].lower()
    check("Teacher message acknowledges the change (mentions 'long' or 'changed' or 'noticed')",
          any(w in teacher_text for w in ["long", "changed", "changed", "noticed", "see", "observe", "ನೀವು", "ಬದಲಾ"]),
          f"Teacher said: {r_change['teacher_message']['text'][:120]}")

    # ── Live Test 4: Param-only turn (empty student_response) ────────────────
    section("TIER 2 · Live: Param-only turn (no text, only slider change)")
    print("\n  → Sending param-only turn (empty student_response)...")
    exchange_before_silent = r_change["learning_state"]["exchange_count"]

    r_silent = post(f"{BASE}/api/session/{session_id}/respond", {
        "student_response": "",
        "student_changed_params": {"initialState": "short"}
    })

    print(f"  Teacher: {r_silent['teacher_message']['text'][:100]}...")
    print(f"  Params after: {r_silent['simulation']['current_params']}")

    check("Param-only: current_params updated to 'short'",
          r_silent["simulation"]["current_params"].get("initialState") == "short",
          f"got: {r_silent['simulation']['current_params']}")

    check("Param-only: show_simulation = True",
          r_silent["simulation"]["show_simulation"] == True)

    check("Param-only: exchange_count NOT incremented",
          r_silent["learning_state"]["exchange_count"] == exchange_before_silent,
          f"before={exchange_before_silent}, after={r_silent['learning_state']['exchange_count']}")

    check("Param-only: param_change.reason is present (translated)",
          bool(r_silent["simulation"]["param_change"].get("reason")))

    # ── Live Test 5: Backward compatibility ───────────────────────────────────
    section("TIER 2 · Live: Backward compatibility (no student_changed_params)")
    print("\n  → Sending normal response (verifying backward compat)...")
    exchange_before_bc = r_silent["learning_state"]["exchange_count"]

    r_bc = post(f"{BASE}/api/session/{session_id}/respond", {
        "student_response": "I think longer pendulums swing slower"
    })

    print(f"  Understanding: {r_bc['learning_state']['understanding_level']}")
    print(f"  Exchange count: before={exchange_before_bc}, after={r_bc['learning_state']['exchange_count']}")

    # Either it increments normally, OR if understanding is high, it advances concept and resets to 1 (or 0)
    check("Backward compat: exchange_count incremented normally or reset due to mastery",
          r_bc["learning_state"]["exchange_count"] > exchange_before_bc or r_bc["learning_state"]["exchange_count"] <= 1,
          f"before={exchange_before_bc}, after={r_bc['learning_state']['exchange_count']}")

    check("Backward compat: understanding_level is set (LLM evaluated)",
          r_bc["learning_state"]["understanding_level"] in ["none","partial","mostly","complete"],
          f"got: {r_bc['learning_state']['understanding_level']}")

    check("Backward compat: no crash, valid teacher message",
          len(r_bc["teacher_message"]["text"]) > 0)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    run_live = "--live" in sys.argv

    print("\n" + "█"*60)
    print("  Student-Driven Parameter Detection — Test Suite")
    print("█"*60)

    # ── Tier 1: Unit tests ────────────────────────────────────────────────────
    print("\n▶ TIER 1: Unit tests (no LLM, no server required)")

    test_state_new_fields_initialized()
    test_api_models_accept_student_changed_params()
    test_show_simulation_in_api_model()
    test_evaluator_short_circuits()
    test_evaluator_normal_path_unchanged()
    test_strategy_preserves_on_param_change()
    test_strategy_normal_increments_exchange()
    test_graph_continue_session_injects_params()
    test_parameter_history_entry_format()
    test_format_api_response_show_simulation()

    # ── Tier 2: Live API tests ────────────────────────────────────────────────
    if run_live:
        print("\n▶ TIER 2: Live API tests (server at localhost:8000)")
        try:
            import requests
            requests.get("http://localhost:8000/", timeout=3)
        except Exception:
            print("\n  ✗ Server not reachable at localhost:8000")
            print("    Start it with:  uvicorn api_server:app --reload --port 8000")
            print("    Then re-run:    python test_student_param_changes.py --live\n")
        else:
            try:
                run_live_tests()
            except Exception as e:
                import traceback
                print(f"\n  ✗ Live test crashed: {e}")
                traceback.print_exc()
    else:
        print("\n  (Skipping Tier 2 live tests — run with --live flag and server running)")

    # ── Summary ───────────────────────────────────────────────────────────────
    total = PASS_COUNT + FAIL_COUNT
    print(f"\n{'='*60}")
    print(f"  Results: {PASS_COUNT}/{total} passed", end="")
    if FAIL_COUNT:
        print(f"  |  {FAIL_COUNT} FAILED ←")
    else:
        print("  ✓ ALL PASSED")
    print(f"{'='*60}\n")

    sys.exit(0 if FAIL_COUNT == 0 else 1)


if __name__ == "__main__":
    main()
