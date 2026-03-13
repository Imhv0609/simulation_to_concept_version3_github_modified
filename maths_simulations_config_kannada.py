"""
Maths Simulations Configuration - Kannada (ಕನ್ನಡ)
===================================================
Contains metadata, parameters, concepts, and quiz questions for
Kannada-medium MATHS simulations designed for native-language learners.

These simulations have their UI, labels, and instructions written in Kannada.
The agent pipeline continues to operate in English for consistent evaluation;
the translation layer handles student-facing communication in Kannada.

Each entry follows the EXACT same structure as simulations_config.py so that
all existing helper functions (get_simulation, get_quiz_questions, etc.) work
transparently after this file is merged at runtime.

This file is imported and merged into simulations_config.py at the bottom of
that file via:
    from maths_simulations_config_kannada import SIMULATIONS_MATHS_KN, QUIZ_QUESTIONS_MATHS_KN
    SIMULATIONS.update(SIMULATIONS_MATHS_KN)
    QUIZ_QUESTIONS.update(QUIZ_QUESTIONS_MATHS_KN)
"""

# ═══════════════════════════════════════════════════════════════════════
# KANNADA MATHS SIMULATION DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════

SIMULATIONS_MATHS_KN = {}


# =============================================================================
# PLACE VALUE CALCULATOR SIMULATION
# ಸ್ಥಾನ ಬೆಲೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್ – ಸ್ಥಾನ ಬೆಲೆ ಬಟನ್‌ಗಳಿಂದ ಸಂಖ್ಯೆ ನಿರ್ಮಾಣ
# Maths Chapter 1 – Knowing Our Numbers (Place Value)
# Student level: medium
# =============================================================================
SIMULATIONS_MATHS_KN["place_value_calculator_kn"] = {
    "title": "ಸ್ಥಾನ ಬೆಲೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್ (Place Value Calculator)",

    # Mark as Kannada so the sidebar can group it in the Kannada-Maths section
    "language": "kannada_maths",

    # Relative path from the project root — matches the folder structure
    "file": "maths_simulations_kannada/math_chapter1_simulation1_place_value_calculator_kn.html",

    "description": """
An interactive Kannada-language maths simulation where students build numbers
by pressing coloured place-value buttons (+1, +10, +100, +1K, +10K, +1L, +10L).
A live bar chart updates to show how many of each place value have been used,
and the number is displayed in Indian number format (using commas for lakhs/thousands).

Two modes are available:
- Challenge Mode: a target number is given; students must build it using as few
  clicks as possible, discovering that the minimum clicks equals the digit-sum.
- Free Explore Mode: students build any number freely and observe patterns.

The simulation teaches:
- Place value: ones, tens, hundreds, thousands, ten-thousands, lakhs, ten-lakhs
- Indian place value notation (commas at thousands and lakhs, not just thousands)
- The digit-sum property: minimum clicks to build a number = sum of its digits
- Efficient number decomposition (each digit tells how many times to press that button)

The simulation UI, labels, and narrative are entirely in Kannada for native
language learners. Driving parameters are exposed via URL query strings so
the teaching agent can set the demonstration state directly.
""",

    "cannot_demonstrate": [
        "International (Western) place value notation (millions/billions)",
        "Subtraction or decomposition of numbers",
        "Decimals or fractional place values",
        "Place value beyond ten-lakhs (crores and above)",
        "Negative numbers",
        "Arithmetic operations beyond building a number by addition"
    ],

    # ── Agent-controllable parameters ──────────────────────────────────────
    # mode         : string  – 'challenge' or 'free' — selects the activity mode
    # targetIndex  : int     – 0..9 — selects which target number to show in challenge mode
    # restrict     : string  – 'all', '1000', '100', '10' — limits which buttons are active
    "initial_params": {
        "mode": "challenge",
        "targetIndex": 0,
        "restrict": "all"
    },

    "parameter_info": {
        "mode": {
            "label": "Simulation Mode",
            "range": "challenge, free",
            "url_key": "mode",
            "effect": (
                "Controls which activity mode the simulation opens in.\n"
                "  'challenge' → a target number is displayed; student must build it\n"
                "                using as few clicks as possible (default)\n"
                "  'free'      → free exploration; student can build any number with\n"
                "                no target — good for open-ended discovery"
            )
        },
        "targetIndex": {
            "label": "Target Number Index",
            "range": "0-9 (integer)",
            "url_key": "targetIndex",
            "effect": (
                "In Challenge mode, selects which of the 10 preset target numbers is shown.\n"
                "  0 → 5,072     (4-digit, digit-sum 14 — textbook example)\n"
                "  1 → 8,300     (zero in tens place — tests understanding of zeros)\n"
                "  2 → 40,629    (5-digit number)\n"
                "  3 → 56,354    (5-digit, balanced digits)\n"
                "  4 → 66,666    (all same digit — interesting pattern)\n"
                "  5 → 3,67,813  (6-digit, uses lakh place)\n"
                "  6 → 997       (3-digit, digit-sum 25 — minimum clicks challenge)\n"
                "  7 → 1,00,000  (exactly one lakh — landmark number)\n"
                "  8 → 75,000    (round number in thousands)\n"
                "  9 → 321       (simple 3-digit starter)"
            )
        },
        "restrict": {
            "label": "Button Restriction",
            "range": "all, 1000, 100, 10",
            "url_key": "restrict",
            "effect": (
                "Restricts which place-value buttons the student can press.\n"
                "  'all'  → all buttons available (default — normal play)\n"
                "  '1000' → only +1K button active; student must press it repeatedly;\n"
                "           teaches how many thousands are in large numbers\n"
                "  '100'  → only +100 button active; explores hundreds decomposition\n"
                "  '10'   → only +10 button active; explores tens decomposition"
            )
        }
    },

    # ── Teaching concepts ────────────────────────────────────────────────────
    # 3 concepts in progression: foundation → pattern discovery → application
    "concepts": [
        {
            "id": 1,
            "title": "Place Value: Every Digit Has a Position and a Value",
            "description": (
                "Understanding that the position of a digit in a number determines its value. "
                "In 5,072: the digit 5 means five thousands, 0 means no hundreds, "
                "7 means seven tens, 2 means two ones."
            ),
            "key_insight": (
                "Each place-value button (+1, +10, +100, +1K, etc.) adds exactly that value. "
                "The bar chart shows how many of each place value makes up the number. "
                "5,072 needs 5 presses of +1K, 0 of +100, 7 of +10, and 2 of +1."
            ),
            "related_params": ["mode", "targetIndex"]
        },
        {
            "id": 2,
            "title": "The Digit-Sum Property: Minimum Clicks = Sum of Digits",
            "description": (
                "The minimum number of button-presses needed to build any number is always "
                "equal to the sum of its digits. This reveals why place value notation is "
                "the most efficient way to represent numbers."
            ),
            "key_insight": (
                "For 5,072: digit sum = 5+0+7+2 = 14. You need exactly 14 presses. "
                "This works for ALL numbers — the digit sum tells you the minimum presses. "
                "This IS Indian place value: each digit tells how many times to press that button."
            ),
            "related_params": ["mode", "targetIndex"]
        },
        {
            "id": 3,
            "title": "Indian Place Value System: Ones, Thousands, Lakhs",
            "description": (
                "The Indian place value system groups digits as ones (1-999), "
                "thousands (1,000-99,999), lakhs (1,00,000-99,99,999), and crores. "
                "Commas are placed after every 2 digits from the right (except the first group of 3)."
            ),
            "key_insight": (
                "Indian format: 3,67,813 (not 367,813 as in Western format). "
                "After the first comma (thousands), subsequent commas come every 2 digits: "
                "3 | 67 | 813. The simulation uses Indian notation throughout — "
                "lakhs and ten-lakhs are explicitly shown as separate place values."
            ),
            "related_params": ["mode", "targetIndex", "restrict"]
        }
    ]
}


