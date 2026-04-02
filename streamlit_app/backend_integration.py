"""
Backend Integration Module
==========================
Provides a clean interface between the Streamlit app and the LangGraph backend.
Handles session management, state synchronization, and response processing.
"""

import sys
import uuid
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

# Add parent directory to path for backend imports
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Import backend modules
try:
    # Only import what we need - NOT cached constants!
    # Dynamic simulation loading means we DON'T import TOPIC_DESCRIPTION, INITIAL_PARAMS, etc.
    from config import (
        validate_config,
        MAX_EXCHANGES,
        build_simulation_url
    )
    from state import create_initial_state, TeachingState
    from graph import continue_session, get_session_state
    from langchain_core.runnables import RunnableConfig
    
    BACKEND_AVAILABLE = True
    
except Exception as e:
    print(f"Backend import error: {e}")
    import traceback
    traceback.print_exc()
    BACKEND_AVAILABLE = False
    # Set defaults
    INITIAL_PARAMS = {"length": 5, "number_of_oscillations": 10}
    MAX_EXCHANGES = 6

# Translation imports are kept separate so a missing/broken translation module
# does NOT pull down the core backend (BACKEND_AVAILABLE stays True).
try:
    from translation import (
        needs_translation,
        translate,
        translate_to_english,
        translate_to_kannada,
        translate_student_input,
        translate_batch,
        get_language_code,
    )
    TRANSLATION_AVAILABLE = True
except Exception as _t_err:
    print(f"Translation import warning: {_t_err} — translation disabled, English only.")
    TRANSLATION_AVAILABLE = False
    # Stub out helpers so callers never crash
    def needs_translation(language: str) -> bool: return False
    def translate(text, source="en", target="kn"): return text
    def translate_to_english(text): return text
    def translate_to_kannada(text): return text
    def translate_student_input(text, language): return text
    def translate_batch(texts, source="en", target="kn"): return texts
    def get_language_code(language): return "en"


def is_backend_available() -> bool:
    """Check if the backend is available."""
    return BACKEND_AVAILABLE


def create_new_session(simulation_id: str = "simple_pendulum", language: str = "english") -> Tuple[str, Dict[str, Any]]:
    """
    Create a new teaching session for a specific simulation.
    
    Args:
        simulation_id: The ID of the simulation to create a session for
        language: Session language ('english' or 'kannada')
    
    Returns:
        Tuple of (thread_id, initial_state_from_backend)
    """
    if not BACKEND_AVAILABLE:
        raise RuntimeError("Backend not available")
    
    # Dynamically get simulation configuration (NOT from cached module constants!)
    from simulations_config import get_simulation
    sim_config = get_simulation(simulation_id)
    
    if not sim_config:
        raise ValueError(f"Unknown simulation: {simulation_id}")
    
    # Extract simulation-specific data
    topic_description = sim_config['description']
    initial_params = sim_config['initial_params'].copy()
    topic_title = sim_config['title']
    
    # Reload ALL modules to pick up any changes
    import importlib
    import simulations_config
    import config
    import state as state_module
    import graph as graph_module
    from nodes import teacher, evaluator, strategy, trajectory, content_loader
    
    # Reload in dependency order (most fundamental first)
    importlib.reload(simulations_config)
    importlib.reload(config)
    importlib.reload(content_loader)
    importlib.reload(teacher)
    importlib.reload(evaluator)
    importlib.reload(strategy)
    importlib.reload(trajectory)
    importlib.reload(state_module)
    importlib.reload(graph_module)
    
    # Import fresh functions after reload
    from config import validate_config
    from state import create_initial_state
    from graph import start_session, reset_graph
    
    # Reset the graph to force recompile with new nodes
    reset_graph()
    
    # Validate config
    validate_config()
    
    print(f"🔄 Creating session for: {topic_title} ({simulation_id})")
    
    # Create unique session ID
    thread_id = f"streamlit_session_{uuid.uuid4().hex[:8]}"
    
    # Create initial state with simulation_id for dynamic loading
    initial_state = create_initial_state(
        topic_description=topic_description,
        initial_params=initial_params,
        simulation_id=simulation_id,  # Pass simulation_id for content_loader
        language=language  # Pass language for translation
    )
    
    # Start the session - runs until first interrupt (waiting for student input)
    state = start_session(initial_state, thread_id)
    
    return thread_id, state


def send_student_response(thread_id: str, response: str, student_changed_params: dict = None, language: str = "english") -> Dict[str, Any]:
    """
    Send a student response (and optional parameter changes) and get the updated state.
    
    Args:
        thread_id: The session thread ID
        response: Student's response text
        student_changed_params: Parameters changed by the student before sending
        language: Session language for inbound translation
        
    Returns:
        Updated state dict
    """
    if not BACKEND_AVAILABLE:
        raise RuntimeError("Backend not available")
    
    # Translate student input to English if needed
    translated_response = translate_student_input(response, language)
    
    # Import fresh continue_session to ensure we're using the reloaded graph
    from graph import continue_session as fresh_continue_session
    
    state = fresh_continue_session(
        translated_response, 
        thread_id,
        student_changed_params=student_changed_params
    )
    return state


