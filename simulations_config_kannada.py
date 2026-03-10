"""
Simulations Configuration - Kannada (ಕನ್ನಡ)
=============================================
Contains metadata, parameters, concepts, and quiz questions for
Kannada-medium simulations designed for native-language learners.

These simulations have their UI, labels, and instructions written in Kannada.
The agent pipeline continues to operate in English for consistent evaluation;
the translation layer handles student-facing communication in Kannada.

Each entry follows the EXACT same structure as simulations_config.py so that
all existing helper functions (get_simulation, get_quiz_questions, etc.) work
transparently after this file is merged at runtime.

This file is imported and merged into simulations_config.py at the bottom of
that file via:
    from simulations_config_kannada import SIMULATIONS_KN, QUIZ_QUESTIONS_KN
    SIMULATIONS.update(SIMULATIONS_KN)
    QUIZ_QUESTIONS.update(QUIZ_QUESTIONS_KN)
"""

# ═══════════════════════════════════════════════════════════════════════
# KANNADA SIMULATION DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════

SIMULATIONS_KN = {}


# =============================================================================
# INDUSTRIAL WASTE TREATMENT SIMULATION
# ಕೈಗಾರಿಕಾ ತ್ಯಾಜ್ಯ ಚಿಕಿತ್ಸೆ – ನಮ್ಮ ನೀರನ್ನು ರಕ್ಷಿಸುವುದು
# Science Chapter 2 – Acids, Bases and Salts (Neutralization)
# =============================================================================
SIMULATIONS_KN["industrial_waste_treatment_kn"] = {
    "title": "ಕೈಗಾರಿಕಾ ತ್ಯಾಜ್ಯ ಚಿಕಿತ್ಸೆ (Industrial Waste Treatment)",

    # Mark as Kannada so the sidebar can group it separately
    "language": "kannada",

    # Relative path from the project root — matches the folder structure
    "file": "simulations_kannada/science_chapter2_simulation10_industrial_waste_treatment_kn.html",

    "description": """
An interactive Kannada-language simulation demonstrating how acidic industrial
waste must be neutralised with a base (alkali) before being discharged into a river.

Students experience two contrasting scenarios:
- Releasing UNTREATED acidic waste (pH 3) directly into the river
  → fish die, water turns dark, status: disaster (ಅನಾಹುತ)
- NEUTRALISING the acidic waste with alkali (pH rises to 7) before release
  → river stays clean, fish survive, status: safe (ಸುರಕ್ಷಿತ)

The simulation teaches:
- Neutralisation reaction: acid + base → salt + water
- pH scale: acidic (pH 3) vs neutral (pH 7) vs safe water
- Environmental responsibility: mandatory waste treatment before discharge
- Real-world connection: factory regulations requiring effluent treatment

The simulation UI, labels, and narrative are entirely in Kannada for native
language learners. Driving parameters are exposed via URL query strings so
the teaching agent can set the demonstration state directly.
""",

    "cannot_demonstrate": [
        "Specific balanced chemical equations for neutralisation",
        "Effect of alkaline (basic) waste on the river",
        "Intermediate partial-neutralisation pH states",
        "Multiple simultaneous acid-base scenarios",
        "Quantitative measurement of reagent amounts",
        "Any chemical other than a generic acid/alkali pair"
    ],

    # ── Agent-controllable parameters ──────────────────────────────────────
    # initialState : string  – controls which demonstration state to auto-load
    # showHints    : bool    – toggles the explanatory insight box in the UI
    "initial_params": {
        "initialState": "initial",
        "showHints": True
    },

    "parameter_info": {
        "initialState": {
            "label": "Simulation State",
            "range": "initial, polluted, treated",
            "url_key": "initialState",
            "effect": (
                "Sets which state the simulation auto-loads into on page open.\n"
                "  'initial'  → clean river, healthy fish, pH 7 (default starting view)\n"
                "  'polluted' → untreated acidic waste (pH 3) released; fish die, river darkens\n"
                "  'treated'  → acidic waste neutralised with alkali (pH → 7) before release; river safe"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": (
                "Controls visibility of the insight explanation box inside the simulation.\n"
                "  true  → show the 'Why treatment matters' explanation panel (default)\n"
                "  false → hide the explanation panel (cleaner view for focused observation)"
            )
        }
    },

    # ── Teaching concepts ───────────────────────────────────────────────────
    # 3 concepts in progression: problem → solution → broader understanding
    "concepts": [
        {
            "id": 1,
            "title": "Acidic Industrial Waste and Its Harm",
            "description": (
                "Understanding why untreated acidic industrial waste is dangerous to "
                "aquatic ecosystems and the living organisms that depend on rivers."
            ),
            "key_insight": (
                "Factory effluent is often strongly acidic (pH around 3). Discharging it "
                "untreated destroys the gills of fish and other aquatic life, killing them. "
                "A pH of 3 is 10,000 times more acidic than neutral water (pH 7)."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Neutralisation: The Solution to Acidic Waste",
            "description": (
                "How adding a base (alkali) to acidic industrial waste chemically neutralises "
                "it — raising the pH to 7 so the water is safe to release into the river."
            ),
            "key_insight": (
                "Neutralisation reaction: Acid + Base → Salt + Water. "
                "Adding alkali (like lime / calcium hydroxide) to acidic factory waste "
                "converts it from pH 3 to pH 7 (neutral), making it safe for aquatic life."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Environmental Responsibility and pH",
            "description": (
                "How the pH scale measures acidity and alkalinity, and why environmental "
                "regulations require factories to treat their waste before discharge."
            ),
            "key_insight": (
                "pH 7 is neutral — the safe level for rivers and aquatic life. "
                "Factories are legally required to neutralise acidic waste before releasing it. "
                "This is a direct application of the acid-base neutralisation concept "
                "to real-world environmental protection."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}


# ═══════════════════════════════════════════════════════════════════════
# QUIZ QUESTIONS — KANNADA SIMULATIONS
# ═══════════════════════════════════════════════════════════════════════

QUIZ_QUESTIONS_KN = {}


# =============================================================================
# INDUSTRIAL WASTE TREATMENT — QUIZ QUESTIONS
# 3 questions: observe harm → show correct treatment → verify clean state
#
# Quiz parameters:
#   initialState (string): 'initial' | 'polluted' | 'treated'
#   The student selects from a dropdown in the Streamlit quiz UI.
#   The simulation iframe reflects the chosen state via URL param ?initialState=…
#   Evaluation uses string equality (handled by quiz_rules.py string fallback).
# =============================================================================

QUIZ_QUESTIONS_KN["industrial_waste_treatment_kn"] = [

    # ── Q1: Show the HARMFUL scenario ──────────────────────────────────────
    {
        "id": "waste_kn_q1",
        "challenge": (
            "Show what happens when acidic industrial waste is released into the "
            "river WITHOUT any treatment. Set the simulation to demonstrate the "
            "harmful effect of untreated acid discharge on the river and fish.\n\n"
            "(ಚಿಕಿತ್ಸೆ ಇಲ್ಲದ ಆಮ್ಲೀಯ ತ್ಯಾಜ್ಯ ನದಿಗೆ ಬಿಟ್ಟರೆ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "initialState",
                    "operator": "==",
                    "value": "polluted"
                }
            ],
            "scoring": {
                "perfect": 1.0,
                "partial": 0.5,
                "wrong": 0.2
            }
        },
        "hints": {
            "attempt_1": (
                "Use the dropdown in Streamlit to select 'polluted' as the Simulation State. "
                "This will show the untreated acidic waste (pH 3) being released into the "
                "river — watch what happens to the fish."
            ),
            "attempt_2": (
                "Set 'initialState' to 'polluted'. The simulation will show: waste flows in, "
                "river turns dark, fish die. This is the result of uncontrolled acid discharge."
            ),
            "attempt_3": (
                "Select 'polluted' from the Simulation State dropdown. "
                "You will see the disaster scenario: acidic waste (pH 3) kills the fish "
                "by destroying their gills."
            )
        },
        "concept_reminder": (
            "Untreated acidic industrial waste has a very low pH (around 3). "
            "When released directly into rivers, the acid destroys fish gills and kills "
            "aquatic life. This is why factories must NEVER discharge untreated effluent. "
            "(ಅನಾಹುತ! ಚಿಕಿತ್ಸೆ ಇಲ್ಲದ ಆಮ್ಲೀಯ ತ್ಯಾಜ್ಯ ಮೀನುಗಳನ್ನು ಸಾಯಿಸುತ್ತದೆ!)"
        )
    },

    # ── Q2: Show the CORRECT treatment scenario ────────────────────────────
    {
        "id": "waste_kn_q2",
        "challenge": (
            "Now show the CORRECT procedure: demonstrate how proper neutralisation "
            "treatment makes the waste safe before it enters the river. "
            "Set the simulation to show the treated outcome.\n\n"
            "(ಸರಿಯಾದ ಚಿಕಿತ್ಸೆ ಮಾಡಿದ ನಂತರ ನೀರು ಸುರಕ್ಷಿತವಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "initialState",
                    "operator": "==",
                    "value": "treated"
                }
            ],
            "scoring": {
                "perfect": 1.0,
                "partial": 0.5,
                "wrong": 0.2
            }
        },
        "hints": {
            "attempt_1": (
                "Select 'treated' from the Simulation State dropdown. "
                "This shows neutralisation in action: alkali is added to the acidic waste, "
                "raising pH from 3 to 7 (neutral), making the water safe for aquatic life."
            ),
            "attempt_2": (
                "Set 'initialState' to 'treated'. You will see the correct procedure: "
                "first the waste is released (acidic), then alkali is added for neutralisation "
                "(acid + base → salt + water), and finally the river stays clean."
            ),
            "attempt_3": (
                "Choose 'treated' as the Simulation State. "
                "The treated scenario shows: alkali neutralises the acid, pH becomes 7, "
                "fish survive, river remains clean — the success of proper waste management."
            )
        },
        "concept_reminder": (
            "Neutralisation: Acid + Base → Salt + Water. "
            "Adding alkali (base) to acidic industrial waste brings the pH from 3 to 7 "
            "(neutral). Water at pH 7 is safe for fish and aquatic life. "
            "This is the core of industrial effluent treatment. "
            "(ಯಶಸ್ಸು! ಕ್ಷಾರ ಸೇರಿಸಿ ತಟಸ್ಥೀಕರಣ ಮಾಡಿದ ನೀರು pH 7 ಆಗಿ ಸುರಕ್ಷಿತವಾಗುತ್ತದೆ!)"
        )
    },

    # ── Q3: Identify the clean baseline ────────────────────────────────────
    {
        "id": "waste_kn_q3",
        "challenge": (
            "Show the INITIAL clean state of the river — before any industrial "
            "discharge occurs. This represents the healthy ecosystem that proper "
            "waste management protects.\n\n"
            "(ಯಾವುದೇ ತ್ಯಾಜ್ಯ ಬಿಡುಗಡೆ ಮೊದಲು ನದಿಯ ಸ್ಥಿತಿ ಹೇಗಿರುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "initialState",
                    "operator": "==",
                    "value": "initial"
                }
            ],
            "scoring": {
                "perfect": 1.0,
                "partial": 0.5,
                "wrong": 0.2
            }
        },
        "hints": {
            "attempt_1": (
                "Select 'initial' from the Simulation State dropdown. "
                "This shows the starting state: a clean river at pH 7 with healthy fish "
                "— the natural state that waste treatment is designed to preserve."
            ),
            "attempt_2": (
                "Set 'initialState' to 'initial'. You will see the clean river before "
                "any factory discharge. Notice the pH is already 7 (neutral) and fish are "
                "swimming healthily."
            ),
            "attempt_3": (
                "Choose 'initial' to display the pristine river (pH 7, healthy fish). "
                "This is the ecosystem we must protect through mandatory waste treatment."
            )
        },
        "concept_reminder": (
            "A healthy river ecosystem has a pH of around 7 (neutral). "
            "Fish and aquatic organisms can only survive within a narrow pH range close to 7. "
            "Industrial waste treatment ensures that discharge maintains this safe pH, "
            "protecting aquatic biodiversity and water quality. "
            "(ಆರೋಗ್ಯಕರ ನದಿ pH 7 ಇರುತ್ತದೆ — ಮೀನುಗಳಿಗೆ ಮತ್ತು ಜಲಚರ ಜೀವಿಗಳಿಗೆ ಸುರಕ್ಷಿತ.)"
        )
    }
]


# ═══════════════════════════════════════════════════════════════════════
# HELPER: list of Kannada simulation IDs for sidebar grouping
# ═══════════════════════════════════════════════════════════════════════

KN_SIMULATION_IDS = list(SIMULATIONS_KN.keys())