# ═══════════════════════════════════════════════════════════════════════
# QUIZ QUESTIONS — KANNADA MATHS SIMULATIONS
# ═══════════════════════════════════════════════════════════════════════

QUIZ_QUESTIONS_MATHS_KN = {}


# =============================================================================
# PLACE VALUE CALCULATOR — QUIZ QUESTIONS
# 3 questions: understand place value → discover digit-sum property → apply lakh notation
#
# Quiz parameters:
#   mode        (string): 'challenge' | 'free'
#   targetIndex (int):    0..9
#   restrict    (string): 'all' | '1000' | '100' | '10'
#   The student selects from dropdowns/number inputs in the Streamlit quiz UI.
#   The simulation iframe reflects the chosen values via URL params:
#     ?mode=challenge&targetIndex=0&restrict=all
#   Evaluation uses string/numeric equality (handled by quiz_rules.py fallback).
# =============================================================================

QUIZ_QUESTIONS_MATHS_KN["place_value_calculator_kn"] = [

    # ── Q1: Understand place value with the textbook 5,072 example ─────────
    {
        "id": "place_value_kn_q1",
        "challenge": (
            "Set the simulation to Challenge mode and select the textbook number 5,072 "
            "(index 0) as the target. This is the classic example used in the NCERT textbook "
            "for Class 6 place value. Observe how many of each place-value button you need "
            "to press to reach 5,072 using the minimum clicks.\n\n"
            "(ಪಠ್ಯಪುಸ್ತಕದ ಉದಾಹರಣೆ 5,072 ಗುರಿಯಾಗಿ ಇಟ್ಟು ಸವಾಲು ಮೋಡ್ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["mode", "targetIndex"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "mode",
                    "operator": "==",
                    "value": "challenge"
                },
                {
                    "parameter": "targetIndex",
                    "operator": "==",
                    "value": 0
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
                "Set Mode to 'challenge' and Target Number Index to 0. "
                "Index 0 loads the textbook example 5,072. "
                "Then observe: you need 5 presses of +1K, 0 of +100, 7 of +10, 2 of +1 — "
                "that is exactly 14 minimum clicks (= 5+0+7+2, the digit sum)."
            ),
            "attempt_2": (
                "Choose mode='challenge' and targetIndex=0. "
                "The target 5,072 will appear. Notice the bar chart: bar for 'ಸಾವಿರ' (+1K) "
                "must reach height 5, 'ಹತ್ತು' (+10) must reach 7, 'ಒಂದು' (+1) must reach 2, "
                "and 'ನೂರು' (+100) stays at 0."
            ),
            "attempt_3": (
                "Select mode='challenge' and targetIndex=0 to load 5,072. "
                "The minimum clicks = digit sum of 5,072 = 5+0+7+2 = 14. "
                "This is the key insight: place value tells you HOW MANY times to press each button."
            )
        },
        "concept_reminder": (
            "Place value: 5,072 = 5×1000 + 0×100 + 7×10 + 2×1. "
            "Each digit tells how many of that place value the number contains. "
            "The digit in the thousands place (5) means five thousands; "
            "the digit in the tens place (7) means seven tens. "
            "(ಪ್ರತಿ ಅಂಕಿ ಪ್ರತಿ ಸ್ಥಾನ ಬೆಲೆಯಲ್ಲಿ ಎಷ್ಟಿದೆ ಎಂದು ತಿಳಿಸುತ್ತದೆ!)"
        )
    },

    # ── Q2: Discover the digit-sum property with a lakh-scale number ───────
    {
        "id": "place_value_kn_q2",
        "challenge": (
            "Now select the 6-digit number 3,67,813 (targetIndex 5) in Challenge mode. "
            "This number uses the lakh place value. Before clicking, calculate its digit sum "
            "(3+6+7+8+1+3 = 28). This should be the minimum number of button presses. "
            "Set the simulation to show this target.\n\n"
            "(6 ಅಂಕಿಯ ಸಂಖ್ಯೆ 3,67,813 ಗುರಿಯಾಗಿ ಇಟ್ಟು ಲಕ್ಷ ಸ್ಥಾನ ಬೆಲೆ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["mode", "targetIndex"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "mode",
                    "operator": "==",
                    "value": "challenge"
                },
                {
                    "parameter": "targetIndex",
                    "operator": "==",
                    "value": 5
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
                "Set mode='challenge' and targetIndex=5. "
                "Index 5 loads 3,67,813 — a six-digit number with a lakh digit. "
                "Digit sum = 3+6+7+8+1+3 = 28. You need 28 minimum clicks — "
                "including 3 presses of the +1L (lakh) button."
            ),
            "attempt_2": (
                "Choose mode='challenge' and targetIndex=5 to load 3,67,813. "
                "The bar for 'ಲಕ್ಷ' (+1L) should show 3, 'ಹ.ಸಾವಿರ' (+10K) shows 6, "
                "'ಸಾವಿರ' (+1K) shows 7, 'ನೂರು' (+100) shows 8, 'ಹತ್ತು' (+10) shows 1, "
                "'ಒಂದು' (+1) shows 3."
            ),
            "attempt_3": (
                "Set mode='challenge', targetIndex=5 for 3,67,813. "
                "This demonstrates Indian lakh notation: 3,67,813 is 'three lakh sixty-seven "
                "thousand eight hundred thirteen'. The lakh place is the 6th digit from the right."
            )
        },
        "concept_reminder": (
            "3,67,813 = 3×1,00,000 + 6×10,000 + 7×1,000 + 8×100 + 1×10 + 3×1. "
            "In the Indian system, one lakh = 1,00,000 (not 100,000 written as in the West). "
            "Digit sum = 3+6+7+8+1+3 = 28 = minimum clicks to build this number. "
            "(ಡಿಜಿಟ್ ಮೊತ್ತ = ಕನಿಷ್ಠ ಕ್ಲಿಕ್‌ಗಳು — ಸ್ಥಾನ ಬೆಲೆ ವ್ಯವಸ್ಥೆಯ ಸೊಬಗು!)"
        )
    },

    # ── Q3: Explore zeros in place value with restrict mode ─────────────────
    {
        "id": "place_value_kn_q3",
        "challenge": (
            "Set the simulation to Challenge mode with target number 1,00,000 "
            "(one lakh, targetIndex 7), AND restrict the buttons to '+1K only' "
            "(restrict='1000'). Count how many presses of +1K it takes to reach one lakh. "
            "This shows how many thousands are in one lakh.\n\n"
            "(ಒಂದು ಲಕ್ಷ ತಲುಪಲು +1K ಮಾತ್ರ ಬಳಸಿ — ಎಷ್ಟು ಬಾರಿ ಒತ್ತಬೇಕು?)"
        ),
        "target_parameters": ["mode", "targetIndex", "restrict"],
        "success_rule": {
            "conditions": [
                {
                    "parameter": "mode",
                    "operator": "==",
                    "value": "challenge"
                },
                {
                    "parameter": "targetIndex",
                    "operator": "==",
                    "value": 7
                },
                {
                    "parameter": "restrict",
                    "operator": "==",
                    "value": "1000"
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
                "Set mode='challenge', targetIndex=7 (for 1,00,000), and restrict='1000'. "
                "With only +1K available, you must press it 100 times to reach one lakh. "
                "This concretely shows: 1 lakh = 100 thousands."
            ),
            "attempt_2": (
                "Choose mode='challenge', targetIndex=7, restrict='1000'. "
                "1,00,000 ÷ 1,000 = 100 presses required. "
                "The bar chart will show the 'ಸಾವಿರ' bar reaching count 100 "
                "before the 'ಲಕ್ಷ' bar activates — revealing the place-value relationship."
            ),
            "attempt_3": (
                "Set targetIndex=7 (1,00,000) and restrict='1000'. "
                "You need exactly 100 presses of +1K to reach one lakh. "
                "Answer to 'how many thousands in one lakh?' is 100. "
                "This is the key relationship: 1 lakh = 100 thousand = 1,000 × 100."
            )
        },
        "concept_reminder": (
            "1,00,000 (one lakh) = 100 × 1,000 (one thousand). "
            "The zero digits in 1,00,000 are significant: they show that there are "
            "no hundreds, no tens, and no ones — ONLY the lakh place has a value. "
            "Zeros as place-holders are essential: without them, the number would read '1' not '1,00,000'. "
            "(ಸೊನ್ನೆ ಸ್ಥಾನ ಭರ್ತಿ ಮಾಡುತ್ತದೆ — ಇಲ್ಲದಿದ್ದರೆ 1,00,000 ಬರೀ 1 ಆಗಿಬಿಡುತ್ತಿತ್ತು!)"
        )
    }
]


# ═══════════════════════════════════════════════════════════════════════
# HELPER: list of Kannada-Maths simulation IDs for sidebar grouping
# ═══════════════════════════════════════════════════════════════════════

MATHS_KN_SIMULATION_IDS = list(SIMULATIONS_MATHS_KN.keys())