def get_current_state(thread_id: str) -> Dict[str, Any]:
    """
    Get the current state of a session.
    
    Args:
        thread_id: The session thread ID
        
    Returns:
        Current state dict
    """
    if not BACKEND_AVAILABLE:
        return {}
    
    # Import fresh to ensure we're using the reloaded graph
    from graph import get_session_state as fresh_get_session_state
    
    return fresh_get_session_state(thread_id)


def extract_display_data(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract data from backend state for UI display.
    
    Args:
        state: Full backend state
        
    Returns:
        Dict with UI-friendly data
    """
    concepts = state.get("concepts", [])
    current_idx = state.get("current_concept_index", 0)
    
    # Get current concept info
    current_concept = None
    if current_idx < len(concepts):
        current_concept = concepts[current_idx]
    
    # Get parameter change metadata (single simulation display)
    param_history = state.get("parameter_history", [])
    param_change_info = None

    # Get simulation_id from state for dynamic param loading
    simulation_id = state.get("simulation_id", "simple_pendulum")
    default_params = get_initial_params(simulation_id)
    current_params = state.get("current_params", default_params)

    # Use the explicit show_simulation flag set by the teacher node each turn.
    # This mirrors the same logic used in format_api_response (api_integration.py)
    # so the Streamlit UI and the Android API behave identically:
    #   - True  → teacher triggered a display this exact turn (new/different params
    #             OR student explicitly asked to see it)
    #   - False → pure Q&A turn, or duplicate params were suppressed by teacher node
    show_simulation = state.get("show_simulation", False)

    if show_simulation and param_history:
        last_change = param_history[-1]
        print(f"   🔎 DEBUG - Last param change: {last_change.get('parameter')} = {last_change.get('old_value')} → {last_change.get('new_value')}")
        param_change_info = {
            "parameter": last_change["parameter"],
            "old_value": last_change["old_value"],
            "new_value": last_change["new_value"]
        }
        print(f"   ✅ DEBUG - show_simulation=True → displaying simulation")
    else:
        print(f"   🔎 DEBUG - show_simulation=False → no simulation display this turn")
    
    return {
        # Teacher message
        "teacher_message": state.get("last_teacher_message", ""),
        
        # Progress info
        "current_concept_index": current_idx,
        "total_concepts": len(concepts),
        "current_concept": current_concept,
        "concepts": concepts,
        
        # Understanding
        "understanding_level": state.get("understanding_level", "none"),
        "understanding_reasoning": state.get("understanding_reasoning", ""),
        "trajectory_status": state.get("trajectory_status", "improving"),
        
        # Exchange info
        "exchange_count": state.get("exchange_count", 0),
        "max_exchanges": MAX_EXCHANGES,
        
        # Simulation params
        "current_params": current_params,
        "param_change_info": param_change_info,
        "param_history": param_history,
        
        # Session status
        "session_complete": state.get("session_complete", False),
        "concept_complete": state.get("concept_complete", False),
        
        # Teaching context
        "strategy": state.get("strategy", "continue"),
        "teacher_mode": state.get("teacher_mode", "encouraging"),
        
        # Conversation history
        "conversation_history": state.get("conversation_history", []),
        
        # Quiz state
        "quiz_mode": state.get("quiz_mode", False),
        "quiz_questions": state.get("quiz_questions", []),
        "current_quiz_index": state.get("current_quiz_index", 0),
        "quiz_attempts": state.get("quiz_attempts", {}),
        "quiz_scores": state.get("quiz_scores", {}),
        "quiz_complete": state.get("quiz_complete", False),
        "quiz_evaluation": state.get("quiz_evaluation", {})
    }


def translate_display_data(display_data: Dict[str, Any], language: str) -> Dict[str, Any]:
    """
    Translate user-facing text fields in display_data to the target language.
    
    Translates: teacher_message, concept titles/descriptions, quiz questions,
    quiz evaluation feedback. Does NOT translate parameter names/values, IDs, etc.
    
    Args:
        display_data: The dict returned by extract_display_data()
        language: Target language ('english' or 'kannada')
        
    Returns:
        display_data with translated text fields
    """
    if not BACKEND_AVAILABLE or not needs_translation(language):
        return display_data

    target = get_language_code(language)

    # ── Collect all (object, field) pairs that need translation ──────────────
    # We gather every text string into one flat list, translate the whole batch
    # in parallel with a single translate_batch() call, then write results back.
    # This reduces wall-clock time from (N × latency) to (~1 × latency).

    refs: list = []   # list of (container, key)  — container[key] is the text

    # 1. Teacher message
    if display_data.get("teacher_message"):
        refs.append((display_data, "teacher_message"))

    # 2. Current concept fields
    if display_data.get("current_concept"):
        concept = display_data["current_concept"]
        for field in ["title", "description", "key_insight"]:
            if concept.get(field):
                refs.append((concept, field))

    # 3. All concepts list
    for concept in display_data.get("concepts", []):
        for field in ["title", "description", "key_insight"]:
            if concept.get(field):
                refs.append((concept, field))

    # 4. Quiz question challenge text
    for question in display_data.get("quiz_questions", []):
        if question.get("challenge"):
            refs.append((question, "challenge"))

    # 5. Quiz evaluation feedback
    quiz_eval = display_data.get("quiz_evaluation") or {}
    if quiz_eval.get("feedback"):
        refs.append((quiz_eval, "feedback"))

    # 6. Conversation history (teacher messages only)
    for msg in display_data.get("conversation_history", []):
        if msg.get("role") == "teacher" and msg.get("content"):
            refs.append((msg, "content"))

    if not refs:
        return display_data

    # ── Parallel batch translate ──────────────────────────────────────────────
    texts = [container[key] for container, key in refs]
    translated_texts = translate_batch(texts, source="en", target=target)

    for (container, key), translated in zip(refs, translated_texts):
        container[key] = translated

    return display_data


def get_initial_params(simulation_id: str = "simple_pendulum") -> Dict[str, Any]:
    """Get the initial simulation parameters for a specific simulation."""
    if BACKEND_AVAILABLE:
        from simulations_config import get_simulation
        sim_config = get_simulation(simulation_id)
        if sim_config:
            return sim_config['initial_params'].copy()
    return {"length": 5, "number_of_oscillations": 10}


def get_concepts(simulation_id: str = "simple_pendulum") -> list:
    """Get the pre-defined concepts for a specific simulation."""
    if BACKEND_AVAILABLE:
        from simulations_config import get_simulation
        sim_config = get_simulation(simulation_id)
        if sim_config:
            return sim_config['concepts']
    return []


def get_topic_description(simulation_id: str = "simple_pendulum") -> str:
    """Get the topic description for a specific simulation."""
    if BACKEND_AVAILABLE:
        from simulations_config import get_simulation
        sim_config = get_simulation(simulation_id)
        if sim_config:
            return sim_config['description']
    return "Time & Pendulums"


def build_sim_url(params: Dict[str, Any], autostart: bool = True) -> str:
    """Build simulation URL with parameters."""
    if BACKEND_AVAILABLE:
        return build_simulation_url(params, autostart)
    
    # Fallback URL building
    base_url = "https://imhv0609.github.io/simulation_to_concept_version3_github_modified/simulations/simple_pendulum.html"
    url = f"{base_url}?length={params.get('length', 5)}&oscillations={params.get('number_of_oscillations', 10)}"
    if autostart:
        url += "&autoStart=true"
    return url


def submit_quiz_answer(thread_id: str, question_id: str, submitted_params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Submit quiz answer and get evaluation.
    
    Directly runs quiz_evaluator_node without going through the full graph,
    which avoids checkpoint issues when testing quiz mode.
    
    Args:
        thread_id: The session thread ID
        question_id: ID of the question being answered
        submitted_params: Parameters from the simulation
        
    Returns:
        Updated state dict after evaluation
    """
    if not BACKEND_AVAILABLE:
        raise RuntimeError("Backend not available")
    
    from graph import compile_graph
    from nodes.quiz_evaluator import quiz_evaluator_node, quiz_teacher_node, quiz_router
    
    print("\n" + "="*60)
    print("📥 QUIZ SUBMISSION - Direct Evaluation")
    print("="*60)
    print(f"   Thread: {thread_id}")
    print(f"   Question: {question_id}")
    print(f"   Params: {submitted_params}")
    
    # Get graph and config
    graph = compile_graph()
    config = {"configurable": {"thread_id": thread_id}}
    
    # Get current state
    current_snapshot = graph.get_state(config)
    current_state = dict(current_snapshot.values) if current_snapshot.values else {}
    
    # Check if we're in quiz mode
    if not current_state.get("quiz_mode", False):
        print("   ⚠️ Not in quiz mode - using regular continue_session")
        from graph import continue_session
        graph.update_state(config, {"submitted_parameters": submitted_params})
        return continue_session("", thread_id)
    
    print("   ✅ Quiz mode active - running direct evaluation")
    
    # Update state with submitted parameters
    current_state["submitted_parameters"] = submitted_params
    
    # Run quiz_evaluator_node directly
    print("\n" + "="*60)
    print("🔍 QUIZ EVALUATOR - Evaluating Submission")
    print("="*60)
    
    # Create empty config for direct node invocation (outside graph context)
    eval_updates = quiz_evaluator_node(current_state, config={})
    
    # Merge updates into state
    for key, value in eval_updates.items():
        current_state[key] = value
    
    print(f"   ✓ Completed: quiz_evaluator")
    
    # Check if we need to present next question or end
    route_decision = quiz_router(current_state)
    print(f"   Route decision: {route_decision}")
    
    if route_decision == "quiz_teacher":
        # Run quiz_teacher_node to present next question or retry
        teacher_updates = quiz_teacher_node(current_state)
        for key, value in teacher_updates.items():
            current_state[key] = value
        print(f"   ✓ Completed: quiz_teacher")
    else:
        print(f"   ✓ Quiz complete!")
    
    # Save the updated state back to the graph
    graph.update_state(config, current_state, as_node="quiz_teacher")
    
    # Return the updated state
    return current_state
