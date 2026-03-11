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


# =============================================================================
# OLFACTORY INDICATOR SIMULATION (sim6)
# ಘ್ರಾಣ ಸೂಚಕ – ಈರುಳ್ಳಿ ವಾಸನೆಯಿಂದ ಆಮ್ಲ/ಕ್ಷಾರ ಗುರುತಿಸಿ
# =============================================================================
SIMULATIONS_KN["olfactory_indicator_kn"] = {
    "title": "ಘ್ರಾಣ ಸೂಚಕ (Olfactory Indicator)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation6_olfactory_indicator_kn.html",
    "description": (
        "Kannada simulation: students mix household solutions with cut onion and observe "
        "whether the pungent smell remains (acid) or disappears (base). Onion's sulfur "
        "compounds are neutralised by bases but not by acids — making onion a natural "
        "olfactory indicator."
    ),
    "cannot_demonstrate": [
        "Neutral substance — neither preserves nor eliminates smell distinctly",
        "Quantitative measurement of smell intensity"
    ],
    "initial_params": {"initialState": "basic", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Solution Type",
            "range": "acidic, basic",
            "url_key": "initialState",
            "effect": (
                "Selects a solution and auto-runs the mixing test.\n"
                "  'acidic' → tamarind water — smell stays strong (acid confirmed)\n"
                "  'basic'  → baking soda — smell disappears (base confirmed)"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the key insight box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "ಘ್ರಾಣ ಸೂಚಕ: ಆಮ್ಲ ವಾಸನೆ ಉಳಿಸುತ್ತದೆ (Acids Preserve Onion Smell)",
            "description": (
                "Acids do NOT react with onion's sulfur compounds. When an acid solution "
                "is mixed with cut onion the pungent smell remains unchanged."
            ),
            "key_insight": (
                "Acid + Onion → Strong smell persists. Lemon, vinegar, tamarind — "
                "all leave onion smell intact. This is how onion detects an acid."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "ಘ್ರಾಣ ಸೂಚಕ: ಕ್ಷಾರ ವಾಸನೆ ನಾಶ ಮಾಡುತ್ತದೆ (Bases Destroy Onion Smell)",
            "description": (
                "Bases neutralise onion's allyl sulfide compounds. When a base is mixed "
                "with cut onion the smell disappears within seconds."
            ),
            "key_insight": (
                "Base + Onion → Smell vanishes. Baking soda, soap — all eliminate the "
                "pungent odour via neutralisation. Confirmed base!"
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "ಪ್ರತ್ಯಕ್ಷ ಉದಾಹರಣೆ: ಬೇಕಿಂಗ್ ಸೋಡಾದೊಂದಿಗೆ ಈರುಳ್ಳಿ ಬೇಯಿಸುವುದು",
            "description": (
                "Cooking onion with baking soda (alkaline) reduces its pungency. "
                "The same neutralisation reaction seen in the simulation occurs in the kitchen."
            ),
            "key_insight": (
                "Real-world chemistry: alkaline baking soda neutralises onion sulfur compounds "
                "reducing sharpness. Acid-base indicators exist beyond the lab — they are in "
                "your kitchen too!"
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["olfactory_indicator_kn"] = [
    {
        "id": "olfactory_q1",
        "challenge": (
            "Show what happens when an ACID is mixed with cut onion using the olfactory "
            "indicator simulation. Does the smell remain or disappear?\n\n"
            "(ಆಮ್ಲ ಈರುಳ್ಳಿಯೊಂದಿಗೆ ಮಿಶ್ರಣ ಮಾಡಿದಾಗ ವಾಸನೆ ಉಳಿಯುತ್ತದೆಯೇ ಅಥವಾ ಅದೃಶ್ಯವಾಗುತ್ತದೆಯೇ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' as the Simulation State — tamarind water mixed with onion. Watch whether the smell icon keeps showing.",
            "attempt_2": "Set 'initialState' to 'acidic'. Acids do NOT neutralise sulfur compounds so the smell stays strong.",
            "attempt_3": "Choose 'acidic': acid + onion → smell remains. This is how we know it is an acid!"
        },
        "concept_reminder": (
            "Acids preserve onion smell. Tamarind, vinegar, lemon juice — none react "
            "with sulfur compounds. Smell stays = acid. "
            "(ಆಮ್ಲ + ಈರುಳ್ಳಿ → ವಾಸನೆ ಉಳಿಯುತ್ತದೆ!)"
        )
    },
    {
        "id": "olfactory_q2",
        "challenge": (
            "Show what happens when a BASE is mixed with cut onion. Demonstrate why "
            "onion is called an olfactory indicator.\n\n"
            "(ಕ್ಷಾರ ಈರುಳ್ಳಿಯೊಂದಿಗೆ ಮಿಶ್ರಣ ಮಾಡಿದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' — baking soda mixed with onion. The pungent smell disappears completely.",
            "attempt_2": "Set 'initialState' to 'basic'. Bases neutralise sulfur compounds → smell vanishes.",
            "attempt_3": "Choose 'basic': base + onion → smell disappears. A base is confirmed!"
        },
        "concept_reminder": (
            "Bases destroy onion smell via neutralisation. Baking soda, soap — "
            "all eliminate the pungent odour. No smell = base. "
            "(ಕ್ಷಾರ + ಈರುಳ್ಳಿ → ವಾಸನೆ ಅದೃಶ್ಯ!)"
        )
    },
    {
        "id": "olfactory_q3",
        "challenge": (
            "Show the acid test again and explain: why is onion called a PARTIAL olfactory "
            "indicator (not a complete one)?\n\n"
            "(ಘ್ರಾಣ ಸೂಚಕ ಭಾಗಶಃ ಯಾಕೆ — ಪೂರ್ಣ ಸೂಚಕ ಅಲ್ಲ ಯಾಕೆ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' — observe that smell stays strong. Onion can identify acids (smell stays) and bases (smell goes), but NOT neutral substances.",
            "attempt_2": "Set 'initialState' to 'acidic'. Since onion stays smelly with acid AND neutral substances, it cannot distinguish between them.",
            "attempt_3": "Choose 'acidic': smell stays with acid. But neutral water also keeps the smell — so onion is partial, not complete."
        },
        "concept_reminder": (
            "Onion is a PARTIAL olfactory indicator: identifies bases (smell gone) but "
            "cannot distinguish acid from neutral (both keep the smell). "
            "Compare: litmus is complete — gives 3 distinct results. "
            "(ಘ್ರಾಣ ಸೂಚಕ: ಕ್ಷಾರ ಮಾತ್ರ ಖಚಿತಪಡಿಸಬಲ್ಲದು!)"
        )
    }
]


# =============================================================================
# NEUTRALISATION REACTION SIMULATION (sim7)
# ತಟಸ್ಥೀಕರಣ ಪ್ರತಿಕ್ರಿಯೆ – ಆಮ್ಲ + ಕ್ಷಾರ = ಉಪ್ಪು + ನೀರು
# =============================================================================
SIMULATIONS_KN["neutralisation_reaction_kn"] = {
    "title": "ತಟಸ್ಥೀಕರಣ ಪ್ರತಿಕ್ರಿಯೆ (Neutralisation Reaction)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation7_neutralisation_reaction_kn.html",
    "description": (
        "Kannada slider simulation: students adjust the acid-base ratio and observe "
        "the resulting pH. At equal proportions (slider ~50%) full neutralisation "
        "produces salt + water + heat at pH 7. Too much acid → acidic product; "
        "too much base → basic product. pH pointer, product indicators, and color-coded "
        "beakers make the stoichiometry visual."
    ),
    "cannot_demonstrate": [
        "Specific chemical equations (e.g. HCl + NaOH)",
        "Heat measurement in joules",
        "Effect of concentration on reaction rate"
    ],
    "initial_params": {"initialState": "neutral", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Reaction Outcome",
            "range": "acidic, neutral, basic",
            "url_key": "initialState",
            "effect": (
                "Sets the slider position and auto-runs the mixing reaction.\n"
                "  'acidic'  → slider at 20% (excess acid) — acidic product, pH ~3\n"
                "  'neutral' → slider at 50% (equal parts) — neutral, pH 7\n"
                "  'basic'   → slider at 80% (excess base) — basic product, pH ~11"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the key insight box."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "ತಟಸ್ಥೀಕರಣ: ಆಮ್ಲ + ಕ್ಷಾರ → ಉಪ್ಪು + ನೀರು + ಶಾಖ",
            "description": (
                "When acid and base react in equal amounts they completely neutralise "
                "each other producing salt, water AND heat (exothermic reaction). "
                "The result is pH 7 — neutral."
            ),
            "key_insight": (
                "Equal acid + base = complete neutralisation → salt + water + heat. "
                "pH goes from acidic/basic extremes to exactly 7. "
                "Real example: antacid (base) neutralises excess stomach acid (HCl)."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "ಅಸಮ ಅನುಪಾತ: ಹೆಚ್ಚು ಆಮ್ಲ ಅಥವಾ ಕ್ಷಾರ",
            "description": (
                "When acid is in excess the product is still acidic (pH < 7). "
                "When base is in excess the product is still basic (pH > 7). "
                "Only exact equal amounts give pH 7."
            ),
            "key_insight": (
                "Ratio matters! Excess acid → acidic product. Excess base → basic product. "
                "Perfect neutralisation requires stoichiometric equivalence."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "ವಾಸ್ತವ ಬಳಕೆ: ಆಮ್ಲನಿರೋಧಕಗಳು (Real-world: Antacids)",
            "description": (
                "Antacid tablets contain base (Mg(OH)₂) that neutralises excess stomach "
                "acid (HCl) using the same acid-base neutralisation chemistry demonstrated here."
            ),
            "key_insight": (
                "Stomach acid (HCl) + Antacid base → salt + water → relief. "
                "The same neutralisation equation applies: acid + base → salt + water. "
                "This is neutralisation chemistry in daily life."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["neutralisation_reaction_kn"] = [
    {
        "id": "neutralisation_q1",
        "challenge": (
            "Show the COMPLETE neutralisation scenario — the ideal case where acid and "
            "base fully cancel each other producing salt, water, and a neutral pH.\n\n"
            "(ಸಂಪೂರ್ಣ ತಟಸ್ಥೀಕರಣ ತೋರಿಸಿ — pH 7 ಆಗುವ ಅದರ್ಶ ಸ್ಥಿತಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "neutral"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'neutral' — slider goes to 50%, equal acid and base mix, pH pointer reaches exactly 7.",
            "attempt_2": "Set 'initialState' to 'neutral'. Equal proportions → complete neutralisation → salt + water + heat at pH 7.",
            "attempt_3": "Choose 'neutral': 50% base + 50% acid → perfect neutral result, all three products appear."
        },
        "concept_reminder": (
            "Complete neutralisation: Acid + Base (equal parts) → Salt + Water + Heat, pH = 7. "
            "The salt and water products light up. This is the ideal outcome. "
            "(ಸಮ ಭಾಗ ಆಮ್ಲ + ಕ್ಷಾರ → pH 7, ಸಂಪೂರ್ಣ ತಟಸ್ಥೀಕರಣ!)"
        )
    },
    {
        "id": "neutralisation_q2",
        "challenge": (
            "Show what happens when there is EXCESS ACID in the mixture — "
            "demonstrate that incomplete neutralisation still leaves an acidic product.\n\n"
            "(ಆಮ್ಲ ಹೆಚ್ಚಾದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' — slider moves to 20%, excess acid remains after base is exhausted, product pH ~3.",
            "attempt_2": "Set 'initialState' to 'acidic'. Not enough base to neutralise all acid → still acidic product.",
            "attempt_3": "Choose 'acidic': slider at 20% means very little base, lots of acid leftover. Result beaker stays orangey-red."
        },
        "concept_reminder": (
            "Excess acid → product is still acidic (pH < 7). Not enough base to neutralise everything. "
            "The remaining H⁺ ions keep the solution acidic. "
            "(ಆಮ್ಲ ಹೆಚ್ಚಾದರೆ ಫಲಿತಾಂಶ ಇನ್ನೂ ಆಮ್ಲೀಯ!)"
        )
    },
    {
        "id": "neutralisation_q3",
        "challenge": (
            "Show what happens when there is EXCESS BASE — demonstrate that too much "
            "base also prevents complete neutralisation.\n\n"
            "(ಕ್ಷಾರ ಹೆಚ್ಚಾದಾಗ ಏನಾಗುತ್ತದೆ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' — slider moves to 80%, excess base remains, product pH ~11.",
            "attempt_2": "Set 'initialState' to 'basic'. Too much base means leftover OH⁻ ions → basic product.",
            "attempt_3": "Choose 'basic': 80% base means excess alkali. Result beaker turns blue and pH > 9."
        },
        "concept_reminder": (
            "Excess base → product is still basic (pH > 7). Leftover OH⁻ ions keep it alkaline. "
            "Perfect neutralisation needs EXACT stoichiometric ratio. "
            "(ಕ್ಷಾರ ಹೆಚ್ಚಾದರೆ ಫಲಿತಾಂಶ ಇನ್ನೂ ಕ್ಷಾರೀಯ!)"
        )
    }
]


# =============================================================================
# ANT BITE TREATMENT SIMULATION (sim8)
# ಇರುವೆ ಕಚ್ಚುವಿಕೆ ಚಿಕಿತ್ಸೆ – ದೈನಂದಿನ ಜೀವನದಲ್ಲಿ ತಟಸ್ಥೀಕರಣ
# =============================================================================
SIMULATIONS_KN["ant_bite_treatment_kn"] = {
    "title": "ಇರುವೆ ಕಚ್ಚುವಿಕೆ ಚಿಕಿತ್ಸೆ (Ant Bite Treatment)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation8_ant_bite_treatment_kn.html",
    "description": (
        "Kannada sequential simulation: students observe an ant bite inject formic acid "
        "(HCOOH) into the skin, causing redness and pain. Applying baking soda (base) "
        "neutralises the acid, eliminating pain and healing the skin. A real-world "
        "demonstration of neutralisation as first aid."
    ),
    "cannot_demonstrate": [
        "Chemical equation with actual molecular symbols in interactive form",
        "Other ant-bite remedies beyond baking soda",
        "Difference between red-ant and black-ant venom"
    ],
    "initial_params": {"initialState": "normal", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Scenario State",
            "range": "normal, bitten, treated",
            "url_key": "initialState",
            "effect": (
                "Controls the sequential treatment scenario auto-played on load.\n"
                "  'normal'  → healthy skin, no bite (default)\n"
                "  'bitten'  → ant bites, formic acid injected, skin turns red (1 click)\n"
                "  'treated' → baking soda applied, neutralisation, pain relief (2 clicks)"
            )
        },
        "showHints": {
            "label": "Show Hints",
            "range": "true/false",
            "url_key": "showHints",
            "effect": "Shows or hides the insight and science explanation boxes."
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "ಇರುವೆ ಚುಚ್ಚುವ ಆಮ್ಲ: ಫಾರ್ಮಿಕ್ ಆಮ್ಲ (HCOOH)",
            "description": (
                "Ant venom contains formic acid (HCOOH). When an ant bites, it injects "
                "this acid into the skin, causing a burning sensation, redness, "
                "and localised pain."
            ),
            "key_insight": (
                "Formic acid (HCOOH) = ant venom. Acidic substance causes inflammation. "
                "To relieve pain we need to NEUTRALISE the acid — apply a base."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "ಚಿಕಿತ್ಸೆ: ಬೇಕಿಂಗ್ ಸೋಡಾ ತಟಸ್ಥೀಕರಣ (Baking Soda Neutralises the Acid)",
            "description": (
                "Baking soda (NaHCO₃) is a base. Applied to the ant bite it reacts with "
                "formic acid and neutralises it: Formic acid + Baking soda → Salt + Water. "
                "Pain and inflammation disappear."
            ),
            "key_insight": (
                "Baking soda (base) + Formic acid → salt + water + relief. "
                "The same neutralisation formula applies: acid + base → harmless products. "
                "This is the chemistry behind a simple first aid remedy."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "ವಾಸ್ತವ ಅನ್ವಯ: ಚರ್ಮ pH ಮರಳಿ ತಟಸ್ಥ",
            "description": (
                "After treatment the skin's pH returns to normal (~7). "
                "The neutralisation converts the acidic sting into harmless salt and water, "
                "stopping the chemical damage to skin cells."
            ),
            "key_insight": (
                "Neutralisation has real medical uses. Bee stings (also acid) → baking soda. "
                "Wasp stings (alkaline) → vinegar (acid). Match the treatment to the venom type. "
                "Acid venom → base treatment; alkaline venom → acid treatment."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["ant_bite_treatment_kn"] = [
    {
        "id": "antbite_q1",
        "challenge": (
            "Show just the ANT BITE — the moment formic acid is injected into the skin "
            "causing pain and redness. Do NOT apply treatment yet.\n\n"
            "(ಇರುವೆ ಕಚ್ಚುವ ಕ್ಷಣ ತೋರಿಸಿ — ಚಿಕಿತ್ಸೆ ಇಲ್ಲದೆ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "bitten"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'bitten' — the simulation auto-clicks the bite button showing formic acid injection and redness.",
            "attempt_2": "Set 'initialState' to 'bitten'. The skin turns red, pain shows HIGH, pH drops to ~4 (acidic).",
            "attempt_3": "Choose 'bitten': just the bite, no treatment. This shows formic acid (HCOOH) causing the problem."
        },
        "concept_reminder": (
            "Ant venom = formic acid (HCOOH). Injection makes skin acidic (~pH 4). "
            "Pain, redness, burning = acid damage to skin cells. Treatment needed! "
            "(ಇರುವೆ ಕಚ್ಚಿದಾಗ ಫಾರ್ಮಿಕ್ ಆಮ್ಲ ಚುಚ್ಚುತ್ತದೆ — ನೋವು ಮತ್ತು ಕೆಂಪು!)"
        )
    },
    {
        "id": "antbite_q2",
        "challenge": (
            "Show the COMPLETE treatment — bite followed by baking soda application. "
            "Demonstrate how neutralisation provides relief.\n\n"
            "(ಇರುವೆ ಕಚ್ಚಿದ ನಂತರ ಬೇಕಿಂಗ್ ಸೋಡಾ ಲೇಪಿಸಿ ತಟಸ್ಥೀಕರಣ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "treated"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'treated' — both buttons are auto-clicked: bite (800ms) then treatment (1800ms later). Shows full neutralisation.",
            "attempt_2": "Set 'initialState' to 'treated'. Redness disappears, pH returns to ~7, pain becomes 'ಇಲ್ಲ ✅'.",
            "attempt_3": "Choose 'treated': complete scenario — bite → baking soda → neutralisation → relief."
        },
        "concept_reminder": (
            "Baking soda (base) + Formic acid → salt + water. Skin pH returns to 7. "
            "Neutralisation reverses the damage — pain disappears. "
            "(ಬೇಕಿಂಗ್ ಸೋಡಾ ಫಾರ್ಮಿಕ್ ಆಮ್ಲ ತಟಸ್ಥೀಕರಿಸಿ ನೋವು ದೂರ ಮಾಡುತ್ತದೆ!)"
        )
    },
    {
        "id": "antbite_q3",
        "challenge": (
            "Show the HEALTHY initial state — before any bite. "
            "This is the baseline for comparing the effect of acid injection.\n\n"
            "(ಕಚ್ಚುವ ಮೊದಲು ಆರೋಗ್ಯಕರ ಚರ್ಮದ ಪ್ರಾರಂಭಿಕ ಸ್ಥಿತಿ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "normal"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'normal' — the default state with healthy skin and pH ~7 before any ant bite.",
            "attempt_2": "Set 'initialState' to 'normal'. This is the unaffected baseline — no acid, no pain, no treatment needed.",
            "attempt_3": "Choose 'normal': healthy skin, pH ~7. Compare this to 'bitten' (pH ~4) to see the acid's effect."
        },
        "concept_reminder": (
            "Normal skin pH is ~7 (neutral). After ant bite it drops to ~4 (acidic). "
            "After baking soda treatment it returns to ~7. "
            "This three-state comparison shows neutralisation in action. "
            "(ಸಾಮಾನ್ಯ ಚರ್ಮ pH 7 → ಕಚ್ಚಿದ ಮೇಲೆ pH 4 → ಚಿಕಿತ್ಸೆ ನಂತರ pH 7 ಮರಳಿ!)"
        )
    }
]


# =============================================================================
# SOIL TREATMENT SIMULATION (sim9)
# ಮಣ್ಣಿನ ಚಿಕಿತ್ಸೆ – ಕೃಷಿಯಲ್ಲಿ ತಟಸ್ಥೀಕರಣ
# =============================================================================
SIMULATIONS_KN["soil_treatment_kn"] = {
    "title": "ಮಣ್ಣಿನ ಚಿಕಿತ್ಸೆ (Soil Treatment — Agriculture)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter2_simulation9_soil_treatment_kn.html",
    "description": (
        "Kannada two-step soil simulation. Students select acidic soil (pH 4–5) or "
        "alkaline soil (pH 9–10), then apply the correct neutralising agent: lime (base) "
        "for acidic soil, compost (releases acids) for alkaline soil. The wilted plant "
        "recovers to show pH-7 healthy soil. Demonstrates agricultural neutralisation."
    ),
    "cannot_demonstrate": [
        "Quantitative lime dosage calculations",
        "Different types of lime or compost products",
        "Long-term soil pH management over seasons"
    ],
    "initial_params": {"initialState": "acidic", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Soil Scenario",
            "range": "acidic, basic, treated",
            "url_key": "initialState",
            "effect": (
                "Controls which soil problem is selected and whether treatment is applied.\n"
                "  'acidic'  → acidic soil selected (pH 4-5), plant wilted, lime shown\n"
                "  'basic'   → alkaline soil selected (pH 9-10), plant wilted, compost shown\n"
                "  'treated' → acidic soil selected then lime applied → pH returns to 7"
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
            "title": "ಆಮ್ಲೀಯ ಮಣ್ಣಿಗೆ ಚಿಕಿತ್ಸೆ: ಸುಣ್ಣ (ಕ್ಷಾರ) ಸೇರಿಸಿ",
            "description": (
                "When soil is too acidic (pH < 6) plants cannot absorb nutrients properly. "
                "Farmers add lime (calcium carbonate, a base) to neutralise excess soil acid "
                "and raise pH to the optimal neutral range."
            ),
            "key_insight": (
                "Acidic soil → add lime (base) → neutralisation → pH 7 → healthy plants. "
                "Soil acid + lime base → calcium salt + water. Same neutralisation equation."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "ಕ್ಷಾರೀಯ ಮಣ್ಣಿಗೆ ಚಿಕಿತ್ಸೆ: ಕಂಪೋಸ್ಟ್ (ಆಮ್ಲ ಬಿಡುಗಡೆ) ಸೇರಿಸಿ",
            "description": (
                "When soil is too alkaline (pH > 8) plants cannot absorb iron properly. "
                "Farmers add organic compost which releases acids as it decomposes, "
                "neutralising the excess alkali and bringing pH down to 7."
            ),
            "key_insight": (
                "Alkaline soil → add compost (acid-releasing) → neutralisation → pH 7. "
                "Compost acids + soil base → harmless salts + water. Same chemistry."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "pH 7: ಸಸ್ಯಗಳಿಗೆ ಆದರ್ಶ ಸ್ಥಿತಿ",
            "description": (
                "Plants grow best in neutral or near-neutral soil (pH 6.5–7.5). "
                "At this pH, all essential nutrients are maximally available and soluble. "
                "Too acidic or too alkaline blocks nutrient uptake mechanisms."
            ),
            "key_insight": (
                "Neutralisation → pH 7 → plant recovers from wilted to healthy. "
                "This is why farmers test soil pH and apply lime or compost every season. "
                "Chemistry knowledge directly improves agricultural yield."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["soil_treatment_kn"] = [
    {
        "id": "soil_q1",
        "challenge": (
            "Show the ACIDIC SOIL problem — select the acidic soil scenario to demonstrate "
            "why excess acid in soil prevents healthy plant growth.\n\n"
            "(ಆಮ್ಲೀಯ ಮಣ್ಣಿನ ಸಮಸ್ಯೆ ತೋರಿಸಿ — ಸಸ್ಯ ಯಾಕೆ ಮ್ಲಾನವಾಗುತ್ತದೆ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "acidic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'acidic' — the simulation shows acidic soil (pH 4-5), wilted plant, and lime bag highlighted as the solution.",
            "attempt_2": "Set 'initialState' to 'acidic'. Acidic soil blocks nutrient absorption — the plant cannot grow.",
            "attempt_3": "Choose 'acidic': see pH 4-5 soil, wilted plant emoji 🥀, and lime bag shown as the required treatment."
        },
        "concept_reminder": (
            "Acidic soil (pH 4-5) blocks nutrient absorption → plant wilts. "
            "Solution: add lime (base) to neutralise acid → pH reaches 7 → plant recovers. "
            "(ಆಮ್ಲೀಯ ಮಣ್ಣು: pH 4-5, ಸಸ್ಯ ಮ್ಲಾನ. ಸುಣ್ಣ ಹಾಕಿ ತಟಸ್ಥ ಮಾಡಿ!)"
        )
    },
    {
        "id": "soil_q2",
        "challenge": (
            "Show the ALKALINE SOIL problem — demonstrate the opposite case where "
            "excess base in soil also harms plant growth.\n\n"
            "(ಕ್ಷಾರೀಯ ಮಣ್ಣಿನ ಸಮಸ್ಯೆ ತೋರಿಸಿ — ಅಧಿಕ ಕ್ಷಾರ ಸಸ್ಯಕ್ಕೆ ಹಾಗೂ ಹಾನಿ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "basic"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'basic' — alkaline soil (pH 9-10), plant remains wilted, compost bag highlighted.",
            "attempt_2": "Set 'initialState' to 'basic'. Alkaline soil blocks iron absorption — add compost (acid-releasing) to neutralise.",
            "attempt_3": "Choose 'basic': pH 9-10, wilted 🥀 plant, compost shown as treatment. Both extremes harm plants!"
        },
        "concept_reminder": (
            "Alkaline soil (pH 9-10) blocks iron absorption → plant wilts. "
            "Solution: add compost (releases acids) to neutralise excess alkali → pH 7. "
            "Both acidic AND alkaline soil need treatment. "
            "(ಕ್ಷಾರೀಯ ಮಣ್ಣು: pH 9-10, ಸಸ್ಯ ಮ್ಲಾನ. ಕಂಪೋಸ್ಟ್ ಹಾಕಿ ತಟಸ್ಥ ಮಾಡಿ!)"
        )
    },
    {
        "id": "soil_q3",
        "challenge": (
            "Show the COMPLETE TREATMENT — acidic soil selected AND lime applied, "
            "demonstrating full agricultural neutralisation restoring healthy plant growth.\n\n"
            "(ಸಂಪೂರ್ಣ ಚಿಕಿತ್ಸೆ ತೋರಿಸಿ — ಆಮ್ಲೀಯ ಮಣ್ಣಿಗೆ ಸುಣ್ಣ ಹಾಕಿ ಸಸ್ಯ ಚೇತರಿಸಿದ್ದು)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "treated"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'treated' — simulation auto-selects acidic soil (800ms) then applies lime treatment (1800ms). Plant changes from 🥀 to 🌿.",
            "attempt_2": "Set 'initialState' to 'treated'. Full neutralisation: soil acid + lime base → pH 7, plant recovers.",
            "attempt_3": "Choose 'treated': watch the plant go from wilted to healthy! Neutralisation is complete."
        },
        "concept_reminder": (
            "Acidic soil + Lime (base) → neutralisation → pH 7 → healthy plant 🌿. "
            "Same neutralisation equation: acid + base → salt + water. "
            "This is real agricultural chemistry — farmers do this every season! "
            "(ಸುಣ್ಣ ಹಾಕಿ ತಟಸ್ಥೀಕರಣ: ಆಮ್ಲ + ಕ್ಷಾರ → ಉಪ್ಪು + ನೀರು → ಸಸ್ಯ ಆರೋಗ್ಯ!)"
        )
    }
]


# =============================================================================
# CONDUCTORS AND INSULATORS SIMULATION (sim10 — Chapter 3)
# ವಾಹಕಗಳು ಮತ್ತು ಅವಾಹಕಗಳು – ವಿದ್ಯುತ್ ಪರೀಕ್ಷೆ
# =============================================================================
SIMULATIONS_KN["conductors_insulators_kn"] = {
    "title": "ವಾಹಕ ಮತ್ತು ಅವಾಹಕ (Conductors and Insulators)",
    "language": "kannada",
    "file": "simulations_kannada/science_chapter3_simulation10_conductors_insulators_kn.html",
    "description": (
        "Kannada Chapter 3 simulation: students test 8 common materials in a virtual "
        "circuit. Metals (spoon, key, coin, foil) light the bulb — confirmed conductors. "
        "Non-metals (plastic, rubber, wood, glass) keep the bulb off — confirmed insulators. "
        "Score panel tracks conductors vs insulators found. Includes safety rules for "
        "handling electricity."
    ),
    "cannot_demonstrate": [
        "Semiconductors or partial conductors",
        "Effect of temperature on conductivity",
        "Measurement of resistance in ohms"
    ],
    "initial_params": {"initialState": "conductor", "showHints": True},
    "parameter_info": {
        "initialState": {
            "label": "Test Material",
            "range": "conductor, insulator",
            "url_key": "initialState",
            "effect": (
                "Auto-tests a material in the circuit on load.\n"
                "  'conductor' → tests metal spoon (🥄) — bulb lights up, circuit complete\n"
                "  'insulator' → tests plastic scale (📏) — bulb stays off, circuit broken"
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
            "title": "ವಾಹಕಗಳು: ಲೋಹಗಳು ವಿದ್ಯುತ್ ಹರಿಸುತ್ತವೆ (Metals Conduct Electricity)",
            "description": (
                "Conductors allow electric current to flow freely. Metals like copper, "
                "iron, and aluminium have free electrons that can move through the material "
                "carrying the current. The bulb lights up when a conductor completes the circuit."
            ),
            "key_insight": (
                "Conductors = metals = free electrons = current flows = bulb ON. "
                "Spoon, key, coin, foil all light the bulb. This is why electrical wires "
                "are made of copper inside."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 2,
            "title": "ಅವಾಹಕಗಳು: ಲೋಹೇತರ ವಸ್ತುಗಳು ವಿದ್ಯುತ್ ತಡೆಯುತ್ತವೆ",
            "description": (
                "Insulators prevent electric current from flowing. Plastic, rubber, wood, "
                "and glass hold their electrons tightly in chemical bonds — no free electrons "
                "to carry the current. The bulb stays off when an insulator is in the circuit."
            ),
            "key_insight": (
                "Insulators = non-metals = tightly-bound electrons = no current = bulb OFF. "
                "Plastic, rubber, wood, glass all keep the bulb off. This is why wires "
                "are coated with plastic insulation for safety."
            ),
            "related_params": ["initialState"]
        },
        {
            "id": 3,
            "title": "ಭದ್ರತೆ: ಮಾನವ ದೇಹ ವಾಹಕ (Human Body is a Conductor)",
            "description": (
                "The human body conducts electricity (contains ions in body fluids). "
                "Never touch live wires with bare hands, wet hands, or metallic tools. "
                "Rubber gloves and wooden handles are safe insulating materials used by electricians."
            ),
            "key_insight": (
                "Safety: body = conductor → electric shock risk. "
                "Always use insulating materials (rubber, plastic, dry wood) near electricity. "
                "Never use metallic tools near live wires."
            ),
            "related_params": ["initialState", "showHints"]
        }
    ]
}

QUIZ_QUESTIONS_KN["conductors_insulators_kn"] = [
    {
        "id": "conductor_q1",
        "challenge": (
            "Show a CONDUCTOR being tested in the circuit. Demonstrate that metals "
            "allow current to flow and light the bulb.\n\n"
            "(ವಾಹಕ ಪದಾರ್ಥ ಪರೀಕ್ಷಿಸಿ — ಬಲ್ಬ್ ಬೆಳಗುವುದನ್ನು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "conductor"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'conductor' — the metal spoon is auto-tested. Circuit completes, bulb lights yellow.",
            "attempt_2": "Set 'initialState' to 'conductor'. Metal has free electrons — current flows — bulb ON.",
            "attempt_3": "Choose 'conductor': spoon (metal) tested → bulb glows → circuit complete → confirmed conductor."
        },
        "concept_reminder": (
            "Conductors (metals) have FREE electrons that carry current. "
            "Spoon, key, coin, foil → all light the bulb. Bulb ON = conductor. "
            "(ವಾಹಕ + ಸರ್ಕ್ಯೂಟ್ → ಬಲ್ಬ್ ಬೆಳಗುತ್ತದೆ! ಮುಕ್ತ ಇಲೆಕ್ಟ್ರಾನ್‌ಗಳು!)"
        )
    },
    {
        "id": "conductor_q2",
        "challenge": (
            "Show an INSULATOR being tested in the circuit. Demonstrate that non-metal "
            "materials break the circuit and the bulb stays off.\n\n"
            "(ಅವಾಹಕ ಪದಾರ್ಥ ಪರೀಕ್ಷಿಸಿ — ಬಲ್ಬ್ ಆಫ್ ಆಗಿ ಉಳಿಯುವುದನ್ನು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "insulator"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'insulator' — the plastic scale is auto-tested. No current flows, bulb stays dim/off.",
            "attempt_2": "Set 'initialState' to 'insulator'. Non-metals hold electrons tightly — no current — bulb OFF.",
            "attempt_3": "Choose 'insulator': plastic scale tested → bulb stays dark → circuit broken → confirmed insulator."
        },
        "concept_reminder": (
            "Insulators (non-metals) hold electrons tightly — NO free electrons to carry current. "
            "Plastic, rubber, wood, glass → all keep the bulb off. Bulb OFF = insulator. "
            "(ಅವಾಹಕ + ಸರ್ಕ್ಯೂಟ್ → ಬಲ್ಬ್ ಆಫ್! ಇಲೆಕ್ಟ್ರಾನ್‌ಗಳು ಚಲಿಸಲಾರವು!)"
        )
    },
    {
        "id": "conductor_q3",
        "challenge": (
            "Show a conductor test again and explain — why do electrical wires have "
            "METAL INSIDE and PLASTIC OUTSIDE?\n\n"
            "(ವಿದ್ಯುತ್ ತಂತಿಯಲ್ಲಿ ಒಳಗೆ ತಾಮ್ರ, ಹೊರಗೆ ಪ್ಲಾಸ್ಟಿಕ್ ಯಾಕಿದೆ?)"
        ),
        "target_parameters": ["initialState"],
        "success_rule": {
            "conditions": [{"parameter": "initialState", "operator": "==", "value": "conductor"}],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": "Select 'conductor' — watch the metal carry current. Metal inside = conducts; plastic outside = insulates & protects.",
            "attempt_2": "Set 'initialState' to 'conductor'. The metal (conductor) carries the electricity; plastic (insulator) prevents accidental shocks.",
            "attempt_3": "Choose 'conductor': metal spoon lights the bulb. In a wire: copper (metal) = current pathway, plastic = safety barrier."
        },
        "concept_reminder": (
            "Wire design = conductor + insulator working together. "
            "Copper/metal inside → carries current (conductor). "
            "Plastic/rubber outside → blocks accidental current leakage (insulator). "
            "Both are essential! "
            "(ತಂತಿ = ತಾಮ್ರ (ವಾಹಕ) + ಪ್ಲಾಸ್ಟಿಕ್ ಆವರಣ (ಅವಾಹಕ) = ಸುರಕ್ಷಿತ ವಿದ್ಯುತ್!)"
        )
    }
]


# ═══════════════════════════════════════════════════════════════════════
# HELPER: list of Kannada simulation IDs for sidebar grouping
# ═══════════════════════════════════════════════════════════════════════

KN_SIMULATION_IDS = list(SIMULATIONS_KN.keys())
