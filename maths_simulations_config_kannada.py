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


# =============================================================================
# NUMBER SYSTEMS SIMULATION
# ಭಾರತೀಯ vs ಅಂತರರಾಷ್ಟ್ರೀಯ ಸಂಖ್ಯಾ ವ್ಯವಸ್ಥೆ – Indian vs International Number Systems
# Maths Chapter 1 – Knowing Our Numbers (Number Systems)
# =============================================================================
SIMULATIONS_MATHS_KN["number_systems_kn"] = {
    "title": "ಭಾರತೀಯ vs ಅಂತರರಾಷ್ಟ್ರೀಯ ಸಂಖ್ಯಾ ವ್ಯವಸ್ಥೆ (Number Systems)",
    "language": "kannada_maths",
    "file": "maths_simulations_kannada/math_chapter1_simulation2_number_systems_kn.html",
    "description": """
An interactive Kannada-language simulation comparing the Indian and International number
systems side by side. Students explore a number displayed simultaneously in both notations
(Indian: 3-2-2 grouping with commas; International: 3-3-3 grouping) and convert between
systems using a labelled digit strip.

Two modes are available:
- Explore Mode: adjust a slider to choose any number up to 9,99,99,999 and see it in both
  systems instantly, with the full word-name in each system.
- Quiz Mode: comparison questions (e.g., 'Is 30 Thousand < 3 Lakhs?') test understanding of
  relative magnitudes across both systems.

The simulation teaches:
- Indian place value: ones, thousands, ten-thousands, lakhs, ten-lakhs, crores
- International place value: ones, thousands, millions, billions
- Comma-grouping rules for each system (3-2 vs 3-3)
- Cross-system conversion: 1 Crore = 10 Million, 1 Lakh = 100 Thousand
""",
    "cannot_demonstrate": [
        "Decimals or fractions in either number system",
        "Numbers larger than 99,99,99,999 (ten crore / one billion)",
        "Arithmetic operations across number systems",
        "Roman numerals or other historical number systems",
        "Negative numbers"
    ],
    "initial_params": {
        "mode": "explore",
        "number": 4050678
    },
    "parameter_info": {
        "mode": {
            "label": "Simulation Mode",
            "range": "explore, quiz",
            "url_key": "mode",
            "effect": (
                "Controls which activity mode the simulation opens in.\n"
                "  'explore' → slider lets student adjust the number and see both systems side by side\n"
                "  'quiz'    → presents comparison questions (< > =) between Indian and International magnitudes"
            )
        },
        "number": {
            "label": "Starting Number",
            "range": "1 – 999,999,999 (integer)",
            "url_key": "number",
            "effect": (
                "Sets the initial number displayed in explore mode.\n"
                "The digit strip and word-names update instantly to show it in both systems."
            )
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Indian vs International Comma Grouping",
            "description": (
                "The Indian system groups digits as 3 from the right, then 2-2-2 (right to left): "
                "e.g., 40,50,678. The International system groups as 3-3-3: 4,050,678."
            ),
            "key_insight": (
                "The same number looks different in each system because of the comma positions. "
                "40,50,678 (Indian) = 4,050,678 (International). Both represent 'forty lakh fifty thousand six hundred seventy-eight'."
            ),
            "related_params": ["mode", "number"]
        },
        {
            "id": 2,
            "title": "Cross-System Conversion: Lakhs, Crores, Millions",
            "description": (
                "Key conversion facts: 1 Lakh = 1,00,000 = 100 Thousand; "
                "1 Crore = 1,00,00,000 = 10 Million; 100 Crore = 1 Billion."
            ),
            "key_insight": (
                "When comparing across systems, use anchor conversions. "
                "The quiz mode tests these: '500 Lakhs vs 5 Million' — knowing 1 Lakh = 100 Thousand "
                "quickly shows 500 Lakhs = 5,00,00,000 while 5 Million = 50,00,000, so 500 Lakhs > 5 Million."
            ),
            "related_params": ["mode"]
        },
        {
            "id": 3,
            "title": "Reading Large Numbers in Both Systems",
            "description": (
                "Practise reading numbers aloud using both systems: "
                "Indian word-names use 'lakh' and 'crore'; International names use 'million' and 'billion'."
            ),
            "key_insight": (
                "The digit strip shows exactly which comma goes where in each system. "
                "Indian: ...| crore | ten-lakh | lakh | ten-thousand | thousand | hundred | ten | one. "
                "International: ...| billion | hundred-million | ten-million | million | hundred-thousand | ten-thousand | thousand | hundred | ten | one."
            ),
            "related_params": ["mode", "number"]
        }
    ]
}


