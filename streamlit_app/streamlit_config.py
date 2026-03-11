"""
Streamlit App Configuration
===========================
Centralized configuration for simulations and app settings.
Easy to add new simulations here.
"""

# =============================================================================
# GITHUB PAGES BASE URL
# =============================================================================
GITHUB_PAGES_BASE = "https://imhv0609.github.io/simulation_to_concept_version3_github_modified/simulations"

# =============================================================================
# SIMULATION CONFIGURATIONS
# =============================================================================
# Each simulation has:
# - name: Display name
# - base_url: GitHub Pages URL
# - parameters: List of parameter configs with name, default, min, max
# - url_param_names: How params are named in the URL (may differ from internal names)

SIMULATIONS = {
    "simple_pendulum": {
        "name": "Time & Pendulums",
        "description": "Explore how pendulum length affects time period",
        "base_url": f"{GITHUB_PAGES_BASE}/simple_pendulum.html",
        "parameters": [
            {
                "name": "length",
                "display_name": "Pendulum Length",
                "default": 5,
                "min": 1,
                "max": 10,
                "unit": "units",
                "url_param": "length"
            },
            {
                "name": "number_of_oscillations",
                "display_name": "Number of Oscillations",
                "default": 10,
                "min": 5,
                "max": 50,
                "unit": "count",
                "url_param": "oscillations"
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Time & Pendulums"
    },
    
    "earth_rotation_revolution": {
        "name": "Earth's Rotation & Revolution",
        "description": "Explore day/night cycles, seasons, and axial tilt",
        "base_url": f"{GITHUB_PAGES_BASE}/rotAndRev.html",
        "parameters": [
            {
                "name": "rotationSpeed",
                "display_name": "Rotation Speed",
                "default": 50,
                "min": 0,
                "max": 100,
                "unit": "%",
                "url_param": "rotationSpeed"
            },
            {
                "name": "axialTilt",
                "display_name": "Axial Tilt",
                "default": 23.5,
                "min": 0,
                "max": 30,
                "unit": "°",
                "url_param": "axialTilt"
            },
            {
                "name": "revolutionSpeed",
                "display_name": "Revolution Speed",
                "default": 50,
                "min": 0,
                "max": 100,
                "unit": "%",
                "url_param": "revolutionSpeed"
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Earth's Rotation & Revolution"
    },
    
    "light_shadows": {
        "name": "Light & Shadows",
        "description": "Explore how light creates shadows and shadow properties",
        "base_url": f"{GITHUB_PAGES_BASE}/lightsShadows.html",
        "parameters": [
            {
                "name": "lightDistance",
                "display_name": "Light Distance",
                "default": 5,
                "min": 1,
                "max": 10,
                "unit": "units",
                "url_param": "lightDistance"
            },
            {
                "name": "objectType",
                "display_name": "Object Type",
                "default": "Opaque",
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "objectType",
                "options": ["Opaque", "Translucent", "Transparent"]
            },
            {
                "name": "objectSize",
                "display_name": "Object Size",
                "default": 5,
                "min": 1,
                "max": 10,
                "unit": "units",
                "url_param": "objectSize"
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Light & Shadows"
    },
    
    "angle_sum_property": {
        "name": "Triangle Angle Sum",
        "description": "Explore how triangle interior angles always sum to 180°",
        "base_url": f"{GITHUB_PAGES_BASE}/AngleSumProperty.html",
        "parameters": [
            {
                "name": "vertexA_y",
                "display_name": "Top Vertex (A) Height",
                "default": 150,
                "min": 50,
                "max": 550,
                "unit": "pixels",
                "url_param": "vertexA_y"
            },
            {
                "name": "vertexB_x",
                "display_name": "Left Vertex (B) Position",
                "default": 200,
                "min": 50,
                "max": 950,
                "unit": "pixels",
                "url_param": "vertexB_x"
            },
            {
                "name": "vertexC_x",
                "display_name": "Right Vertex (C) Position",
                "default": 800,
                "min": 50,
                "max": 950,
                "unit": "pixels",
                "url_param": "vertexC_x"
            },
            {
                "name": "show_proof_lines",
                "display_name": "Show Geometric Proof",
                "default": False,
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "show_proof_lines",
                "options": [True, False]
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Triangle Angle Sum"
    },
    
    "parallel_lines_angles": {
        "name": "Parallel Lines & Transversal",
        "description": "Explore angle relationships when a transversal crosses parallel lines",
        "base_url": f"{GITHUB_PAGES_BASE}/parallel-angles-interactive.html",
        "parameters": [
            {
                "name": "angle",
                "display_name": "Transversal Angle",
                "default": 60,
                "min": 20,
                "max": 160,
                "unit": "degrees",
                "url_param": "angle"
            },
            {
                "name": "phase",
                "display_name": "Phase",
                "default": "explore",
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "phase",
                "options": ["explore", "quiz"]
            },
            {
                "name": "highlightPair",
                "display_name": "Highlight Angle Pair",
                "default": None,
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "highlightPair",
                "options": [None, "1-5", "2-6", "3-7", "4-8", "3-5", "4-6", "3-6", "4-5"]
            },
            {
                "name": "showRelationships",
                "display_name": "Show Relationships",
                "default": True,
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "showRelationships",
                "options": [True, False]
            },
            {
                "name": "lockAngle",
                "display_name": "Lock Angle",
                "default": False,
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "lockAngle",
                "options": [True, False]
            }
        ],
        "auto_start_param": None,
        "topic": "Parallel Lines & Transversal"
    },
    
    "angle_sum_interactive": {
        "name": "Interactive Triangle Angles",
        "description": "Adjust angles to reshape triangle and see they always sum to 180°",
        "base_url": f"{GITHUB_PAGES_BASE}/angle-sum-property.html",
        "parameters": [
            {
                "name": "angleA",
                "display_name": "Angle A (Red)",
                "default": 60,
                "min": 10,
                "max": 170,
                "unit": "degrees",
                "url_param": "angleA"
            },
            {
                "name": "angleB",
                "display_name": "Angle B (Blue)",
                "default": 60,
                "min": 10,
                "max": 170,
                "unit": "degrees",
                "url_param": "angleB"
            },
            {
                "name": "angleC",
                "display_name": "Angle C (Green)",
                "default": 60,
                "min": 10,
                "max": 170,
                "unit": "degrees",
                "url_param": "angleC"
            },
            {
                "name": "autoInteract",
                "display_name": "Show Discovery Message",
                "default": False,
                "min": None,
                "max": None,
                "unit": "",
                "url_param": "autoInteract",
                "options": [True, False]
            }
        ],
        "auto_start_param": None,
        "topic": "Interactive Triangle Angles"
    },
    
    "speed_race": {
        "name": "Speed, Distance & Time Race",
        "description": "Race simulation comparing speeds of walker, cyclist, car, and train",
        "base_url": f"{GITHUB_PAGES_BASE}/simulation_7_speed_race.html",
        "parameters": [
            {
                "name": "speedWalker",
                "display_name": "Walker Speed",
                "default": 5,
                "min": 1,
                "max": 10,
                "unit": "km/h",
                "url_param": "speedWalker"
            },
            {
                "name": "speedCyclist",
                "display_name": "Cyclist Speed",
                "default": 20,
                "min": 5,
                "max": 40,
                "unit": "km/h",
                "url_param": "speedCyclist"
            },
            {
                "name": "speedCar",
                "display_name": "Car Speed",
                "default": 60,
                "min": 20,
                "max": 120,
                "unit": "km/h",
                "url_param": "speedCar"
            },
            {
                "name": "speedTrain",
                "display_name": "Train Speed",
                "default": 100,
                "min": 50,
                "max": 200,
                "unit": "km/h",
                "url_param": "speedTrain"
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Speed, Distance & Time"
    },
    
    "time_units": {
        "name": "Time Units Converter",
        "description": "Convert between different units of time (hours, minutes, seconds, milliseconds)",
        "base_url": f"{GITHUB_PAGES_BASE}/simulation_5_time_units.html",
        "parameters": [
            {
                "name": "timeValue",
                "display_name": "Time Value",
                "default": 1,
                "min": 0.1,
                "max": 100,
                "unit": "",
                "url_param": "timeValue"
            },
            {
                "name": "timeUnit",
                "display_name": "Time Unit",
                "default": "s",
                "options": ["h", "min", "s", "ms"],
                "option_labels": ["hours (h)", "minutes (min)", "seconds (s)", "milliseconds (ms)"],
                "url_param": "timeUnit"
            }
        ],
        "auto_start_param": None,
        "topic": "Time Units & SI Standards"
    },
    
    "speed_calculator": {
        "name": "Speed Calculator",
        "description": "Calculate speed, distance, or time using the speed formula",
        "base_url": f"{GITHUB_PAGES_BASE}/simulation_6_speed_calculator.html",
        "parameters": [
            {
                "name": "calculationMode",
                "display_name": "Calculation Mode",
                "default": "speed",
                "options": ["speed", "distance", "time"],
                "option_labels": ["Find Speed", "Find Distance", "Find Time"],
                "url_param": "calculationMode"
            },
            {
                "name": "distance",
                "display_name": "Distance (km)",
                "default": 100,
                "min": 1,
                "max": 1000,
                "unit": "km",
                "url_param": "distance"
            },
            {
                "name": "time",
                "display_name": "Time (hours)",
                "default": 2,
                "min": 0.1,
                "max": 100,
                "unit": "h",
                "url_param": "time"
            },
            {
                "name": "speed",
                "display_name": "Speed (km/h)",
                "default": 50,
                "min": 1,
                "max": 1000,
                "unit": "km/h",
                "url_param": "speed"
            }
        ],
        "auto_start_param": None,
        "topic": "Speed, Distance & Time Relationships"
    },
    
    "simple_pendulum_new": {
        "name": "Simple Pendulum Interactive",
        "description": "Explore how length and mass affect pendulum oscillations. Discover why time period depends only on length!",
        "base_url": f"{GITHUB_PAGES_BASE}/simulation_3_pendulum.html",
        "parameters": [
            {
                "name": "length",
                "type": "slider",
                "display_name": "String Length (cm)",
                "default": 100,
                "min": 50,
                "max": 200,
                "unit": "cm",
                "url_param": "length"
            },
            {
                "name": "mass",
                "type": "slider",
                "display_name": "Bob Mass (g)",
                "default": 100,
                "min": 50,
                "max": 200,
                "unit": "g",
                "url_param": "mass"
            }
        ],
        "auto_start_param": "autoStart",
        "topic": "Oscillatory Motion & Time Period"
    },
    
    "brackets_signs": {
        "name": "Brackets & Sign Rules",
        "description": "Learn when to flip signs and when to keep them when removing brackets in algebra",
        "base_url": f"{GITHUB_PAGES_BASE}/ch2_sim2_brackets_signs.html",
        "parameters": [
            {
                "name": "mode",
                "type": "select",
                "display_name": "Mode",
                "default": "learn",
                "options": ["learn", "quiz"],
                "option_labels": ["Learn (Examples)", "Quiz (Test Yourself)"],
                "url_param": "mode"
            },
            {
                "name": "problemIndex",
                "type": "slider",
                "display_name": "Example Number",
                "default": 0,
                "min": 0,
                "max": 9,
                "unit": "",
                "url_param": "problemIndex"
            }
        ],
        "auto_start_param": None,
        "topic": "Algebra - Brackets & Sign Rules"
    },
    
    "distributive": {
        "name": "Distributive Property",
        "description": "Understand a × (b + c) = a × b + a × c through dot arrays, area models, and mental math",
        "base_url": f"{GITHUB_PAGES_BASE}/ch2_sim3_distributive.html",
        "parameters": [
            {
                "name": "mode",
                "type": "select",
                "display_name": "Visualization Mode",
                "default": "dots",
                "options": ["dots", "area", "mental", "quiz"],
                "option_labels": ["Dot Array", "Area Model", "Mental Math", "Quiz"],
                "url_param": "mode"
            },
            {
                "name": "a",
                "type": "slider",
                "display_name": "a (rows/multiplier)",
                "default": 3,
                "min": 1,
                "max": 8,
                "unit": "",
                "url_param": "a"
            },
            {
                "name": "b",
                "type": "slider",
                "display_name": "b (blue columns/first addend)",
                "default": 4,
                "min": 1,
                "max": 10,
                "unit": "",
                "url_param": "b"
            },
            {
                "name": "c",
                "type": "slider",
                "display_name": "c (green columns/second addend)",
                "default": 6,
                "min": 1,
                "max": 10,
                "unit": "",
                "url_param": "c"
            },
            {
                "name": "mentalMathIndex",
                "type": "slider",
                "display_name": "Mental Math Example",
                "default": 0,
                "min": 0,
                "max": 4,
                "unit": "",
                "url_param": "mentalMathIndex"
            },
            {
                "name": "quizIndex",
                "type": "slider",
                "display_name": "Quiz Question",
                "default": 0,
                "min": 0,
                "max": 9,
                "unit": "",
                "url_param": "quizIndex"
            }
        ],
        "auto_start_param": None,
        "topic": "Algebra - Distributive Property"
    }
}

# =============================================================================
# KANNADA SIMULATIONS
# ಕನ್ನಡ ಸಿಮ್ಯುಲೇಷನ್‌ಗಳು
# =============================================================================
# GitHub Pages base URL for the Kannada simulations folder
GITHUB_PAGES_BASE_KN = (
    "https://imhv0609.github.io/simulation_to_concept_version3_github_modified"
    "/simulations_kannada"
)

# Each Kannada simulation is added directly to the SIMULATIONS dict so that
# build_simulation_url() and get_default_params() work without modification.
# A "language": "kannada" field is added so the sidebar can group them.

SIMULATIONS["industrial_waste_treatment_kn"] = {
    "name": "ಕೈಗಾರಿಕಾ ತ್ಯಾಜ್ಯ ಚಿಕಿತ್ಸೆ (Industrial Waste Treatment)",
    "language": "kannada",
    "description": (
        "ತಟಸ್ಥೀಕರಣ ವಿಧಾನದ ಮೂಲಕ ಕೈಗಾರಿಕಾ ತ್ಯಾಜ್ಯ ನಿರ್ವಹಣೆ ಅಧ್ಯಯನ ಮಾಡಿ.\n"
        "Explore neutralisation of acidic industrial waste to protect river ecosystems."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation10_industrial_waste_treatment_kn.html"
    ),
    # ── Parameter definitions ────────────────────────────────────────────────
    # initialState : dropdown — controls which demonstration state auto-loads
    # showHints    : checkbox — shows/hides the insight explanation box
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Simulation State / ಸಿಮ್ಯುಲೇಷನ್ ಸ್ಥಿತಿ",
            "default": "initial",
            # options list is used by Streamlit quiz UI to build a dropdown
            "options": ["initial", "polluted", "treated"],
            "option_labels": [
                "ಪ್ರಾರಂಭ (Initial — clean river)",
                "ಮಾಲಿನ್ಯ (Polluted — untreated waste)",
                "ಚಿಕಿತ್ಸೆ (Treated — neutralised waste)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            # bool options → Streamlit checkbox
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# TURMERIC INDICATOR SIMULATION (Kannada)
# ಹಲ್ದಿ ಸೂಚಕ – ಭಾಗಶಃ ಸೂಚಕ (ಕ್ಷಾರ ಮಾತ್ರ ಕೆಂಪಾಗಿಸುತ್ತದೆ)
# =============================================================================
SIMULATIONS["turmeric_indicator_kn"] = {
    "name": "ಹಲ್ದಿ ಸೂಚಕ (Turmeric Indicator)",
    "language": "kannada",
    "description": (
        "ಹಲ್ದಿ ಕಾಗದ ಬಳಸಿ ದ್ರಾವಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ — ಕ್ಷಾರ ಮಾತ್ರ ಕೆಂಪು-ಕಂದು ಬಣ್ಣ ನೀಡುತ್ತದೆ.\n"
        "Test solutions with turmeric paper — only bases turn it red/brown (partial indicator)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation5_turmeric_indicator_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದ್ರಾವಣದ ಪ್ರಕಾರ / Solution Type",
            "default": "basic",
            "options": ["acidic", "basic", "neutral"],
            "option_labels": [
                "ಆಮ್ಲ (Acidic — lemon juice, stays yellow)",
                "ಕ್ಷಾರ (Basic — soap, turns red/brown)",
                "ತಟಸ್ಥ (Neutral — tap water, stays yellow)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# RED ROSE INDICATOR SIMULATION (Kannada)
# ಕೆಂಪು ಗುಲಾಬಿ ಸೂಚಕ – ಪೂರ್ಣ ಸೂಚಕ (ಕೆಂಪು/ಹಸಿರು/ಗುಲಾಬಿ ಬಣ್ಣ)
# =============================================================================
SIMULATIONS["red_rose_indicator_kn"] = {
    "name": "ಕೆಂಪು ಗುಲಾಬಿ ಸೂಚಕ (Red Rose Indicator)",
    "language": "kannada",
    "description": (
        "ಗುಲಾಬಿ ಸಾರ ಬಳಸಿ ದ್ರಾವಣ ಪರೀಕ್ಷಿಸಿ — ಕೆಂಪು=ಆಮ್ಲ, ಹಸಿರು=ಕ್ಷಾರ, ಗುಲಾಬಿ=ತಟಸ್ಥ.\n"
        "Test solutions with rose petal extract — red=acid, green=base, pink=neutral (complete indicator)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation4_red_rose_indicator_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದ್ರಾವಣದ ಪ್ರಕಾರ / Solution Type",
            "default": "acidic",
            "options": ["acidic", "basic", "neutral"],
            "option_labels": [
                "ಆಮ್ಲ (Acidic — lemon juice, turns red)",
                "ಕ್ಷಾರ (Basic — soap, turns green)",
                "ತಟಸ್ಥ (Neutral — tap water, stays pink)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# PROPERTIES OF ACIDS AND BASES SIMULATION (Kannada)
# ಆಮ್ಲ ಮತ್ತು ಕ್ಷಾರ ಗುಣಗಳ ಹೋಲಿಕೆ
# =============================================================================
SIMULATIONS["properties_acids_bases_kn"] = {
    "name": "ಆಮ್ಲ ಮತ್ತು ಕ್ಷಾರ ಗುಣಗಳು (Properties of Acids & Bases)",
    "language": "kannada",
    "description": (
        "ಆಮ್ಲ ಮತ್ತು ಕ್ಷಾರ ಗುಣಗಳನ್ನು ಟ್ಯಾಬ್ ಮೂಲಕ ಹೋಲಿಸಿ — ರುಚಿ, ಸ್ಪರ್ಶ, ಲಿಟ್ಮಸ್ ಕ್ರಿಯೆ.\n"
        "Compare acid vs base properties using tabs — taste, touch, litmus reaction, examples."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation3_properties_acids_bases_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ಯಾನಲ್ ಆಯ್ಕೆ / Panel Selection",
            "default": "initial",
            "options": ["initial", "acids", "bases"],
            "option_labels": [
                "ಪ್ರಾರಂಭ (Initial — acids tab default)",
                "ಆಮ್ಲ (Acids — sour, blue litmus → red)",
                "ಕ್ಷಾರ (Bases — bitter/slippery, red litmus → blue)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# LITMUS INDICATOR SIMULATION (Kannada)
# ಲಿಟ್ಮಸ್ ಕಾಗದ ಪರೀಕ್ಷೆ – ಶಾಸ್ತ್ರೀಯ ಪೂರ್ಣ ಸೂಚಕ
# =============================================================================
SIMULATIONS["litmus_indicator_kn"] = {
    "name": "ಲಿಟ್ಮಸ್ ಕಾಗದ ಪರೀಕ್ಷೆ (Litmus Paper Test)",
    "language": "kannada",
    "description": (
        "ಲಿಟ್ಮಸ್ ಕಾಗದ ಮುಳುಗಿಸಿ ಪರೀಕ್ಷಿಸಿ — ನೀಲಿ→ಕೆಂಪು=ಆಮ್ಲ, ಕೆಂಪು→ನೀಲಿ=ಕ್ಷಾರ, ಬದಲಾವಣೆ ಇಲ್ಲ=ತಟಸ್ಥ.\n"
        "Dip litmus papers — blue→red=acid, red→blue=base, no change=neutral (complete indicator)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation2_litmus_indicator_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದ್ರಾವಣದ ಪ್ರಕಾರ / Solution Type",
            "default": "acidic",
            "options": ["acidic", "basic", "neutral"],
            "option_labels": [
                "ಆಮ್ಲ (Acidic — lemon juice, blue→red)",
                "ಕ್ಷಾರ (Basic — soap, red→blue)",
                "ತಟಸ್ಥ (Neutral — tap water, no change)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# HIDDEN MESSAGE SIMULATION (Kannada)
# ಗುಪ್ತ ಸಂದೇಶ ಬಹಿರಂಗ – ಸೂಚಕ ಪರಿಚಯ
# =============================================================================
SIMULATIONS["hidden_message_kn"] = {
    "name": "ಗುಪ್ತ ಸಂದೇಶ ಬಹಿರಂಗ (Hidden Message Reveal)",
    "language": "kannada",
    "description": (
        "ಸೂಚಕ ಸಿಂಪಡಿಸಿ ಅದೃಶ್ಯ ಸಂದೇಶ ಬಹಿರಂಗ ಮಾಡಿ — ಕ್ಷಾರ ಶಾಯಿ + ಸೂಚಕ = ಬಣ್ಣ ಬದಲಾವಣೆ.\n"
        "Spray indicator to reveal hidden base ink message — introduction to indicator chemistry."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation1_hidden_message_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಬಹಿರಂಗ ಸ್ಥಿತಿ / Reveal State",
            "default": "hidden",
            "options": ["hidden", "revealing", "revealed"],
            "option_labels": [
                "ಅದೃಶ್ಯ (Hidden — blank paper, 0 sprays)",
                "ಬಹಿರಂಗಗೊಳ್ಳುತ್ತಿದೆ (Revealing — 1 spray, partial)",
                "ಬಹಿರಂಗ (Revealed — 3 sprays, fully visible)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# OLFACTORY INDICATOR SIMULATION (Kannada)
# ಘ್ರಾಣ ಸೂಚಕ – ಈರುಳ್ಳಿ ವಾಸನೆಯಿಂದ ಆಮ್ಲ/ಕ್ಷಾರ ಗುರುತಿಸಿ
# =============================================================================
SIMULATIONS["olfactory_indicator_kn"] = {
    "name": "ಘ್ರಾಣ ಸೂಚಕ (Olfactory Indicator)",
    "language": "kannada",
    "description": (
        "ಈರುಳ್ಳಿ ಬಳಸಿ ಆಮ್ಲ/ಕ್ಷಾರ ಗುರುತಿಸಿ — ಆಮ್ಲ: ವಾಸನೆ ಉಳಿಯುತ್ತದೆ, ಕ್ಷಾರ: ಅದೃಶ್ಯ.\n"
        "Test with cut onion — acid keeps the smell, base neutralises it (olfactory indicator)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation6_olfactory_indicator_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದ್ರಾವಣದ ಪ್ರಕಾರ / Solution Type",
            "default": "basic",
            "options": ["acidic", "basic"],
            "option_labels": [
                "ಆಮ್ಲ (Acidic — tamarind, smell stays)",
                "ಕ್ಷಾರ (Basic — baking soda, smell disappears)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# NEUTRALISATION REACTION SIMULATION (Kannada)
# ತಟಸ್ಥೀಕರಣ ಪ್ರತಿಕ್ರಿಯೆ – ಆಮ್ಲ + ಕ್ಷಾರ = ಉಪ್ಪು + ನೀರು
# =============================================================================
SIMULATIONS["neutralisation_reaction_kn"] = {
    "name": "ತಟಸ್ಥೀಕರಣ ಪ್ರತಿಕ್ರಿಯೆ (Neutralisation Reaction)",
    "language": "kannada",
    "description": (
        "ಆಮ್ಲ-ಕ್ಷಾರ ಅನುಪಾತ ಸರಿಹೊಂದಿಸಿ pH ಬದಲಾವಣೆ ಗಮನಿಸಿ — pH 7 ತಟಸ್ಥ ಸ್ಥಿತಿ.\n"
        "Adjust acid-base ratio with slider and observe pH — perfect mix gives pH 7 (salt + water + heat)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation7_neutralisation_reaction_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರತಿಕ್ರಿಯೆ ಫಲಿತಾಂಶ / Reaction Outcome",
            "default": "neutral",
            "options": ["acidic", "neutral", "basic"],
            "option_labels": [
                "ಆಮ್ಲೀಯ (Acidic — excess acid, pH ~3)",
                "ತಟಸ್ಥ (Neutral — equal parts, pH 7)",
                "ಕ್ಷಾರೀಯ (Basic — excess base, pH ~11)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# ANT BITE TREATMENT SIMULATION (Kannada)
# ಇರುವೆ ಕಚ್ಚುವಿಕೆ ಚಿಕಿತ್ಸೆ – ದೈನಂದಿನ ತಟಸ್ಥೀಕರಣ
# =============================================================================
SIMULATIONS["ant_bite_treatment_kn"] = {
    "name": "ಇರುವೆ ಕಚ್ಚುವಿಕೆ ಚಿಕಿತ್ಸೆ (Ant Bite Treatment)",
    "language": "kannada",
    "description": (
        "ಇರುವೆ ಫಾರ್ಮಿಕ್ ಆಮ್ಲ ಚುಚ್ಚುತ್ತದೆ — ಬೇಕಿಂಗ್ ಸೋಡಾ ತಟಸ್ಥೀಕರಣ ನೋವು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.\n"
        "Ant injects formic acid — baking soda (base) neutralises it, relieving pain and redness."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation8_ant_bite_treatment_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಸ್ಥಿತಿ / Scenario State",
            "default": "normal",
            "options": ["normal", "bitten", "treated"],
            "option_labels": [
                "ಸಾಮಾನ್ಯ (Normal — healthy skin, no bite)",
                "ಕಚ್ಚಿದ (Bitten — formic acid injected, pain)",
                "ಚಿಕಿತ್ಸೆ (Treated — baking soda applied, relief)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಸೂಚನೆಗಳನ್ನು ತೋರಿಸಿ (Show Hints)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# SOIL TREATMENT SIMULATION (Kannada)
# ಮಣ್ಣಿನ ಚಿಕಿತ್ಸೆ – ಕೃಷಿಯಲ್ಲಿ ತಟಸ್ಥೀಕರಣ
# =============================================================================
SIMULATIONS["soil_treatment_kn"] = {
    "name": "ಮಣ್ಣಿನ ಚಿಕಿತ್ಸೆ (Soil Treatment — Agriculture)",
    "language": "kannada",
    "description": (
        "ಆಮ್ಲ/ಕ್ಷಾರ ಮಣ್ಣಿಗೆ ಸರಿಯಾದ ಚಿಕಿತ್ಸೆ ಆರಿಸಿ — ಸಸ್ಯ ಚೇತರಿಸಿ pH 7 ಆಗಲಿ.\n"
        "Select acidic or alkaline soil and apply the correct treatment — plant recovers to pH 7."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter2_simulation9_soil_treatment_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಮಣ್ಣಿನ ಸ್ಥಿತಿ / Soil Scenario",
            "default": "acidic",
            "options": ["acidic", "basic", "treated"],
            "option_labels": [
                "ಆಮ್ಲೀಯ (Acidic soil — pH 4-5, lime needed)",
                "ಕ್ಷಾರೀಯ (Alkaline soil — pH 9-10, compost needed)",
                "ಚಿಕಿತ್ಸೆ (Treated — lime applied, pH 7, plant healthy)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Acids, Bases and Salts (ಆಮ್ಲಗಳು, ಕ್ಷಾರಗಳು ಮತ್ತು ಲವಣಗಳು)"
}


# =============================================================================
# CONDUCTORS AND INSULATORS SIMULATION (Kannada — Chapter 3)
# ವಾಹಕಗಳು ಮತ್ತು ಅವಾಹಕಗಳು – ವಿದ್ಯುತ್ ಪರೀಕ್ಷೆ
# =============================================================================
SIMULATIONS["conductors_insulators_kn"] = {
    "name": "ವಾಹಕ ಮತ್ತು ಅವಾಹಕ (Conductors and Insulators)",
    "language": "kannada",
    "description": (
        "8 ವಸ್ತುಗಳನ್ನು ಸರ್ಕ್ಯೂಟ್‌ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ — ಬಲ್ಬ್ ಬೆಳಗಿದರೆ ವಾಹಕ, ಇಲ್ಲದಿದ್ದರೆ ಅವಾಹಕ.\n"
        "Test 8 materials in a virtual circuit — bulb ON = conductor (metal), OFF = insulator (plastic/rubber)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation10_conductors_insulators_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪರೀಕ್ಷಾ ಪದಾರ್ಥ / Test Material",
            "default": "conductor",
            "options": ["conductor", "insulator"],
            "option_labels": [
                "ವಾಹಕ (Conductor — metal spoon, bulb lights up)",
                "ಅವಾಹಕ (Insulator — plastic scale, bulb stays off)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}

SIMULATIONS["electricity_uses_kn"] = {
    "name": "ವಿದ್ಯುತ್ ಬಳಕೆಗಳು (Electricity Uses)",
    "language": "kannada",
    "description": (
        "12 ವಿದ್ಯುತ್ ಉಪಕರಣಗಳನ್ನು 6 ವರ್ಗಗಳಿಗೆ ವರ್ಗೀಕರಿಸಿ — ಅಡುಗೆ, ಬೆಳಕು, ತಂಪು, ಸಂವಹನ, ಮನರಂಜನೆ, ಸಾರಿಗೆ.\n"
        "Classify 12 electrical appliances into 6 categories to understand how electricity powers daily life."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation1_electricity_uses_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಆರಂಭಿಕ ವರ್ಗ / Starting Category",
            "default": "cooking",
            "options": ["cooking", "lighting", "cooling", "communication", "entertainment", "transport"],
            "option_labels": [
                "ಅಡುಗೆ (Cooking)",
                "ಬೆಳಕು (Lighting)",
                "ತಂಪು/ಬಿಸಿ (Cooling/Heating)",
                "ಸಂವಹನ (Communication)",
                "ಮನರಂಜನೆ (Entertainment)",
                "ಸಾರಿಗೆ (Transport)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}

SIMULATIONS["electricity_sources_kn"] = {
    "name": "ವಿದ್ಯುತ್ ಮೂಲಗಳು (Electricity Sources)",
    "language": "kannada",
    "description": (
        "ಜಲ, ಸೌರ, ಗಾಳಿ ಮತ್ತು ಉಷ್ಣ ವಿದ್ಯುತ್ ಉತ್ಪಾದನಾ ಮೂಲಗಳ ದೃಶ್ಯ ಅನ್ವೇಷಣೆ.\n"
        "Explore hydro, solar, wind and thermal power generation and transmission to homes."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation2_electricity_sources_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ವಿದ್ಯುತ್ ಮೂಲ / Power Source",
            "default": "hydro",
            "options": ["hydro", "solar", "wind", "thermal"],
            "option_labels": [
                "ಜಲವಿದ್ಯುತ್ (Hydro — dam & turbine)",
                "ಸೌರ (Solar — panels & sunlight)",
                "ಗಾಳಿ (Wind — turbine blades)",
                "ಉಷ್ಣ (Thermal — coal/fossil fuel)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}

SIMULATIONS["torch_components_kn"] = {
    "name": "ಟಾರ್ಚ್ ಒಳಭಾಗ (Torch Components)",
    "language": "kannada",
    "description": (
        "ಟಾರ್ಚ್‌ನ ಮೂರು ಮುಖ್ಯ ಭಾಗಗಳನ್ನು (ಕೋಶ, ದೀಪ, ಸ್ವಿಚ್) ಅನ್ವೇಷಿಸಿ.\n"
        "Explore the 3 components of a torch — cells, bulb, switch — and learn how a simple circuit works."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation3_torch_components_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ನೋಟ ಸ್ಥಿತಿ / View Mode",
            "default": "assembled",
            "options": ["assembled", "exploded", "on"],
            "option_labels": [
                "ಜೋಡಿಸಿದ ಟಾರ್ಚ್ (Assembled — normal view)",
                "ಒಳ ನೋಟ (Exploded — see all components)",
                "ಆನ್ ಸ್ಥಿತಿ (ON — switch turned on, bulb glowing)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}

SIMULATIONS["electric_cell_kn"] = {
    "name": "ವಿದ್ಯುತ್ ಕೋಶ (Electric Cell)",
    "language": "kannada",
    "description": (
        "ವಿದ್ಯುತ್ ಕೋಶದ ಧನ (+) ಮತ್ತು ಋಣ (−) ಟರ್ಮಿನಲ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ ಮತ್ತು ಸರ್ಕ್ಯೂಟ್ ಚಿಹ್ನೆ ಕಲಿಯಿರಿ.\n"
        "Explore the positive and negative terminals of an electric cell and learn the circuit symbol."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation4_electric_cell_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಟರ್ಮಿನಲ್ / Terminal",
            "default": "positive",
            "options": ["positive", "negative", "circuit"],
            "option_labels": [
                "ಧನ ಟರ್ಮಿನಲ್ + (Positive — metal cap highlighted)",
                "ಋಣ ಟರ್ಮಿನಲ್ − (Negative — flat disc highlighted)",
                "ಸರ್ಕ್ಯೂಟ್ ದೃಶ್ಯ (Circuit — current flow shown)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}

SIMULATIONS["battery_connection_kn"] = {
    "name": "ಬ್ಯಾಟರಿ ಜೋಡಣೆ (Battery Connection)",
    "language": "kannada",
    "description": (
        "1, 2 ಮತ್ತು 3 ಕೋಶಗಳನ್ನು ಸರಣಿಯಲ್ಲಿ ಜೋಡಿಸಿ — ಹೆಚ್ಚು ಕೋಶ = ಹೆಚ್ಚು ವೋಲ್ಟೇಜ್ = ಹೆಚ್ಚು ಬೆಳಕು.\n"
        "Connect 1, 2 or 3 cells in series — observe voltage addition and increasing bulb brightness."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation5_battery_connection_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಕೋಶಗಳ ಸಂಖ್ಯೆ / Number of Cells",
            "default": "one_cell",
            "options": ["one_cell", "two_cells", "three_cells"],
            "option_labels": [
                "1 ಕೋಶ (One Cell — 1.5V, dim bulb)",
                "2 ಕೋಶಗಳು (Two Cells — 3V, brighter bulb)",
                "3 ಕೋಶಗಳು (Three Cells — 4.5V, brightest bulb)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "showHints",
            "type": "checkbox",
            "display_name": "ಪರಿಕಲ್ಪನಾ ಕಾರ್ಡ್ ತೋರಿಸಿ (Show Concept Card)",
            "default": True,
            "options": [True, False],
            "url_param": "showHints"
        }
    ],
    "auto_start_param": None,
    "topic": "Science – Electricity (ವಿದ್ಯುತ್)"
}


# =============================================================================
# DEFAULT SIMULATION
# =============================================================================
# =============================================================================
DEFAULT_SIMULATION = "simple_pendulum"

# =============================================================================
# UI SETTINGS
# =============================================================================
UI_CONFIG = {
    "page_title": "🎓 Adaptive Physics Tutor",
    "page_icon": "🎓",
    "layout": "wide",
    
    # Simulation display
    "simulation_height": 700,
    "simulation_width": "100%",
    
    # Chat settings
    "max_chat_history": 50,  # Messages to keep in view
    
    # Colors
    "teacher_bg_color": "#e3f2fd",  # Light blue
    "student_bg_color": "#f5f5f5",  # Light gray
    "system_bg_color": "#fff3e0",   # Light orange
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_simulation_config(sim_key: str) -> dict:
    """Get configuration for a specific simulation."""
    return SIMULATIONS.get(sim_key, SIMULATIONS[DEFAULT_SIMULATION])


def build_simulation_url(sim_key: str, params: dict, auto_start: bool = True) -> str:
    """
    Build the full URL for a simulation with parameters.
    
    Args:
        sim_key: Key of the simulation (e.g., "simple_pendulum")
        params: Dictionary of parameter values (using internal names)
        auto_start: Whether to auto-start the simulation
        
    Returns:
        Full URL with query parameters
    """
    config = get_simulation_config(sim_key)
    base_url = config["base_url"]
    
    # Build query params
    query_parts = []
    
    # Add simulation parameters
    for param_config in config["parameters"]:
        internal_name = param_config["name"]
        url_name = param_config["url_param"]
        
        if internal_name in params:
            value = params[internal_name]
            
            # Convert Python booleans to lowercase for JavaScript compatibility
            if isinstance(value, bool):
                value = "true" if value else "false"
            
            query_parts.append(f"{url_name}={value}")
    
    # Add auto-start if enabled and configured
    if auto_start and config.get("auto_start_param"):
        query_parts.append(f"{config['auto_start_param']}=true")
    
    # Combine
    if query_parts:
        return f"{base_url}?{'&'.join(query_parts)}"
    return base_url


def get_available_simulations() -> list:
    """Get list of available simulation keys and names."""
    return [(key, config["name"]) for key, config in SIMULATIONS.items()]


def get_default_params(sim_key: str) -> dict:
    """Get default parameter values for a simulation."""
    config = get_simulation_config(sim_key)
    return {
        param["name"]: param["default"] 
        for param in config["parameters"]
    }
