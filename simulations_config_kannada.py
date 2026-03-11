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


# =============================================================================
# TURMERIC INDICATOR SIMULATION
# ಹಲ್ದಿ ಸೂಚಕ – ಕ್ಷಾರ ಮಾತ್ರ ಗುರುತಿಸುವ ಭಾಗಶಃ ಸೂಚಕ
# Science Chapter 2 – Natural Indicators (partial indicator concept)
# =============================================================================
SIMULATIONS_KN["turmeric_indicator_kn"] = {
    "title": "ಹಲ್ದಿ ಸೂಚಕ (Turmeric Indicator)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation5_turmeric_indicator_kn.html",
    "description": (
        "Kannada simulation: students test household solutions on turmeric paper and "
        "observe that turmeric turns red/brown ONLY with bases. Both acids and neutral "
        "substances leave it yellow — making turmeric a PARTIAL indicator."
    ),
    "cannot_demonstrate": [
        "Distinguishing acids from neutral substances (turmeric stays yellow for both)",
        "Quantitative pH measurement"
    ],
    "initial_params": {"initialState": "basic", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Solution Type",
            "range": "acidic, basic, neutral",
            "url_key": "initialState",
            "effect": (
                "Selects a solution and auto-runs the turmeric test.\n"
                "  'acidic'  → lemon juice — turmeric stays yellow (no change)\n"
                "  'basic'   → soap solution — turmeric turns red/brown\n"
                "  'neutral' → tap water — turmeric stays yellow (same as acid!)"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the insight box and limitation box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Turmeric Detects Bases: Turns Red or Brown",
            "description": (
                "Turmeric paper turns red/reddish-brown when it contacts a basic solution. "
                "Curcumin (the yellow pigment) changes structure in alkaline environments."
            ),
            "key_insight": (
                "Bases turn turmeric RED/BROWN. Soap, baking soda, and lime water all "
                "cause this colour change. The stronger the base, the deeper the red."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Turmeric Cannot Distinguish Acids from Neutral Substances",
            "description": (
                "Unlike litmus, turmeric stays yellow with BOTH acids and neutral substances. "
                "It is therefore a PARTIAL indicator — it can only confirm a base."
            ),
            "key_insight": (
                "Turmeric is PARTIAL: base → red/brown, acid/neutral → yellow. "
                "If turmeric stays yellow, you cannot tell whether the substance is acidic "
                "or neutral without a different test."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Real-World: Soap Stains on Turmeric Fabric Turn Red",
            "description": (
                "Soap (alkaline) reacts with turmeric stains on clothing producing "
                "a red/brown colour — the same reaction seen in the simulation."
            ),
            "key_insight": (
                "Soap is alkaline; curcumin on fabric reacts with the alkali and turns red. "
                "This is a real-world natural indicator showing acid-base behaviour."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["turmeric_indicator_kn"] = [
    {
        "id": "turmeric_q1",
        "challenge": (
            "Set the simulation to demonstrate what happens when a BASIC (alkaline) solution "
            "is added to turmeric paper. Show the characteristic colour change.\n\n"
            "(ಕ್ಷಾರ ದ್ರಾವಣ ಹಲ್ದಿ ಕಾಗದಕ್ಕೆ ಸೋಕಿದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' as the Simulation State — soap solution on turmeric produces a dramatic red/brown colour change.",
            "attempt_2": "Set 'initialState' to 'basic'. Curcumin reacts with alkaline solutions to turn red/brown.",
            "attempt_3": "Choose 'basic': soap turns turmeric red/brown — the definitive sign of a base."
        },
        "concept_reminder": (
            "Turmeric turns RED/BROWN with bases. Curcumin changes structure in alkaline conditions. "
            "Soap, baking soda, and lime water all produce this change. "
            "(ಕ್ಷಾರ ಹಲ್ದಿಯನ್ನು ಕೆಂಪಾಗಿಸುತ್ತದೆ!)"
        )
    },
    {
        "id": "turmeric_q2",
        "challenge": (
            "Show what happens when an ACIDIC solution is added to turmeric paper. "
            "Observe whether the colour changes — what does this reveal about turmeric as an indicator?\n\n"
            "(ಆಮ್ಲ ದ್ರಾವಣ ಹಲ್ದಿ ಕಾಗದಕ್ಕೆ ಸೋಕಿದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' — lemon juice on turmeric. Notice NO colour change occurs; turmeric stays yellow.",
            "attempt_2": "Set 'initialState' to 'acidic'. Turmeric stays yellow with acids — proving it is a partial indicator.",
            "attempt_3": "Choose 'acidic': turmeric stays yellow with lemon juice; acids do NOT trigger the colour change."
        },
        "concept_reminder": (
            "Turmeric stays YELLOW with acids — no change. "
            "This is turmeric's limitation: acids and neutral substances both leave it yellow. "
            "(ಆಮ್ಲ ಹಲ್ದಿಯನ್ನು ಹಳದಿ ಉಳಿಸುತ್ತದೆ — ಬದಲಾವಣೆ ಇಲ್ಲ!)"
        )
    },
    {
        "id": "turmeric_q3",
        "challenge": (
            "Show what happens with a NEUTRAL substance on turmeric paper. "
            "Explain why this makes turmeric a PARTIAL indicator.\n\n"
            "(ತಟಸ್ಥ ದ್ರಾವಣ ಹಲ್ದಿ ಕಾಗದಕ್ಕೆ ಸೋಕಿದಾಗ ಏನಾಗುತ್ತದೆ — ಹಲ್ದಿ ಯಾಕೆ ಭಾಗಶಃ ಸೂಚಕ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "neutral"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'neutral' — tap water on turmeric. It stays yellow, identical to the acid result.",
            "attempt_2": "Set 'initialState' to 'neutral'. Same yellow as an acid — making it impossible to distinguish them.",
            "attempt_3": "Choose 'neutral': tap water leaves turmeric yellow, same as an acid, proving turmeric cannot tell them apart."
        },
        "concept_reminder": (
            "Neutral substances leave turmeric YELLOW — same as acids. "
            "Turmeric is PARTIAL: confirms base (red/brown) but cannot separate acid from neutral. "
            "A COMPLETE indicator (litmus, rose extract) distinguishes all three types. "
            "(ಹಲ್ದಿ ಭಾಗಶಃ ಸೂಚಕ — ಕ್ಷಾರ ಮಾತ್ರ ಗುರುತಿಸಬಲ್ಲದು!)"
        )
    }
]


# =============================================================================
# RED ROSE INDICATOR SIMULATION
# ಕೆಂಪು ಗುಲಾಬಿ ಸೂಚಕ – ಪೂರ್ಣ ನೈಸರ್ಗಿಕ ಸೂಚಕ (ಆಮ್ಲ, ಕ್ಷಾರ, ತಟಸ್ಥ ಎಲ್ಲ ಗುರುತಿಸಬಲ್ಲದು)
# Science Chapter 2 – Natural Indicators (complete indicator)
# =============================================================================
SIMULATIONS_KN["red_rose_indicator_kn"] = {
    "title": "ಕೆಂಪು ಗುಲಾಬಿ ಸೂಚಕ (Red Rose Indicator)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation4_red_rose_indicator_kn.html",
    "description": (
        "Kannada simulation: students test household solutions with rose petal extract and "
        "observe three distinct colours — red (acid), green (base), pink (neutral). "
        "Rose extract is a COMPLETE indicator containing anthocyanins that respond to both "
        "acids and bases, unlike turmeric which only responds to bases."
    ),
    "cannot_demonstrate": [
        "Quantitative pH values",
        "Direct comparison with litmus paper side-by-side",
        "Effect of highly concentrated acids or bases"
    ],
    "initial_params": {"initialState": "acidic", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Solution Type",
            "range": "acidic, basic, neutral",
            "url_key": "initialState",
            "effect": (
                "Selects a solution and auto-runs the colour test.\n"
                "  'acidic'  → lemon juice — rose extract turns RED\n"
                "  'basic'   → soap solution — rose extract turns GREEN\n"
                "  'neutral' → tap water — rose extract stays PINK (no change)"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the insight box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Acids Turn Rose Extract Red",
            "description": (
                "Rose petal extract turns bright red when added to an acidic solution. "
                "H⁺ ions from the acid cause anthocyanin pigment to shift to its red form."
            ),
            "key_insight": (
                "Acids → rose extract turns RED. Lemon juice, vinegar, orange juice all "
                "produce this colour change. Easy identification of an acid."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Bases Turn Rose Extract Green",
            "description": (
                "Rose petal extract turns green when added to a basic (alkaline) solution. "
                "OH⁻ ions cause anthocyanin to shift to its green form."
            ),
            "key_insight": (
                "Bases → rose extract turns GREEN — the most striking change. "
                "Soap, baking soda, and lime water all produce green. "
                "Green is the exact opposite of the acid red."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Rose Extract is a Complete Indicator",
            "description": (
                "Unlike turmeric (partial), rose extract shows three distinct colours: "
                "red (acid), green (base), pink/unchanged (neutral)."
            ),
            "key_insight": (
                "Rose stays PINK with neutral substances. "
                "RED=acid, GREEN=base, PINK=neutral — three distinct results. "
                "This makes rose extract as powerful as litmus, using natural materials."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["red_rose_indicator_kn"] = [
    {
        "id": "rose_q1",
        "challenge": (
            "Show what colour change happens when an ACID is added to red rose petal extract. "
            "Set the simulation to demonstrate the acid colour response.\n\n"
            "(ಆಮ್ಲ ಸೇರಿಸಿದಾಗ ಗುಲಾಬಿ ಸಾರ ಯಾವ ಬಣ್ಣಕ್ಕೆ ಬದಲಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' as the Simulation State — lemon juice turns rose extract RED.",
            "attempt_2": "Set 'initialState' to 'acidic'. Anthocyanins shift to red form with H⁺ ions from acids.",
            "attempt_3": "Choose 'acidic': lemon juice turns rose extract RED — confirming it is an acid."
        },
        "concept_reminder": (
            "Acids turn rose extract RED. Anthocyanin reacts with H⁺ ions to produce red colour. "
            "Lemon, vinegar, orange juice all turn it red. "
            "(ಆಮ್ಲ ಗುಲಾಬಿ ಸಾರವನ್ನು ಕೆಂಪಾಗಿಸುತ್ತದೆ!)"
        )
    },
    {
        "id": "rose_q2",
        "challenge": (
            "Show what colour change happens when a BASE is added to red rose petal extract. "
            "Demonstrate the dramatic colour response that identifies a base.\n\n"
            "(ಕ್ಷಾರ ಸೇರಿಸಿದಾಗ ಗುಲಾಬಿ ಸಾರ ಯಾವ ಬಣ್ಣಕ್ಕೆ ಬದಲಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' — soap turns rose extract from pink to GREEN.",
            "attempt_2": "Set 'initialState' to 'basic'. OH⁻ ions from bases cause the striking green colour.",
            "attempt_3": "Choose 'basic': soap turns rose extract GREEN — confirming it is a base."
        },
        "concept_reminder": (
            "Bases turn rose extract GREEN — the most distinctive change. "
            "OH⁻ ions shift anthocyanin to green form. Soap, baking soda, lime water all go green. "
            "(ಕ್ಷಾರ ಗುಲಾಬಿ ಸಾರವನ್ನು ಹಸಿರಾಗಿಸುತ್ತದೆ!)"
        )
    },
    {
        "id": "rose_q3",
        "challenge": (
            "Show what happens with a NEUTRAL substance and explain why rose extract is a "
            "COMPLETE indicator (unlike turmeric, which is only partial).\n\n"
            "(ತಟಸ್ಥ ದ್ರಾವಣದೊಂದಿಗೆ ಏನಾಗುತ್ತದೆ, ಮತ್ತು ಗುಲಾಬಿ ಸಾರ ಪೂರ್ಣ ಸೂಚಕ ಯಾಕೆ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "neutral"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'neutral' — tap water leaves rose extract PINK; neutral substances cause no change.",
            "attempt_2": "Set 'initialState' to 'neutral'. Rose stays pink — three distinct colours, one per type = complete indicator.",
            "attempt_3": "Choose 'neutral': tap water keeps rose extract pink, confirming neutrals don't react with anthocyanins."
        },
        "concept_reminder": (
            "Neutral substances leave rose extract PINK (unchanged). "
            "RED=acid, GREEN=base, PINK=neutral — three distinct results makes it a COMPLETE indicator. "
            "Compare: turmeric stays yellow for BOTH acids and neutrals (partial). "
            "(ಗುಲಾಬಿ ಸಾರ ಪೂರ್ಣ ಸೂಚಕ: ಕೆಂಪು=ಆಮ್ಲ, ಹಸಿರು=ಕ್ಷಾರ, ಗುಲಾಬಿ=ತಟಸ್ಥ!)"
        )
    }
]


# =============================================================================
# PROPERTIES OF ACIDS AND BASES SIMULATION
# ಆಮ್ಲಗಳು ಮತ್ತು ಕ್ಷಾರಗಳ ಗುಣಗಳು – ಹೋಲಿಕೆ ಮಾಡಿ ಕಲಿಯಿರಿ
# Science Chapter 2 – Properties comparison with misconception correction
# =============================================================================
SIMULATIONS_KN["properties_acids_bases_kn"] = {
    "title": "ಆಮ್ಲ ಮತ್ತು ಕ್ಷಾರ ಗುಣಗಳು (Properties of Acids & Bases)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation3_properties_acids_bases_kn.html",
    "description": (
        "Kannada tab-based simulation comparing properties of acids vs bases. "
        "Two interactive panels show: acids (sour taste, blue litmus → red, corrosive) "
        "and bases (bitter/slippery, red litmus → blue). A substance quiz lets students "
        "classify common items. Key misconception: bitter taste ≠ necessarily a base "
        "(demonstrated via bitter gourd which is NOT a base)."
    ),
    "cannot_demonstrate": [
        "Quantitative pH values",
        "Chemical equations for reactions",
        "Neutralisation between acids and bases"
    ],
    "initial_params": {"initialState": "initial", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Panel to Show",
            "range": "initial, acids, bases",
            "url_key": "initialState",
            "effect": (
                "Controls which tab panel is active on load.\n"
                "  'initial' → loads with acids tab showing (default)\n"
                "  'acids'   → clicks the Acids tab showing acid properties\n"
                "  'bases'   → clicks the Bases tab showing base properties"
            )
        },
        "showHints": {
            "label": "Show Concept Card",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the concept summary card at the top."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Properties of Acids",
            "description": (
                "Acids: sour taste, turn blue litmus red, can corrode metals. "
                "Examples: citric acid (lemon), acetic acid (vinegar), lactic acid (curd)."
            ),
            "key_insight": (
                "Key acid properties: (1) Sour taste. (2) Blue litmus → RED. (3) Corrosive. "
                "Acids release H⁺ ions in solution."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Properties of Bases",
            "description": (
                "Bases: bitter taste, soapy/slippery touch, turn red litmus blue. "
                "Examples: baking soda, soap, lime water, antacids."
            ),
            "key_insight": (
                "Key base properties: (1) Bitter taste. (2) Slippery/soapy touch — reacts with "
                "skin oils. (3) Red litmus → BLUE. Bases release OH⁻ ions in solution."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Misconception: Bitter Taste Does Not Always Mean Basic",
            "description": (
                "Bitter gourd tastes bitter but is NOT a base. "
                "Bitterness is a property of bases but not all bitter things are bases."
            ),
            "key_insight": (
                "Always use litmus or an indicator to confirm whether something is a base. "
                "Bitter gourd's bitterness comes from glucoside compounds, not from being alkaline. "
                "Test with litmus, not just taste."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["properties_acids_bases_kn"] = [
    {
        "id": "props_q1",
        "challenge": (
            "Navigate the simulation to show the PROPERTIES OF ACIDS panel. "
            "Explore the key characteristics that define acids.\n\n"
            "(ಆಮ್ಲಗಳ ಗುಣಗಳ ಪ್ಯಾನಲ್ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acids"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acids' as the Simulation State to activate the Acids panel — sour taste, blue litmus → red, and corrosive.",
            "attempt_2": "Set 'initialState' to 'acids'. The simulation clicks the acids tab and shows all three key acid properties.",
            "attempt_3": "Choose 'acids': the acids panel shows sour taste, litmus effect, and common examples."
        },
        "concept_reminder": (
            "Acids: (1) SOUR taste. (2) Blue litmus → RED. (3) Corrosive. "
            "Examples: citric acid (lemon), acetic acid (vinegar), lactic acid (curd). "
            "(ಆಮ್ಲ: ಹುಳಿ ರುಚಿ, ನೀಲಿ ಲಿಟ್ಮಸ್ → ಕೆಂಪು!)"
        )
    },
    {
        "id": "props_q2",
        "challenge": (
            "Show the PROPERTIES OF BASES panel. "
            "Explore how bases differ from acids in their characteristics.\n\n"
            "(ಕ್ಷಾರಗಳ ಗುಣಗಳ ಪ್ಯಾನಲ್ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "bases"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'bases' — the Bases panel shows bitter taste, slippery touch, and red litmus → blue.",
            "attempt_2": "Set 'initialState' to 'bases'. The bases tab shows all three key properties of bases.",
            "attempt_3": "Choose 'bases': bitter taste, soapy touch, and red litmus turning blue."
        },
        "concept_reminder": (
            "Bases: (1) BITTER taste. (2) SLIPPERY/SOAPY touch — reacts with skin oils. "
            "(3) Red litmus → BLUE. Examples: baking soda, soap, lime water. "
            "(ಕ್ಷಾರ: ಕಹಿ ರುಚಿ, ಜಾರುವ ಸ್ಪರ್ಶ, ಕೆಂಪು ಲಿಟ್ಮಸ್ → ನೀಲಿ!)"
        )
    },
    {
        "id": "props_q3",
        "challenge": (
            "Return to the INITIAL view. Reflect: what is the key litmus difference "
            "between acids and bases?\n\n"
            "(ಪ್ರಾರಂಭ ಸ್ಥಿತಿಗೆ ಹಿಂದಿರಿ ಮತ್ತು ಆಮ್ಲ-ಕ್ಷಾರ ಲಿಟ್ಮಸ್ ವ್ಯತ್ಯಾಸ ವಿವರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "initial"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'initial' to see the default acids tab view. Then reflect on both panels.",
            "attempt_2": "Set 'initialState' to 'initial'. The acids panel loads as the starting reference point.",
            "attempt_3": "Choose 'initial' to reset to the starting view where both tabs are available to compare."
        },
        "concept_reminder": (
            "Acids: Blue litmus → RED. Bases: Red litmus → BLUE. Neutrals: NEITHER changes. "
            "Also: bitter taste ≠ base (e.g. bitter gourd is NOT a base — test with litmus!). "
            "(ಆಮ್ಲ ↔ ಕ್ಷಾರ: ಎದುರು ಲಿಟ್ಮಸ್ ಕ್ರಿಯೆಗಳು!)"
        )
    }
]


# =============================================================================
# LITMUS INDICATOR SIMULATION
# ಲಿಟ್ಮಸ್ ಪೇಪರ್ ಪರೀಕ್ಷೆ – ಶಾಸ್ತ್ರೀಯ ಆಮ್ಲ-ಕ್ಷಾರ ಸೂಚಕ
# Science Chapter 2 – Litmus as the standard complete indicator
# =============================================================================
SIMULATIONS_KN["litmus_indicator_kn"] = {
    "title": "ಲಿಟ್ಮಸ್ ಕಾಗದ ಪರೀಕ್ಷೆ (Litmus Paper Test)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation2_litmus_indicator_kn.html",
    "description": (
        "Kannada simulation of the classic litmus paper test. Blue and red litmus papers "
        "are dipped simultaneously into a chosen solution. Students observe: acid = blue → red, "
        "base = red → blue, neutral = neither changes. Tests 9 common solutions. "
        "Litmus is a COMPLETE indicator derived from lichen."
    ),
    "cannot_demonstrate": [
        "Quantitative pH values",
        "Other indicator types (phenolphthalein, universal indicator)",
        "Concentration effects on colour intensity"
    ],
    "initial_params": {"initialState": "acidic", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Solution Type",
            "range": "acidic, basic, neutral",
            "url_key": "initialState",
            "effect": (
                "Selects a solution and auto-runs the litmus dip animation.\n"
                "  'acidic'  → lemon juice: blue paper turns RED, red unchanged\n"
                "  'basic'   → soap: red paper turns BLUE, blue unchanged\n"
                "  'neutral' → tap water: NEITHER paper changes colour"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the insight box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Acids Turn Blue Litmus Red",
            "description": (
                "Blue litmus paper turns red in acidic solutions. "
                "H⁺ ions released by acids cause this colour change. "
                "Red litmus stays red in acids."
            ),
            "key_insight": (
                "Blue → RED in acids. This is the classic acid test. "
                "Lemon juice, vinegar, curd all turn blue litmus red."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Bases Turn Red Litmus Blue",
            "description": (
                "Red litmus paper turns blue in basic (alkaline) solutions. "
                "OH⁻ ions cause this colour change. Blue litmus stays blue in bases."
            ),
            "key_insight": (
                "Red → BLUE in bases. This is the classic base test. "
                "Soap, baking soda, lime water all turn red litmus blue."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Neutral Substances: No Change in Either Litmus",
            "description": (
                "Neither litmus paper changes in neutral solutions. "
                "Absence of change is itself a result."
            ),
            "key_insight": (
                "Neutral → NO change in either litmus. pH 7 means equal H⁺ and OH⁻. "
                "Three distinct outcomes make litmus a COMPLETE indicator."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["litmus_indicator_kn"] = [
    {
        "id": "litmus_q1",
        "challenge": (
            "Show the litmus paper test result for an ACID. Demonstrate what happens to "
            "both blue and red litmus papers in an acidic solution.\n\n"
            "(ಆಮ್ಲ ದ್ರಾವಣದಲ್ಲಿ ಲಿಟ್ಮಸ್ ಕಾಗದ ಮುಳುಗಿಸಿದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' — lemon juice used. Blue litmus turns red, red litmus stays unchanged.",
            "attempt_2": "Set 'initialState' to 'acidic'. Classic result: blue → RED confirms acid.",
            "attempt_3": "Choose 'acidic': lemon juice gives the acid result — BLUE turns RED."
        },
        "concept_reminder": (
            "Acids turn BLUE litmus RED. Red litmus stays unchanged. "
            "H⁺ ions from acids cause blue litmus to change to red. "
            "(ಆಮ್ಲ: ನೀಲಿ ಲಿಟ್ಮಸ್ → ಕೆಂಪು!)"
        )
    },
    {
        "id": "litmus_q2",
        "challenge": (
            "Show the litmus paper test result for a BASE. Demonstrate what both "
            "litmus papers do in an alkaline solution.\n\n"
            "(ಕ್ಷಾರ ದ್ರಾವಣದಲ್ಲಿ ಲಿಟ್ಮಸ್ ಕಾಗದ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' — soap used. Red litmus turns BLUE, blue litmus stays unchanged.",
            "attempt_2": "Set 'initialState' to 'basic'. Base result: red → BLUE confirms base.",
            "attempt_3": "Choose 'basic': soap gives the base result — RED turns BLUE."
        },
        "concept_reminder": (
            "Bases turn RED litmus BLUE. Blue litmus stays unchanged. "
            "OH⁻ ions from bases cause red litmus to turn blue. "
            "(ಕ್ಷಾರ: ಕೆಂಪು ಲಿಟ್ಮಸ್ → ನೀಲಿ!)"
        )
    },
    {
        "id": "litmus_q3",
        "challenge": (
            "Show the litmus result for a NEUTRAL substance and explain how this makes "
            "litmus a COMPLETE indicator.\n\n"
            "(ತಟಸ್ಥ ದ್ರಾವಣದಲ್ಲಿ ಲಿಟ್ಮಸ್ ಕಾಗದ ಏನಾಗುತ್ತದೆ — ಲಿಟ್ಮಸ್ ಪೂರ್ಣ ಸೂಚಕ ಯಾಕೆ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "neutral"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'neutral' — tap water used. NEITHER paper changes. Both stay their original colour.",
            "attempt_2": "Set 'initialState' to 'neutral'. No colour change confirms neutrality.",
            "attempt_3": "Choose 'neutral': tap water gives no change in either paper — neutral result."
        },
        "concept_reminder": (
            "Neutral → NEITHER litmus changes. Blue stays blue, red stays red. "
            "Three outcomes: Blue→Red=acid, Red→Blue=base, No change=neutral. "
            "This makes litmus a COMPLETE indicator. pH 7 = neutral. "
            "(ತಟಸ್ಥ: ಯಾವ ಲಿಟ್ಮಸ್ ಕಾಗದವೂ ಬಣ್ಣ ಬದಲಾಯಿಸಲ್ಲ!)"
        )
    }
]


# =============================================================================
# HIDDEN MESSAGE SIMULATION
# ಗುಪ್ತ ಸಂದೇಶ ಬಹಿರಂಗ – ಆಮ್ಲ-ಕ್ಷಾರ ಸೂಚಕ ಪರಿಚಯ
# Science Chapter 2 – Chapter-opening indicator demonstration
# =============================================================================
SIMULATIONS_KN["hidden_message_kn"] = {
    "title": "ಗುಪ್ತ ಸಂದೇಶ ಬಹಿರಂಗ (Hidden Message Reveal)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation1_hidden_message_kn.html",
    "description": (
        "Kannada chapter-opening simulation: a message written with invisible alkaline "
        "ink (base) is revealed by spraying an indicator (phenolphthalein) 3 times. "
        "Characters Ashwin and Kirti observe the science fair demonstration. "
        "Creates curiosity about why indicators change colour with acids and bases."
    ),
    "cannot_demonstrate": [
        "Specific chemistry of phenolphthalein",
        "What happens with acidic invisible ink",
        "Quantitative colour change data"
    ],
    "initial_params": {"initialState": "hidden", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Reveal State",
            "range": "hidden, revealing, revealed",
            "url_key": "initialState",
            "effect": (
                "Controls how many indicator sprays are applied on page load.\n"
                "  'hidden'    → blank paper, 0 sprays (default)\n"
                "  'revealing' → 1 spray — message partially visible (33%)\n"
                "  'revealed'  → 3 sprays — message fully visible (100%)"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the insight explanation box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Indicators Change Colour in the Presence of Acids or Bases",
            "description": (
                "An indicator is a substance that changes colour when it contacts an acid or base. "
                "The spray in this simulation reacts with the base ink to produce colour."
            ),
            "key_insight": (
                "Indicators are our tools for detecting acids and bases. "
                "The colour change is a chemical reaction, not just physical mixing. "
                "Different indicators respond to acids, bases, or both."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "Invisible Ink: Base + Indicator = Visible Message",
            "description": (
                "The message was written with a BASE solution (e.g. baking soda water) "
                "which dries clear. Spraying an indicator reveals it through colour change."
            ),
            "key_insight": (
                "Base (invisible) + Indicator → colour change (visible). "
                "This is acid-base chemistry applied to: science demos, invisible ink, "
                "surface testing for base residues."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "Real-World: Invisible Ink Uses Acid-Base Chemistry",
            "description": (
                "Historically, lemon juice (acid ink) or baking soda (base ink) "
                "were used as invisible inks, revealed by the appropriate indicator."
            ),
            "key_insight": (
                "Lemon juice ink: revealed by alkaline indicator or heat. "
                "Baking soda ink: revealed by acidic indicator (like red cabbage juice). "
                "Acid-base chemistry has practical real-world applications beyond the lab."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["hidden_message_kn"] = [
    {
        "id": "hidden_q1",
        "challenge": (
            "Show the INITIAL state of the paper — before any indicator is sprayed. "
            "This represents the completely invisible hidden message.\n\n"
            "(ಸೂಚಕ ಸಿಂಪಡಿಸುವ ಮೊದಲು ಕಾಗದ ಹೇಗಿರುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "hidden"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'hidden' — the paper appears blank; the base ink is invisible before any indicator reaction.",
            "attempt_2": "Set 'initialState' to 'hidden'. No indicator applied yet, so no colour change, no visible message.",
            "attempt_3": "Choose 'hidden': blank paper state showing how base ink is truly invisible when dry."
        },
        "concept_reminder": (
            "The message is written with BASE solution. When dry, base is colourless and invisible. "
            "No indicator applied = no colour change = invisible message. "
            "Dilute bases are often colourless in solution. "
            "(ಗುಪ್ತ ಸಂದೇಶ: ಕ್ಷಾರ ಒಣಗಿದಾಗ ಅದೃಶ್ಯ!)"
        )
    },
    {
        "id": "hidden_q2",
        "challenge": (
            "Show the COMPLETELY REVEALED state — after full indicator treatment. "
            "Demonstrate how the indicator reacts with the base to make the message fully visible.\n\n"
            "(ಸೂಚಕ ಸಿಂಪಡಿಸಿದ ನಂತರ ಸಂದೇಶ ಸಂಪೂರ್ಣ ಬಹಿರಂಗ ಆಗುವುದನ್ನು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "revealed"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'revealed' — all 3 sprays applied automatically and 'ವಿಜ್ಞಾನ ಮೇಳ!' becomes fully visible.",
            "attempt_2": "Set 'initialState' to 'revealed'. Complete reveal shows indicator reacting fully with all base molecules.",
            "attempt_3": "Choose 'revealed': 3 sprays show the full message — indicator + base = colour change."
        },
        "concept_reminder": (
            "3 indicator sprays reveal the full message. "
            "Indicator + Base → coloured compound exactly where base was applied. "
            "This is COLOUR CHANGE REACTION: Indicator + Base → visible coloured product. "
            "(ಸೂಚಕ + ಕ್ಷಾರ → ಬಣ್ಣ ಬದಲಾವಣೆ → ಗುಪ್ತ ಸಂದೇಶ ಬಹಿರಂಗ!)"
        )
    },
    {
        "id": "hidden_q3",
        "challenge": (
            "Show the PARTIALLY REVEALED state — after just one spray. "
            "Demonstrate how the colour change builds gradually.\n\n"
            "(ಒಂದು ಸಿಂಪಡಿಕೆಯ ನಂತರ ಸಂದೇಶ ಭಾಗಶಃ ಕಾಣಿಸುವ ಸ್ಥಿತಿ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "revealing"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'revealing' — one spray applied; message appears faintly showing partial colour change.",
            "attempt_2": "Set 'initialState' to 'revealing'. After 1 spray, partial visibility shows the reaction is gradual.",
            "attempt_3": "Choose 'revealing': one spray gives a faint glimpse — reaction in progress but not complete."
        },
        "concept_reminder": (
            "After one spray, the message is partially visible — faint but detectable. "
            "More indicator → more reaction → more colour → clearer message. "
            "The indicator must contact all base molecules in the ink for full visibility. "
            "(ಒಂದು ಸಿಂಪಡಿಕೆ: ಭಾಗಶಃ ಬಹಿರಂಗ — ಪ್ರತಿಕ್ರಿಯೆ ಮುಂದುವರಿಯುತ್ತಿದೆ!)"
        )
    }
]


# ═══════════════════════════════════════════════════════════════════════
# HELPER: list of Kannada simulation IDs for sidebar grouping
# ═══════════════════════════════════════════════════════════════════════

KN_SIMULATION_IDS = list(SIMULATIONS_KN.keys())