# =============================================================================
# SENSE OF SCALE SIMULATION
# ಸ್ಕೇಲ್ ಅರಿವು – Large Number Visualisation
# Maths Chapter 1 – Knowing Our Numbers (Large Numbers)
# =============================================================================
SIMULATIONS_MATHS_KN["sense_of_scale_kn"] = {
    "title": "ಸ್ಕೇಲ್ ಅರಿವು — ದೊಡ್ಡ ಸಂಖ್ಯೆ ದೃಶ್ಯೀಕರಣ (Sense of Scale)",
    "language": "kannada_maths",
    "file": "maths_simulations_kannada/math_chapter1_simulation3_sense_of_scale_kn.html",
    "description": """
A real-world Kannada-language simulation that makes large numbers tangible by embedding them
in concrete, relatable scenarios. Students adjust sliders and see progress bars scale against
familiar reference quantities.

Five scenario tabs are available:
- Journey (ಪ್ರಯಾಣ): driving at a chosen speed for a chosen number of years — comparing distance
  to the Moon, the Sun, and the Trans-Siberian railway.
- Buses (ಬಸ್‌ಗಳು): filling buses with passengers to try to match city populations (Chintamani,
  Jaipur, Mumbai).
- Weight (ತೂಕ): stacking small items to compare their combined weight against a child, adult,
  or weightlifter.
- Counting (ಎಣಿಕೆ): counting items at a chosen rate — does it fit within an hour, a day, a year?
- Facts (ತಥ್ಯಗಳು): probability-based facts (e.g., chance of getting a specific 10-digit phone number).

The simulation teaches:
- Real-world meaning of numbers in the lakh and crore range
- Relative comparisons using progress bars (are we there yet?)
- Multiplicative reasoning with large factor products
""",
    "cannot_demonstrate": [
        "Exact arithmetic computations step-by-step",
        "Numbers in the billions range",
        "Probability theory beyond intuitive comparison",
        "Geographic or scientific facts beyond the stated scenarios"
    ],
    "initial_params": {
        "scenario": 0
    },
    "parameter_info": {
        "scenario": {
            "label": "Scenario Tab",
            "range": "0-4 (integer)",
            "url_key": "scenario",
            "effect": (
                "Selects which real-world scenario tab the simulation opens on.\n"
                "  0 → Journey (🚀 — driving speed × years vs astronomical distances)\n"
                "  1 → Buses (🚌 — passengers × buses vs city populations)\n"
                "  2 → Weight (⚖️ — item weight × count vs human weights)\n"
                "  3 → Counting (⏱️ — items at rate vs time durations)\n"
                "  4 → Facts (🔢 — probability-based number facts)"
            )
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Large Numbers Need Real-World Anchors",
            "description": (
                "Abstract numbers like 1,00,00,000 are hard to sense. "
                "Anchoring them to physical journeys, populations, or time makes them concrete."
            ),
            "key_insight": (
                "Driving 100 km/day for 10 years covers 3,65,000 km — just short of Earth-Moon distance (3,84,400 km). "
                "Suddenly '3.6 lakh' feels like a real and almost reachable scale."
            ),
            "related_params": ["scenario"]
        },
        {
            "id": 2,
            "title": "Multiplicative Scaling with Progress Bars",
            "description": (
                "Progress bars show what fraction of a reference quantity a student's chosen value reaches. "
                "Filling a bar requires multiplying two controllable quantities."
            ),
            "key_insight": (
                "In the Buses scenario: 50 passengers × 2,00,000 buses = 1,00,00,000 (one crore) people — "
                "enough to fill Jaipur nearly three times. This reveals how multiplying modest numbers "
                "quickly reaches crore-scale quantities."
            ),
            "related_params": ["scenario"]
        },
        {
            "id": 3,
            "title": "Comparing Magnitudes: Which Is Bigger?",
            "description": (
                "Comparing two large quantities (e.g., 50 lakh vs Mumbai's 1.24 crore) requires "
                "understanding both numbers in Indian notation and knowing their relative sizes."
            ),
            "key_insight": (
                "Use the progress bar percentage: if the bar shows 40%, the student's number is "
                "less than half the reference. This makes > / < comparisons intuitive without needing "
                "to line up digits."
            ),
            "related_params": ["scenario"]
        }
    ]
}


# =============================================================================
# ROUNDING & ESTIMATION SIMULATION
# ಪೂರ್ಣಾಂಕನ ಮತ್ತು ಅಂದಾಜು – Rounding and Estimation
# Maths Chapter 1 – Knowing Our Numbers (Rounding)
# =============================================================================
SIMULATIONS_MATHS_KN["rounding_estimation_kn"] = {
    "title": "ಪೂರ್ಣಾಂಕನ ಮತ್ತು ಅಂದಾಜು (Rounding and Estimation)",
    "language": "kannada_maths",
    "file": "maths_simulations_kannada/math_chapter1_simulation4_rounding_estimation_kn.html",
    "description": """
An interactive Kannada-language simulation that teaches rounding large numbers to the nearest
thousand, ten-thousand, lakh, ten-lakh, and crore using animated number-line visualisations.

Two modes are available:
- Explore Mode: a slider lets the student choose any number; five number lines (one per rounding
  place) update simultaneously, showing the red marker (actual position) and blue snap marker
  (rounded value). The rounded value for each place is displayed alongside the number line.
- Quiz Mode: estimation questions based on real Indian census data and textbook examples test
  whether students can round correctly and compare sums/differences.

The simulation teaches:
- The rounding rule: if the digit in the next smaller place is ≥ 5, round up; else round down
- Visual intuition: where does the number lie on the number line between two multiples?
- Estimation in context: approximating sums of large populations to the nearest lakh/crore
""",
    "cannot_demonstrate": [
        "Rounding to the nearest ten or hundred (the slider minimum is in tens of thousands)",
        "Decimal rounding",
        "Negative number rounding",
        "Numbers larger than 9,99,99,999 (ten crore)"
    ],
    "initial_params": {
        "mode": "explore",
        "number": 38769957
    },
    "parameter_info": {
        "mode": {
            "label": "Simulation Mode",
            "range": "explore, quiz",
            "url_key": "mode",
            "effect": (
                "Controls which activity mode the simulation opens in.\n"
                "  'explore' → number lines show all five rounding places at once for the chosen number\n"
                "  'quiz'    → estimation questions using real census data and textbook numbers"
            )
        },
        "number": {
            "label": "Starting Number",
            "range": "1 – 99,999,999 (integer)",
            "url_key": "number",
            "effect": (
                "Sets the initial number shown by the number lines in explore mode. "
                "All five number lines (nearest thousand up to nearest crore) update to reflect it."
            )
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "The Rounding Rule: ≥ 5 Round Up, < 5 Round Down",
            "description": (
                "To round to a given place, look at the digit immediately to the right. "
                "If it is 5 or more, add 1 to the rounding digit; if less than 5, keep the rounding digit."
            ),
            "key_insight": (
                "For 3,87,69,957 rounded to the nearest crore: the ten-lakh digit is 8 (≥ 5) so round up → 4,00,00,000. "
                "The number lines make this visible: the red marker is closer to the upper end of the interval."
            ),
            "related_params": ["mode", "number"]
        },
        {
            "id": 2,
            "title": "Visual Number Lines for Every Rounding Place",
            "description": (
                "Each number line spans from the lower multiple to the upper multiple of one rounding unit. "
                "The red marker shows the number's exact position; the blue snap shows where it rounds to."
            ),
            "key_insight": (
                "If the red marker is past the midpoint (50%), the blue snap jumps to the right end (round up). "
                "If the red marker is before the midpoint, the blue snap stays at the left end (round down). "
                "Five number lines at once show that a number can round up in some places and down in others."
            ),
            "related_params": ["mode", "number"]
        },
        {
            "id": 3,
            "title": "Estimation Using Rounded Numbers",
            "description": (
                "Adding or comparing city populations is easier when rounded to the nearest lakh. "
                "Estimation is not imprecision — it is deliberate, useful approximation."
            ),
            "key_insight": (
                "4,63,128 + 4,19,682 ≈ 5 lakh + 4 lakh = 9 lakh (both round up). "
                "Exact answer 8,82,810 confirms the estimate is close. "
                "This shows why rounding is a TOOL: it lets you verify a calculation quickly."
            ),
            "related_params": ["mode"]
        }
    ]
}


