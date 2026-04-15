"""
Simulation Component
====================
Handles displaying simulation iframes (single view).
"""

import sys
from pathlib import Path
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import streamlit.components.v1 as components
from streamlit_config import build_simulation_url, get_simulation_config, UI_CONFIG


# Declare the proper bidirectional component
component_path = str(Path(__file__).parent / "simulation_wrapper")
_simulation_component = components.declare_component("simulation_wrapper", path=component_path)

def render_simulation_single(sim_key: str, params: dict, title: str = "Simulation",
                             unique_id: str = None, capture_changes: bool = False):
    """
    Render a single HTML simulation iframe with bidirectional message support.

    Args:
        sim_key: Simulation key (e.g., "simple_pendulum")
        params: Current parameter values
        title: Title to display above simulation
        unique_id: Optional unique suffix for the component key (needed when
                   rendering multiple simulations on the same page)
        capture_changes: If True, store returned params in pending_student_params.
                         Set False for read-only history displays so they never
                         overwrite the student's live pending changes.
    """
    url = build_simulation_url(sim_key, params, auto_start=True)
    height = UI_CONFIG.get("simulation_height", 600)

    if title:
        st.markdown(f"**{title}**")

    # Build a unique key to avoid DuplicateWidgetID errors when multiple
    # simulations are rendered in the chat history on the same page.
    component_key = f"sim_{sim_key}_{unique_id}" if unique_id else f"sim_{sim_key}"

    # Render component and capture return value (which will be the params JSON)
    returned_params = _simulation_component(url=url, height=height, key=component_key)

    if not capture_changes:
        # Read-only display (chat history) — never touch pending_student_params
        return

    # Parse the returned value into a clean dict (strip internal keys)
    clean_params = None
    if returned_params:
        if isinstance(returned_params, dict):
            clean_params = {k: v for k, v in returned_params.items() if k not in ('__t', 'cmd')}
        elif isinstance(returned_params, str):
            try:
                parsed = json.loads(returned_params)
                clean_params = {k: v for k, v in parsed.items() if k not in ('__t', 'cmd')}
            except Exception:
                pass

    # Ignore empty dicts (e.g. after stripping control keys like cmd)
    if clean_params:
        # ── Autostart echo filter ──────────────────────────────────────────
        # When a simulation loads, its autostart IIFE clicks buttons which
        # triggers the AndroidBridge to send a postMessage with the *resolved*
        # initial state (e.g., URL has initialState=acidic, HTML solutionMap
        # resolves to 'lemon', simulation reports {initialState:'lemon'}).
        # This is NOT a student-initiated change.  We detect autostart echoes
        # by tracking the URL: the first param report for a given URL is always
        # the autostart echo (the "baseline").  Only subsequent *different*
        # reports from the same URL are genuine student interactions.
        url_key = f"_sim_url_{component_key}"
        baseline_key = f"_sim_baseline_{component_key}"

        current_url = url  # the URL we just passed to the iframe

        if st.session_state.get(url_key) != current_url:
            # URL changed (new simulation load or param update from agent).
            # Store the new URL and treat this first report as the baseline.
            st.session_state[url_key] = current_url
            st.session_state[baseline_key] = clean_params
            print(f"   🎛️ Autostart baseline set for new URL: {clean_params}")
        else:
            # Same URL — compare against the baseline
            baseline = st.session_state.get(baseline_key, {})
            if clean_params != baseline:
                # Genuinely different from autostart → real student interaction
                cache_key = f"_last_sim_val_{component_key}"
                if clean_params != st.session_state.get(cache_key):
                    st.session_state[cache_key] = clean_params
                    st.session_state.pending_student_params = clean_params
                    print(f"   🎛️ Streamlit captured param change: {clean_params}")
            else:
                print(f"   🔇 Ignored autostart echo: {clean_params}")