# =============================================================================
# MULTIPLICATION PATTERNS SIMULATION
# ಗುಣಾಕಾರ ಭಾವನೆ ಮತ್ತು ಅಂಕಿ ಎಣಿಕೆ – Multiplication Patterns and Digit Counting
# Maths Chapter 1 – Knowing Our Numbers (Multiplication)
# =============================================================================
SIMULATIONS_MATHS_KN["multiplication_patterns_kn"] = {
    "title": "ಗುಣಾಕಾರ ಭಾವನೆ ಮತ್ತು ಅಂಕಿ ಎಣಿಕೆ (Multiplication Patterns)",
    "language": "kannada_maths",
    "file": "maths_simulations_kannada/math_chapter1_simulation5_multiplication_patterns_kn.html",
    "description": """
An interactive Kannada-language simulation that explores the number of digits in a product
when two numbers are multiplied, and reveals shortcuts for multiplying by 10, 100, 1000, etc.

Four tabs are available:
- Multiply (ಗುಣಿಸಿ): two sliders (A and B) let students set any two numbers; the product is
  displayed instantly along with a 'digit range rule' badge: digits(A) + digits(B) - 1 ≤ digits(product) ≤ digits(A) + digits(B).
- Patterns (ಭಾವನೆ): preset multiplication tables showing how digit counts behave when identical
  numbers are multiplied (e.g., 111×111, 1111×1111).
- Shortcuts (ಶಾರ್ಟ್‌ಕಟ್): rules for multiplying by 10 (append zero), 100 (append two zeros), etc.
- Digit Grid (ಅಂಕಿ ಗ್ರಿಡ್): a 5×5 grid showing digit-count ranges for all combinations of 1-5 digit numbers.

The simulation teaches:
- The digit-count rule for products: product has da + db − 1 or da + db digits
- Why multiplying by 10 appends a zero (place-value shift)
- Estimation of product magnitude without computing it
""",
    "cannot_demonstrate": [
        "Decimal multiplication",
        "Division or factorisation",
        "Numbers beyond 5 digits in the digit grid",
        "Negative number multiplication",
        "Exact products beyond the slider range"
    ],
    "initial_params": {
        "mode": "multiply",
        "numA": 111,
        "numB": 111
    },
    "parameter_info": {
        "mode": {
            "label": "Simulation Tab",
            "range": "multiply, patterns, shortcuts, digitGrid",
            "url_key": "mode",
            "effect": (
                "Controls which activity tab the simulation opens on.\n"
                "  'multiply'  → live sliders show product and digit-count rule badge\n"
                "  'patterns'  → preset multiplication tables showing digit-count patterns\n"
                "  'shortcuts' → rules for ×10, ×100, ×1000 with examples\n"
                "  'digitGrid' → 5×5 grid of digit-count ranges for all A×B combinations"
            )
        },
        "numA": {
            "label": "Number A",
            "range": "1 – 99,999 (integer)",
            "url_key": "numA",
            "effect": (
                "Sets the initial value of slider A in multiplication mode. "
                "The digit count of A is highlighted in the digit grid."
            )
        },
        "numB": {
            "label": "Number B",
            "range": "1 – 99,999 (integer)",
            "url_key": "numB",
            "effect": (
                "Sets the initial value of slider B in multiplication mode. "
                "Both slider values together determine starting product and grid highlight."
            )
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "Digit-Count Rule for Products",
            "description": (
                "When multiplying a d_a-digit number by a d_b-digit number, the product always has "
                "either d_a + d_b − 1 or d_a + d_b digits. This lets you estimate the magnitude "
                "of a product before computing it."
            ),
            "key_insight": (
                "111 (3 digits) × 111 (3 digits) = 12,321 (5 digits = 3+3−1). "
                "999 × 999 = 998,001 (6 digits = 3+3). "
                "So 3-digit × 3-digit will always give a 5- or 6-digit product."
            ),
            "related_params": ["mode", "numA", "numB"]
        },
        {
            "id": 2,
            "title": "Multiplication Shortcuts: Appending Zeros",
            "description": (
                "Multiplying any number by 10 shifts every digit one place to the left, "
                "equivalent to appending one zero. Multiplying by 100 appends two zeros, etc."
            ),
            "key_insight": (
                "234 × 10 = 2,340. The digits don't change — each moves one place-value position up. "
                "Place value makes this automatic: ones become tens, tens become hundreds, etc."
            ),
            "related_params": ["mode"]
        },
        {
            "id": 3,
            "title": "Pattern Recognition in Multiplication Tables",
            "description": (
                "Special multiplication tables (e.g., 11×11=121, 111×111=12321, 1111×1111=1234321) "
                "reveal palindrome patterns that arise from the digit-count rule."
            ),
            "key_insight": (
                "111×111 = 12,321 — the product's digits go 1,2,3,2,1. "
                "1111×1111 = 1,234,321 — the pattern extends. "
                "These patterns are not magic; they follow directly from the distributive property "
                "and the place-value structure of the number system."
            ),
            "related_params": ["mode"]
        }
    ]
}


# =============================================================================
# EXPRESSION EVALUATOR SIMULATION
# ಸಮೀಕರಣ ಮೌಲ್ಯಮಾಪನ – Expression Evaluator
# Maths Chapter 2 – Whole Numbers (Algebraic Expressions)
# =============================================================================
SIMULATIONS_MATHS_KN["expression_evaluator_kn"] = {
    "title": "ಸಮೀಕರಣ ಮೌಲ್ಯಮಾಪನ (Expression Evaluator)",
    "language": "kannada_maths",
    "file": "maths_simulations_kannada/math_chapter2_simulation1_expression_evaluator_kn.html",
    "description": """
An interactive Kannada-language simulation that teaches students to identify terms in an
algebraic expression and evaluate each term step-by-step before summing them to find the
final value.

The simulation displays a mathematical expression (e.g., '39 − 2×6 + 11') in coloured term
boxes — each distinct term (separated by + or −) gets its own colour. Step-by-step cards then
show:
  Step 1: Identify the terms and count them.
  Step 2: Evaluate each term individually (respecting multiplication/division before addition).
  Step 3: Add all term values to get the final result.

A preset panel lets students select from 12 built-in expressions of increasing complexity.
The 'problem' URL param lets the agent load any specific expression by index.

The simulation teaches:
- Defining a 'term' in an expression (a quantity separated by + or −)
- Evaluating each term independently before combining
- Why BODMAS/PEMDAS matters: multiplication inside a term must be done first
- Reading expressions that mix subtraction (as negative terms) with addition
""",
    "cannot_demonstrate": [
        "Expressions with variables (only numeric expressions)",
        "Expressions with brackets requiring bracket expansion",
        "Expressions longer than 4 terms",
        "Division resulting in non-integer quotients",
        "Floating-point arithmetic"
    ],
    "initial_params": {
        "problem": 0
    },
    "parameter_info": {
        "problem": {
            "label": "Expression Index",
            "range": "0 – 11 (integer)",
            "url_key": "problem",
            "effect": (
                "Selects which of the 12 preset expressions is displayed.\n"
                "  0  → 28 − 7 + 8        (result: 29 — simple mix of add and subtract)\n"
                "  1  → 39 − 2×6 + 11     (result: 38 — introduces multiplication in a term)\n"
                "  2  → 40 − 10 + 10 + 10 (result: 50 — four terms)\n"
                "  3  → 48 − 10×2 + 16÷2  (result: 36 — both multiplication and division)\n"
                "  4  → 6×3 − 4×8×5       (result: −142 — large negative term)\n"
                "  5  → 30 + 5×4           (result: 50 — classic BODMAS starter)\n"
                "  6  → 4×23 + 5           (result: 97)\n"
                "  7  → 6×5 + 3            (result: 33)\n"
                "  8  → 89 + 21 − 10       (result: 100 — landmark answer)\n"
                "  9  → 5×12 − 6           (result: 54)\n"
                "  10 → 4×9 + 2×6          (result: 48 — two multiplication terms)\n"
                "  11 → 13 − 2 + 6         (result: 17)"
            )
        }
    },
    "concepts": [
        {
            "id": 1,
            "title": "What Is a Term? Separating an Expression",
            "description": (
                "A term is a quantity in an expression that is separated from others by + or −. "
                "The sign before it is part of the term: '39 − 2×6 + 11' has three terms: 39, −2×6, and 11."
            ),
            "key_insight": (
                "Colour-coded boxes make terms visually distinct. "
                "Counting terms correctly is the first step: '48 − 10×2 + 16÷2' has 3 terms, not 5 — "
                "because 10×2 is one term (multiplication within the term, not a separator)."
            ),
            "related_params": ["problem"]
        },
        {
            "id": 2,
            "title": "Evaluate Each Term First (BODMAS Within a Term)",
            "description": (
                "Before adding terms together, each term must be fully evaluated — "
                "multiplication and division within a term must be computed before any addition or subtraction."
            ),
            "key_insight": (
                "In '39 − 2×6 + 11': evaluate 2×6 = 12 first (not 39−2=37 then ×6). "
                "So the terms are 39, −12, and 11, giving 39 − 12 + 11 = 38. "
                "The step-by-step cards guide this exact sequence."
            ),
            "related_params": ["problem"]
        },
        {
            "id": 3,
            "title": "Summing Signed Terms to Get the Final Value",
            "description": (
                "Once all terms are evaluated, add them algebraically — "
                "treating negative terms as subtraction from the running sum."
            ),
            "key_insight": (
                "For problem 4 ('6×3 − 4×8×5'): term 1 = 18, term 2 = −160. Sum = 18 + (−160) = −142. "
                "The result can be negative! Term evaluation prevents the common error of computing "
                "left-to-right without respecting multiplication priority."
            ),
            "related_params": ["problem"]
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


# =============================================================================
# NUMBER SYSTEMS — QUIZ QUESTIONS
# 3 questions: explore Indian notation → learn cross-system conversion → quiz mode
# =============================================================================
QUIZ_QUESTIONS_MATHS_KN["number_systems_kn"] = [

    {
        "id": "number_systems_kn_q1",
        "challenge": (
            "Set the simulation to Explore mode and enter the number 40,50,678 (four crore "
            "fifty lakh six hundred seventy-eight). Observe how the same number is shown in "
            "the Indian system (40,50,678) and the International system (4,050,678) side by side.\n\n"
            "(ಸಂಖ್ಯೆ 4050678 ಅನ್ನು ಭಾರತೀಯ ಮತ್ತು ಅಂತರರಾಷ್ಟ್ರೀಯ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ ತೋರಿಸಿ)"
        ),
        "target_parameters": ["mode", "number"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "explore"},
                {"parameter": "number", "operator": "==", "value": 4050678}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='explore' and number=4050678. "
                "Indian: 40,50,678 (comma after every 2 digits from right, first group of 3). "
                "International: 4,050,678 (comma after every 3 digits from right)."
            ),
            "attempt_2": (
                "Choose mode='explore' and number=4050678. "
                "The digit strip shows both comma placements simultaneously — "
                "red commas for the Indian system, blue commas for International."
            ),
            "attempt_3": (
                "Set mode='explore', number=4050678. "
                "Word name (Indian): 'Forty Lakh Fifty Thousand Six Hundred Seventy-Eight'. "
                "Word name (International): 'Four Million Fifty Thousand Six Hundred Seventy-Eight'."
            )
        },
        "concept_reminder": (
            "40,50,678 (Indian) = 4,050,678 (International). "
            "Indian groups: 3 from right, then 2-2. International groups: 3-3-3 from right. "
            "The numbers are identical — only the comma placement rules differ."
        )
    },

    {
        "id": "number_systems_kn_q2",
        "challenge": (
            "Use the simulation in Quiz mode. Answer the comparison question: "
            "'500 Lakhs ___ 5 Million' (is it <, >, or =?). "
            "Use the explore mode to check: enter 50000000 (5 crore) to see 500 Lakhs, "
            "then check what 5 Million equals in Indian notation.\n\n"
            "(ರಸಪ್ರಶ್ನೆ ಮೋಡ್‌ನಲ್ಲಿ 500 Lakhs vs 5 Million ಹೋಲಿಸಿ)"
        ),
        "target_parameters": ["mode"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "quiz"}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='quiz'. "
                "500 Lakhs = 500 × 1,00,000 = 5,00,00,000 (five crore). "
                "5 Million = 50,00,000 (fifty lakh). "
                "So 500 Lakhs > 5 Million."
            ),
            "attempt_2": (
                "Use mode='quiz'. "
                "Key anchor: 1 Lakh = 100 Thousand = 0.1 Million. "
                "Therefore 500 Lakhs = 50 Million, NOT 5 Million. "
                "500 Lakhs is 10× larger than 5 Million."
            ),
            "attempt_3": (
                "Select mode='quiz'. "
                "To compare: 1 Million = 10 Lakh. So 5 Million = 50 Lakh. "
                "500 Lakh > 50 Lakh → 500 Lakhs > 5 Million. Answer: >."
            )
        },
        "concept_reminder": (
            "Conversion anchors: 1 Million = 10 Lakh; 1 Billion = 100 Crore. "
            "500 Lakhs = 50 Million (not 5 Million). "
            "Always convert both numbers to the same system before comparing."
        )
    },

    {
        "id": "number_systems_kn_q3",
        "challenge": (
            "Set the simulation to explore mode and enter 1,00,00,000 (one crore = 10 million). "
            "This is the key conversion anchor between the two systems. "
            "Observe both the Indian word name (One Crore) and the International word name (Ten Million).\n\n"
            "(1 ಕೋಟಿ = 10 ಮಿಲಿಯನ್ ಎಂದು ತೋರಿಸಿ)"
        ),
        "target_parameters": ["mode", "number"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "explore"},
                {"parameter": "number", "operator": "==", "value": 10000000}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='explore' and number=10000000 (one crore). "
                "Indian: 1,00,00,000. International: 10,000,000. "
                "Indian name: 'One Crore'. International name: 'Ten Million'."
            ),
            "attempt_2": (
                "Choose mode='explore', number=10000000. "
                "This shows the key anchor: 1 Crore = 10 Million = 10,000 Thousand."
            ),
            "attempt_3": (
                "mode='explore', number=10000000. "
                "1 Crore has 8 digits (1 followed by 7 zeros). "
                "In International it is 10 Million — the digit strip clearly shows both comma styles."
            )
        },
        "concept_reminder": (
            "1 Crore (Indian) = 10 Million (International). "
            "1,00,00,000 (Indian notation) = 10,000,000 (International notation). "
            "This is the most important cross-system anchor for Class 6 students."
        )
    }
]


# =============================================================================
# SENSE OF SCALE — QUIZ QUESTIONS
# 3 questions: journey scenario → buses scenario → counting scenario
# =============================================================================
QUIZ_QUESTIONS_MATHS_KN["sense_of_scale_kn"] = [

    {
        "id": "sense_of_scale_kn_q1",
        "challenge": (
            "Open the Journey scenario (scenario 0). Set the speed to 100 km/day and the "
            "duration to 10 years. Observe what fraction of the Earth-Moon distance "
            "(3,84,400 km) you can cover. "
            "How many kilometres does 100 km/day for 10 years give?\n\n"
            "(ಪ್ರಯಾಣ ಸನ್ನಿವೇಶ: 100 km/day × 10 years ಎಷ್ಟು km?)"
        ),
        "target_parameters": ["scenario"],
        "success_rule": {
            "conditions": [
                {"parameter": "scenario", "operator": "==", "value": 0}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set scenario=0 (Journey). Use speed=100 km/day, years=10. "
                "Distance = 100 × 365 × 10 = 3,65,000 km. "
                "Earth-Moon distance = 3,84,400 km. We reach about 94.9%!"
            ),
            "attempt_2": (
                "Select scenario=0. "
                "3,65,000 km is just short of the Moon. "
                "This shows '3.65 lakh' is a real, tangible scale — almost Moon distance."
            ),
            "attempt_3": (
                "Choose scenario=0 to open the Journey tab. "
                "100 km/day × 365 days × 10 years = 3,65,000 km = 3 lakh 65 thousand km. "
                "This gives intuitive meaning to a 6-digit number."
            )
        },
        "concept_reminder": (
            "3,65,000 km ≈ 3.65 lakh km. The Moon is 3,84,400 km away. "
            "Driving 100 km/day for 10 years gets you 95% of the way to the Moon. "
            "This makes '3 lakh' a viscerally understandable quantity."
        )
    },

    {
        "id": "sense_of_scale_kn_q2",
        "challenge": (
            "Open the Buses scenario (scenario 1). Set capacity to 50 passengers per bus "
            "and count to 2,00,000 buses. Compare the total passenger count to the population "
            "of Mumbai (1,24,42,373). Does the bus fleet carry more or fewer people than Mumbai?\n\n"
            "(ಬಸ್ ಸನ್ನಿವೇಶ: 50 × 2,00,000 = ? — ಮುಂಬೈ ಜನಸಂಖ್ಯೆಗಿಂತ ಹೆಚ್ಚೇ?)"
        ),
        "target_parameters": ["scenario"],
        "success_rule": {
            "conditions": [
                {"parameter": "scenario", "operator": "==", "value": 1}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set scenario=1 (Buses). 50 passengers × 2,00,000 buses = 1,00,00,000 people (1 crore). "
                "Mumbai's population = 1,24,42,373 (about 1.24 crore). "
                "Our fleet carries slightly less than Mumbai's population."
            ),
            "attempt_2": (
                "Use scenario=1. "
                "50 × 2,00,000 = 1,00,00,000. Mumbai = 1,24,42,373. "
                "The progress bar for Mumbai shows ~80% — we don't quite reach Mumbai's size."
            ),
            "attempt_3": (
                "Select scenario=1. "
                "To exceed Mumbai (1.24 crore) with 50-passenger buses, you need 50 × 2,49,000 ≈ 1.24 crore. "
                "This shows that '1 crore' and 'Mumbai's population' are in the same magnitude range."
            )
        },
        "concept_reminder": (
            "50 × 2,00,000 = 1,00,00,000 = 1 crore. "
            "Mumbai's population ≈ 1.24 crore. "
            "Multiplying two relatively small numbers (50 and 2 lakh) gives a crore-scale result — "
            "demonstrating why multiplication is a powerful tool for working with large numbers."
        )
    },

    {
        "id": "sense_of_scale_kn_q3",
        "challenge": (
            "Open the Counting scenario (scenario 3). Set the target to 10,00,000 (ten lakh) "
            "items and the counting rate to 1 item per second. How long does it take to count "
            "ten lakh items — is it within one day, one year, or more?\n\n"
            "(ಎಣಿಕೆ ಸನ್ನಿವೇಶ: 10 ಲಕ್ಷ ವಸ್ತುಗಳನ್ನು 1/ಸೆಕೆಂಡ್ ವೇಗದಲ್ಲಿ ಎಣಿಸಲು ಎಷ್ಟು ಸಮಯ?)"
        ),
        "target_parameters": ["scenario"],
        "success_rule": {
            "conditions": [
                {"parameter": "scenario", "operator": "==", "value": 3}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set scenario=3 (Counting). target=1000000, rate=1 item/second. "
                "10,00,000 seconds ÷ 86,400 seconds/day ≈ 11.6 days. "
                "More than one day, less than one month."
            ),
            "attempt_2": (
                "Use scenario=3. "
                "1,00,000 seconds = about 1.16 days. "
                "10,00,000 seconds = about 11.6 days. "
                "The progress bar for '1 day' shows > 100%, meaning counting takes longer than a day."
            ),
            "attempt_3": (
                "Select scenario=3. "
                "10 lakh ÷ (1 per second × 86,400 seconds/day) = 11.57 days. "
                "This shows that 'lakh' is a human-scale number — countable within a lifetime!"
            )
        },
        "concept_reminder": (
            "10,00,000 seconds ≈ 11.6 days at 1 per second. "
            "1 crore seconds ≈ 115 days. "
            "These anchors make lakh and crore viscerally understandable — "
            "they are large but not infinitely large."
        )
    }
]


# =============================================================================
# ROUNDING & ESTIMATION — QUIZ QUESTIONS
# 3 questions: visualise rounding → apply rounding rule → estimation in context
# =============================================================================
QUIZ_QUESTIONS_MATHS_KN["rounding_estimation_kn"] = [

    {
        "id": "rounding_estimation_kn_q1",
        "challenge": (
            "Set the simulation to Explore mode and enter 38,769,957 (3,87,69,957). "
            "Look at all five number lines. For which rounding places does the number round UP, "
            "and for which does it round DOWN?\n\n"
            "(3,87,69,957 ಅನ್ನು ತೋರಿಸಿ ಮತ್ತು ಎಲ್ಲಾ 5 ಪೂರ್ಣಾಂಕನ ಸ್ಥಾನಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ)"
        ),
        "target_parameters": ["mode", "number"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "explore"},
                {"parameter": "number", "operator": "==", "value": 38769957}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='explore' and number=38769957. "
                "Nearest 1000: 957 > 500 → round UP → 3,87,70,000. "
                "Nearest 10000: 9957 > 5000 → round UP → 3,87,70,000 (same here). "
                "Nearest 1 lakh: 69,957 > 50,000 → round UP → 3,88,00,000. "
                "Nearest 10 lakh: 7,69,957 > 5,00,000 → round UP → 3,90,00,000. "
                "Nearest crore (1,00,00,000): 87,69,957 > 50,00,000 → round UP → 4,00,00,000."
            ),
            "attempt_2": (
                "Choose mode='explore', number=38769957. "
                "The red marker on every number line is past the midpoint — so ALL five places round UP for this number."
            ),
            "attempt_3": (
                "Set mode='explore', number=38769957. "
                "All blue snap markers are at the right end of their number lines (100%), confirming all places round up."
            )
        },
        "concept_reminder": (
            "3,87,69,957 rounds UP at every place because: "
            "957 > 500, 9957 > 5000, 69957 > 50000, 769957 > 500000, 8769957 > 5000000. "
            "Rounded to nearest crore = 4,00,00,000 (four crore)."
        )
    },

    {
        "id": "rounding_estimation_kn_q2",
        "challenge": (
            "Switch to Quiz mode. Answer the question: "
            "'What is the nearest crore of 29,05,32,481?' "
            "(Is it 29,00,00,000 or 30,00,00,000?)\n\n"
            "(ರಸಪ್ರಶ್ನೆ ಮೋಡ್: 29,05,32,481 ನ ಹತ್ತಿರದ ಕೋಟಿ ಯಾವುದು?)"
        ),
        "target_parameters": ["mode"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "quiz"}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='quiz'. "
                "29,05,32,481 rounded to nearest crore: look at the ten-lakh digit = 0. "
                "0 < 5 → round DOWN → 29,00,00,000."
            ),
            "attempt_2": (
                "Use mode='quiz'. "
                "29,05,32,481 = 29 crore 5,32,481. "
                "The sub-crore part is 5,32,481 which is less than 50,00,000 (half a crore) → round down. "
                "Nearest crore = 29,00,00,000."
            ),
            "attempt_3": (
                "Select mode='quiz'. "
                "Rule: look at the crore-remainder = 5,32,481. "
                "5,32,481 < 50,00,000 → stay at 29 crore. Answer: 29,00,00,000."
            )
        },
        "concept_reminder": (
            "29,05,32,481 → nearest crore: check if the sub-crore part (5,32,481) ≥ 50,00,000. "
            "5,32,481 < 50,00,000 → round DOWN → 29,00,00,000. "
            "Always compare the remainder to half the rounding unit."
        )
    },

    {
        "id": "rounding_estimation_kn_q3",
        "challenge": (
            "Set explore mode and enter 4631280 (46,31,280) — Bengaluru's 2001 census population. "
            "Observe it rounded to the nearest lakh. Now mentally check: "
            "Bengaluru's 2011 population was 84,43,675. Rounded to the nearest lakh, "
            "did the city roughly double?\n\n"
            "(ಬೆಂಗಳೂರು ಜನಸಂಖ್ಯೆ 2001: 46,31,280 — ಹತ್ತಿರದ ಲಕ್ಷಕ್ಕೆ ಪೂರ್ಣಾಂಕ ಮಾಡಿ)"
        ),
        "target_parameters": ["mode", "number"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "explore"},
                {"parameter": "number", "operator": "==", "value": 4631280}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='explore', number=4631280 (46,31,280). "
                "Nearest lakh: 31,280 < 50,000 → round DOWN → 46,00,000 (46 lakh). "
                "2011 population 84,43,675 → nearest lakh: 43,675 < 50,000 → 84,00,000 (84 lakh). "
                "84 ÷ 46 ≈ 1.83 — almost doubled!"
            ),
            "attempt_2": (
                "Use mode='explore', number=4631280. "
                "46,31,280 rounds to 46 lakh (down, because 31,280 < 50,000). "
                "84,43,675 rounds to 84 lakh (down, because 43,675 < 50,000). "
                "46 × 2 = 92 lakh; actual is 84 lakh — so not quite doubled but very close."
            ),
            "attempt_3": (
                "Set mode='explore', number=4631280 → 46 lakh. "
                "84 lakh ÷ 46 lakh ≈ 1.83. Bengaluru grew by 83% — close to doubling. "
                "Rounding to the nearest lakh is enough precision to answer 'roughly doubled'."
            )
        },
        "concept_reminder": (
            "46,31,280 → nearest lakh = 46,00,000 (31,280 < 50,000 → round down). "
            "84,43,675 → nearest lakh = 84,00,000 (43,675 < 50,000 → round down). "
            "Estimation answer: 84 ÷ 46 ≈ 1.83 — city nearly doubled in one decade."
        )
    }
]


# =============================================================================
# MULTIPLICATION PATTERNS — QUIZ QUESTIONS
# 3 questions: digit-count rule → shortcuts → digit grid
# =============================================================================
QUIZ_QUESTIONS_MATHS_KN["multiplication_patterns_kn"] = [

    {
        "id": "multiplication_patterns_kn_q1",
        "challenge": (
            "Set the simulation to Multiply mode with numA=999 and numB=999. "
            "Before looking at the product, predict: will the result have 5 or 6 digits? "
            "(Use the digit-count rule: 3-digit × 3-digit gives 3+3−1=5 or 3+3=6 digits.) "
            "Then verify by checking the product displayed.\n\n"
            "(ಗುಣಾಕಾರ ಮೋಡ್: 999 × 999 — ಉತ್ಪನ್ನದಲ್ಲಿ ಎಷ್ಟು ಅಂಕಿ?)"
        ),
        "target_parameters": ["mode", "numA", "numB"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "multiply"},
                {"parameter": "numA", "operator": "==", "value": 999},
                {"parameter": "numB", "operator": "==", "value": 999}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='multiply', numA=999, numB=999. "
                "999 × 999 = 998,001 → 6 digits. "
                "Digit-count rule: 3+3=6 (the maximum). "
                "When both numbers have 9 as the leading digit, the product hits the maximum digit count."
            ),
            "attempt_2": (
                "Use mode='multiply', numA=999, numB=999. "
                "Rule: d_a=3, d_b=3 → product has 3+3−1=5 or 3+3=6 digits. "
                "999×999=998,001 is a 6-digit number (maximum). "
                "Compare: 100×100=10,000 (5 digits, minimum). The badge confirms which applies."
            ),
            "attempt_3": (
                "Set mode='multiply', numA=999, numB=999. "
                "The PASS badge shows '3+3−1 ≤ digits(product) ≤ 3+3', i.e., 5 ≤ 6 ≤ 6. "
                "998,001 has exactly 6 digits — the maximum allowed by the rule."
            )
        },
        "concept_reminder": (
            "d_a-digit × d_b-digit → product has d_a+d_b−1 or d_a+d_b digits. "
            "999 (3-digit) × 999 (3-digit) → 5 or 6 digits. Answer: 998,001 has 6 digits. "
            "Minimum case: 100×100=10,000 (5 digits, the minimum). Maximum case: 999×999=998,001 (6 digits)."
        )
    },

    {
        "id": "multiplication_patterns_kn_q2",
        "challenge": (
            "Switch to Shortcuts mode. Study the rule for multiplying by 10 and 100. "
            "Then answer: what is 4,367 × 1,000? "
            "Explain why the answer has three extra zeros compared to 4,367.\n\n"
            "(ಶಾರ್ಟ್‌ಕಟ್ ಮೋಡ್: 4,367 × 1,000 = ? — ಮೂರು ಸೊನ್ನೆ ಸೇರಿಸಲು ಕಾರಣ ಏನು?)"
        ),
        "target_parameters": ["mode"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "shortcuts"}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='shortcuts'. "
                "Rule: multiplying by 10 appends one zero (each digit shifts one place left). "
                "×100 appends two zeros, ×1000 appends three zeros. "
                "4,367 × 1,000 = 43,67,000 (append three zeros → seven digits)."
            ),
            "attempt_2": (
                "Use mode='shortcuts'. "
                "Place-value explanation: 4,367 × 1,000 shifts every digit three places left: "
                "ones become thousands, tens become ten-thousands, etc. "
                "The three vacated places become zeros."
            ),
            "attempt_3": (
                "Select mode='shortcuts'. "
                "4,367 × 1,000 = 4,367,000 = 43,67,000 (Indian notation). "
                "The rule: count the zeros in the multiplier → append that many zeros to the other number."
            )
        },
        "concept_reminder": (
            "Multiplying by 10^n appends n zeros. "
            "4,367 × 1,000 = 43,67,000 (three extra zeros). "
            "This is a direct consequence of place value: each ×10 shifts all digits one position left."
        )
    },

    {
        "id": "multiplication_patterns_kn_q3",
        "challenge": (
            "Open the Digit Grid (digitGrid mode). Find the cell for 4-digit × 4-digit. "
            "What is the range of digit counts possible for such a product? "
            "Verify by checking: 1000 × 1000 (minimum) and 9999 × 9999 (maximum).\n\n"
            "(ಅಂಕಿ ಗ್ರಿಡ್ ಮೋಡ್: 4 ಅಂಕಿ × 4 ಅಂಕಿ ಉತ್ಪನ್ನದಲ್ಲಿ ಎಷ್ಟು ಅಂಕಿ ಇರಬಹುದು?)"
        ),
        "target_parameters": ["mode"],
        "success_rule": {
            "conditions": [
                {"parameter": "mode", "operator": "==", "value": "digitGrid"}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set mode='digitGrid'. "
                "Cell (4d, 4d): range = 4+4−1 to 4+4 = 7 to 8 digits. "
                "Check: 1000×1000=1,000,000 (7 digits ✓). 9999×9999=99,980,001 (8 digits ✓)."
            ),
            "attempt_2": (
                "Use mode='digitGrid'. "
                "The 4d×4d cell shows '7-8'. "
                "Minimum: 10^3 × 10^3 = 10^6 (7 digits). Maximum: (10^4−1)^2 ≈ 10^8 (8 digits)."
            ),
            "attempt_3": (
                "Select mode='digitGrid'. "
                "4-digit × 4-digit always gives either 7 or 8 digit answer. "
                "The grid shows this pattern for all combinations from 1d×1d up to 5d×5d."
            )
        },
        "concept_reminder": (
            "4-digit × 4-digit product has 7 or 8 digits (4+4−1=7 to 4+4=8). "
            "1,000 × 1,000 = 10,00,000 (7 digits, minimum). "
            "9,999 × 9,999 = 9,99,80,001 (8 digits, maximum). "
            "The digit-count rule holds for ALL integer multiplication."
        )
    }
]


# =============================================================================
# EXPRESSION EVALUATOR — QUIZ QUESTIONS
# 3 questions: identify terms → evaluate BODMAS → sum signed terms
# =============================================================================
QUIZ_QUESTIONS_MATHS_KN["expression_evaluator_kn"] = [

    {
        "id": "expression_evaluator_kn_q1",
        "challenge": (
            "Load expression index 1: '39 − 2×6 + 11'. "
            "Before stepping through, count the number of terms. "
            "Hint: terms are separated by + or −. How many terms does this expression have?\n\n"
            "(ಸಮೀಕರಣ index 1 ತೋರಿಸಿ: 39 − 2×6 + 11 ರಲ್ಲಿ ಎಷ್ಟು ಪದಗಳಿವೆ?)"
        ),
        "target_parameters": ["problem"],
        "success_rule": {
            "conditions": [
                {"parameter": "problem", "operator": "==", "value": 1}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set problem=1 to load '39 − 2×6 + 11'. "
                "Terms separated by + or −: term 1 = 39, term 2 = −2×6, term 3 = 11. "
                "Three terms, not five (the × is NOT a term separator — it stays within term 2)."
            ),
            "attempt_2": (
                "Use problem=1. "
                "The three colour-coded boxes show: '39', '−2×6', '11'. "
                "Common mistake: thinking 2 and 6 are separate terms because of ×. "
                "Only + and − between terms separate them."
            ),
            "attempt_3": (
                "Select problem=1. "
                "'39 − 2×6 + 11': the separators are '−' (before 2×6) and '+' (before 11). "
                "So 3 terms: 39, −2×6, +11. Each gets its own coloured term box."
            )
        },
        "concept_reminder": (
            "'39 − 2×6 + 11' has 3 terms: 39, −2×6, and 11. "
            "The × inside '2×6' does NOT create a new term — it is an operation within term 2. "
            "Terms are separated ONLY by + or − between separate parts of the expression."
        )
    },

    {
        "id": "expression_evaluator_kn_q2",
        "challenge": (
            "Load expression index 3: '48 − 10×2 + 16÷2'. "
            "Step through the evaluation cards and compute the final value. "
            "The three terms are: 48, −10×2, and 16÷2. Evaluate each term first, then add.\n\n"
            "(index 3 ತೋರಿಸಿ: 48 − 10×2 + 16÷2 ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ)"
        ),
        "target_parameters": ["problem"],
        "success_rule": {
            "conditions": [
                {"parameter": "problem", "operator": "==", "value": 3}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set problem=3 for '48 − 10×2 + 16÷2'. "
                "Term 1 = 48. Term 2 = −10×2 = −20. Term 3 = 16÷2 = 8. "
                "Sum: 48 + (−20) + 8 = 36."
            ),
            "attempt_2": (
                "Use problem=3. "
                "Step 2: evaluate each term: 48→48, −10×2→−20, 16÷2→8. "
                "Step 3: add all: 48 − 20 + 8 = 36. Final value = 36."
            ),
            "attempt_3": (
                "Select problem=3. "
                "Do NOT compute 48−10 first! Evaluate 10×2=20 inside term 2 before subtracting. "
                "Then: 48 − 20 + 8 = 36."
            )
        },
        "concept_reminder": (
            "'48 − 10×2 + 16÷2': evaluate each term independently first. "
            "Term 2: 10×2=20 → the term is −20. Term 3: 16÷2=8. "
            "Final: 48 − 20 + 8 = 36. BODMAS within each term, then addition of all terms."
        )
    },

    {
        "id": "expression_evaluator_kn_q3",
        "challenge": (
            "Load expression index 4: '6×3 − 4×8×5'. "
            "This expression has a large negative term. Evaluate it step by step: "
            "what is the value of each term, and what is the final sum?\n\n"
            "(index 4: 6×3 − 4×8×5 — ಋಣ ಪದ ಸಹಿತ ಮೌಲ್ಯಮಾಪನ)"
        ),
        "target_parameters": ["problem"],
        "success_rule": {
            "conditions": [
                {"parameter": "problem", "operator": "==", "value": 4}
            ],
            "scoring": {"perfect": 1.0, "partial": 0.5, "wrong": 0.2}
        },
        "hints": {
            "attempt_1": (
                "Set problem=4 for '6×3 − 4×8×5'. "
                "Term 1 = 6×3 = 18. Term 2 = −4×8×5 = −160. "
                "Sum: 18 + (−160) = −142. The result is NEGATIVE."
            ),
            "attempt_2": (
                "Use problem=4. "
                "4×8×5 = 4×40 = 160. The term is negative: −160. "
                "18 − 160 = −142. The negative term dominates completely."
            ),
            "attempt_3": (
                "Select problem=4. "
                "Step 1: two terms (6×3 and −4×8×5). "
                "Step 2: 6×3=18; 4×8×5=160 so second term = −160. "
                "Step 3: 18 + (−160) = −142."
            )
        },
        "concept_reminder": (
            "'6×3 − 4×8×5' evaluates to −142. "
            "Term 1 = 6×3 = 18 (positive). Term 2 = 4×8×5 = 160 (negative because of the '−'). "
            "Sum = 18 − 160 = −142. "
            "Expressions CAN have negative final values when a large negative term dominates."
        )
    }
]


# ═══════════════════════════════════════════════════════════════════════
# HELPER: list of Kannada-Maths simulation IDs for sidebar grouping
# ═══════════════════════════════════════════════════════════════════════

MATHS_KN_SIMULATION_IDS = list(SIMULATIONS_MATHS_KN.keys())
