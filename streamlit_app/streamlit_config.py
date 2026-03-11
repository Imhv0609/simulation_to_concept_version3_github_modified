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
# LAMP TYPES (KN)
# =============================================================================
SIMULATIONS["lamp_types_kn"] = {
    "name": "ದೀಪ ಪ್ರಕಾರಗಳು (Lamp Types — Incandescent vs LED)",
    "language": "kannada",
    "description": (
        "ಇನ್ಕ್ಯಾಂಡಿಸೆಂಟ್ ಬಲ್ಬ್ ಮತ್ತು LED ಅನ್ನು ಆನ್/ಆಫ್ ಮಾಡಿ ಹೋಲಿಕೆ ಮಾಡಿ — ಫಿಲಾಮೆಂಟ್ vs ಸೆಮಿಕಂಡಕ್ಟರ್.\n"
        "Compare incandescent (filament) and LED (semiconductor) lamps by switching each on and off."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation6_lamp_types_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದೀಪ ಸ್ಥಿತಿ / Lamp State",
            "default": "incandescent_off",
            "options": ["incandescent_off", "incandescent_on", "led_off", "led_on"],
            "option_labels": [
                "ಇನ್ಕ್ಯಾಂಡಿಸೆಂಟ್ ಆಫ್ (Incandescent off — default view)",
                "ಇನ್ಕ್ಯಾಂಡಿಸೆಂಟ್ ಆನ್ (Incandescent on — filament glowing)",
                "LED ಆಫ್ (LED off — polarity view)",
                "LED ಆನ್ (LED on — semiconductor emitting light)"
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
# SIMPLE CIRCUIT (KN)
# =============================================================================
SIMULATIONS["simple_circuit_kn"] = {
    "name": "ಸರಳ ವಿದ್ಯುತ್ ಸರ್ಕ್ಯೂಟ್ (Simple Electric Circuit)",
    "language": "kannada",
    "description": (
        "ಕೋಶ, ಬಲ್ಬ್, ಸ್ವಿಚ್ ಮತ್ತು ತಂತಿಗಳನ್ನು ಇರಿಸಿ ಸರ್ಕ್ಯೂಟ್ ನಿರ್ಮಿಸಿ ಮತ್ತು ಪರೀಕ್ಷಿಸಿ.\n"
        "Build a simple circuit by placing all four components and test it to see the bulb light up."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation7_simple_circuit_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಸರ್ಕ್ಯೂಟ್ ಸ್ಥಿತಿ / Circuit State",
            "default": "empty",
            "options": ["empty", "built", "tested"],
            "option_labels": [
                "ಖಾಲಿ ಬೋರ್ಡ್ (Empty — no components placed)",
                "ನಿರ್ಮಿಸಿದ (Built — all components placed)",
                "ಪರೀಕ್ಷಿಸಿದ (Tested — circuit running, bulb lit)"
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
# ELECTRIC SWITCH (KN)
# =============================================================================
SIMULATIONS["electric_switch_kn"] = {
    "name": "ವಿದ್ಯುತ್ ಸ್ವಿಚ್ (Electric Switch)",
    "language": "kannada",
    "description": (
        "ಸ್ವಿಚ್ ಆನ್/ಆಫ್ ಟಾಗಲ್ ಮಾಡಿ — ಲಿವರ್, ಪುಶ್ ಮತ್ತು ಟಾಗಲ್ ಸ್ವಿಚ್ ಪ್ರಕಾರಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.\n"
        "Toggle the switch ON/OFF and observe circuit changes. Explore three switch types."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation8_electric_switch_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಸ್ವಿಚ್ ಸ್ಥಿತಿ / Switch State",
            "default": "off",
            "options": ["off", "on"],
            "option_labels": [
                "ಆಫ್ (Off — open circuit, bulb dark)",
                "ಆನ್ (On — closed circuit, bulb lit)"
            ],
            "url_param": "initialState"
        },
        {
            "name": "switchType",
            "type": "select",
            "display_name": "ಸ್ವಿಚ್ ಪ್ರಕಾರ / Switch Type",
            "default": "lever",
            "options": ["lever", "push", "toggle"],
            "option_labels": [
                "ಲಿವರ್ ಸ್ವಿಚ್ (Lever — wall switches)",
                "ಪುಶ್ ಬಟನ್ (Push button — doorbells, calculators)",
                "ಟಾಗಲ್ ಸ್ವಿಚ್ (Toggle — electronics boards)"
            ],
            "url_param": "switchType"
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
# CIRCUIT SYMBOLS (KN)
# =============================================================================
SIMULATIONS["circuit_symbols_kn"] = {
    "name": "ಸರ್ಕ್ಯೂಟ್ ಚಿಹ್ನೆಗಳು (Circuit Symbols)",
    "language": "kannada",
    "description": (
        "ಸರ್ಕ್ಯೂಟ್ ಚಿತ್ರಗಳಲ್ಲಿ ಬಳಸಲಾಗುವ ಮಾನಕ ಚಿಹ್ನೆಗಳನ್ನು ಕಲಿಯಿರಿ — ಕೋಶ, ಬ್ಯಾಟರಿ, ಬಲ್ಬ್, LED, ಸ್ವಿಚ್, ತಂತಿ.\n"
        "Learn standard circuit diagram symbols for cell, battery, bulb, LED, switches and wires."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter3_simulation9_circuit_symbols_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಚಿಹ್ನೆ / Symbol to Display",
            "default": "cell",
            "options": [
                "cell", "battery", "bulb", "led",
                "switch_open", "switch_closed", "wire", "wire_cross"
            ],
            "option_labels": [
                "ಕೋಶ (Cell — single long+short line pair)",
                "ಬ್ಯಾಟರಿ (Battery — multiple cell pairs)",
                "ದೀಪ/ಬಲ್ಬ್ (Bulb — circle with X)",
                "LED (LED — triangle + arrow)",
                "ತೆರೆದ ಸ್ವಿಚ್ (Switch Open — gap in line)",
                "ಮುಚ್ಚಿದ ಸ್ವಿಚ್ (Switch Closed — complete line)",
                "ತಂತಿ (Wire — straight conductor line)",
                "ತಂತಿ ಛೇದನ (Wire Cross — crossing without connection)"
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
# MATERIALS APPLICATIONS (KN) — Chapter 4
# =============================================================================
SIMULATIONS["materials_applications_kn"] = {
    "name": "ಲೋಹ ಮತ್ತು ಅಲೋಹ ಬಳಕೆಗಳು (Applications of Metals & Non-metals)",
    "language": "kannada",
    "description": (
        "ಲೋಹ, ಅಲೋಹ ಮತ್ತು ಎರಡೂ ಬಳಸುವ ವಸ್ತುಗಳ ನೈಜ-ಜೀವನ ಅನ್ವಯಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.\n"
        "Explore real-world applications of metals, non-metals, and objects combining both."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation10_applications_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ವರ್ಗ / Category",
            "default": "metals",
            "options": ["metals", "nonmetals", "both"],
            "option_labels": [
                "ಲೋಹಗಳು (Metals — wires, cookware, bells, jewellery)",
                "ಅಲೋಹಗಳು (Non-metals — insulation, oxygen, chlorine, iodine)",
                "ಎರಡೂ ಬಳಕೆ (Both — tools, pans, plugs, pencils)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# MALLEABILITY (KN) — Chapter 4
# =============================================================================
SIMULATIONS["malleability_kn"] = {
    "name": "ನಮ್ಯತೆ (Malleability)",
    "language": "kannada",
    "description": (
        "ಲೋಹ ಮತ್ತು ಅಲೋಹ ವಸ್ತುಗಳ ಮೇಲೆ ಸುತ್ತಿಗೆ ಬಡಿದು ನಮ್ಯ ಮತ್ತು ಭಂಗುರ ಗುಣ ಕಲಿಯಿರಿ.\n"
        "Hammer metals and non-metals to learn which flatten (malleable) and which shatter (brittle)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation1_malleability_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರದರ್ಶನ ಸ್ಥಿತಿ / Demonstration State",
            "default": "initial",
            "options": ["initial", "metal_hammer", "nonmetal_hammer"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — blank experiment)",
                "ಲೋಹ ಸುತ್ತಿಗೆ (Metal Hammer — copper flattens into sheet)",
                "ಅಲೋಹ ಸುತ್ತಿಗೆ (Non-metal Hammer — coal shatters into pieces)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# DUCTILITY (KN) — Chapter 4
# =============================================================================
SIMULATIONS["ductility_kn"] = {
    "name": "ಸೆಳೆತ / ಎಳೆಯಬಲ್ಲ ಗುಣ (Ductility)",
    "language": "kannada",
    "description": (
        "ಲೋಹ ಮತ್ತು ಅಲೋಹ ವಸ್ತುಗಳನ್ನು ತೆಳು ತಂತಿಯಾಗಿ ಎಳೆಯಲು ಪ್ರಯತ್ನಿಸಿ — ಯಾವುದು ಎಳೆಯಲ್ಪಡುತ್ತದೆ, ಯಾವುದು ಮುರಿಯುತ್ತದೆ?\n"
        "Attempt to draw metals and non-metals into wires — which stretches and which snaps?"
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation2_ductility_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರದರ್ಶನ ಸ್ಥಿತಿ / Demonstration State",
            "default": "initial",
            "options": ["initial", "metal_draw", "nonmetal_draw"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — blank experiment)",
                "ಲೋಹ ಎಳೆತ (Metal Draw — copper stretches into wire)",
                "ಅಲೋಹ ಎಳೆತ (Non-metal Draw — coal snaps when pulled)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# SONORITY (KN) — Chapter 4
# =============================================================================
SIMULATIONS["sonority_kn"] = {
    "name": "ಧ್ವನಿವಂತ ಗುಣ (Sonority)",
    "language": "kannada",
    "description": (
        "ಘಂಟೆ, ಚಮಚ, ಮರ ಮತ್ತು ರಬ್ಬರ್ ಹೊಡೆದು ಲೋಹ ಮತ್ತು ಅಲೋಹ ಶಬ್ದ ಹೋಲಿಸಿ.\n"
        "Strike bells, spoons, wood, and rubber to compare the ringing of metals vs the thud of non-metals."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation3_sonority_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರದರ್ಶನ ಸ್ಥಿತಿ / Demonstration State",
            "default": "initial",
            "options": ["initial", "metal_strike", "nonmetal_strike"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — nothing struck yet)",
                "ಲೋಹ ಹೊಡೆತ (Metal Strike — bell rings clearly)",
                "ಅಲೋಹ ಹೊಡೆತ (Non-metal Strike — wood produces dull thud)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# HEAT CONDUCTION (KN) — Chapter 4
# =============================================================================
SIMULATIONS["heat_conduction_kn"] = {
    "name": "ಉಷ್ಣ ವಾಹಕತೆ (Heat Conduction)",
    "language": "kannada",
    "description": (
        "ಲೋಹ ಮತ್ತು ಮರದ ಚಮಚಗಳನ್ನು ಬಿಸಿ ನೀರಲ್ಲಿ ಇಟ್ಟು ಉಷ್ಣ ವಾಹಕತೆ ಹೋಲಿಸಿ.\n"
        "Place metal and wooden spoons in hot water and compare how heat travels through each."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation4_heat_conduction_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರಯೋಗ ಸ್ಥಿತಿ / Experiment State",
            "default": "initial",
            "options": ["initial", "running"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — spoons in water, experiment not started)",
                "ಪ್ರಾರಂಭ (Running — auto-starts 15-second heat conduction experiment)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# ELECTRICAL CONDUCTIVITY (KN) — Chapter 4
# =============================================================================
SIMULATIONS["electrical_conductivity_kn"] = {
    "name": "ವಿದ್ಯುತ್ ವಾಹಕತೆ (Electrical Conductivity)",
    "language": "kannada",
    "description": (
        "ಸರ್ಕ್ಯೂಟ್‌ನಲ್ಲಿ ವಿವಿಧ ವಸ್ತುಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ — ಬಲ್ಬ್ ಬೆಳಗುತ್ತದೆಯೇ ಅಥವಾ ಇಲ್ಲವೇ?\n"
        "Test materials in a circuit — does the bulb light (conductor) or stay dark (insulator)?"
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation5_electrical_conductivity_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪರೀಕ್ಷಾ ವಸ್ತು / Test Material",
            "default": "initial",
            "options": ["initial", "conductor_test", "insulator_test"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — idle circuit, no material inserted)",
                "ವಾಹಕ ಪರೀಕ್ಷೆ (Conductor Test — copper inserted, bulb lights)",
                "ಅವಾಹಕ ಪರೀಕ್ಷೆ (Insulator Test — rubber inserted, bulb stays off)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# RUSTING EXPERIMENT (KN) — Chapter 4
# =============================================================================
SIMULATIONS["rusting_experiment_kn"] = {
    "name": "ತುಕ್ಕು ಪ್ರಯೋಗ (Rusting Experiment)",
    "language": "kannada",
    "description": (
        "ಮೂರು ಟ್ಯೂಬ್‌ಗಳಲ್ಲಿ ಕಬ್ಬಿಣದ ಉಗುರುಗಳನ್ನು ಇಟ್ಟು ತುಕ್ಕಿಗೆ ಗಾಳಿ ಮತ್ತು ನೀರು ಎರಡೂ ಅಗತ್ಯ ಎಂದು ತೋರಿಸಿ.\n"
        "Place iron nails in 3 conditions and discover that BOTH air and water are needed for rusting."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation6_rusting_experiment_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಸಮಯ ಸ್ಥಿತಿ / Time State",
            "default": "initial",
            "options": ["initial", "day3", "day7"],
            "option_labels": [
                "ದಿನ 0 — ಆರಂಭ (Initial — day 0, all nails shiny)",
                "ದಿನ 3 — ಮಧ್ಯ (Day 3 — rust beginning in Tube C only)",
                "ದಿನ 7 — ಪ್ರಯೋಗ ಪೂರ್ಣ (Day 7 — experiment complete, results clear)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# METAL OXIDE REACTION (KN) — Chapter 4
# =============================================================================
SIMULATIONS["metal_oxide_reaction_kn"] = {
    "name": "ಲೋಹ ಆಕ್ಸೈಡ್ ಪ್ರತಿಕ್ರಿಯೆ (Metal Oxide Reaction)",
    "language": "kannada",
    "description": (
        "ಮೆಗ್ನೀಸಿಯಂ ಸುಡಿ → MgO ಕರಗಿಸಿ → ಲಿಟ್ಮಸ್ ಪರೀಕ್ಷೆ — ಲೋಹ ಆಕ್ಸೈಡ್ ಕ್ಷಾರೀಯ ಎಂದು ತೋರಿಸಿ.\n"
        "Burn Mg → dissolve MgO in water → test with litmus — proves metal oxides are basic."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation7_metal_oxide_reaction_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರಯೋಗ ಹಂತ / Experiment Step",
            "default": "initial",
            "options": ["initial", "burned", "dissolved", "tested"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — Mg ribbon ready, not yet burned)",
                "ಸುಟ್ಟ (Burned — Mg burned, white MgO ash formed)",
                "ಕರಗಿಸಿದ (Dissolved — MgO dissolved in water, Mg(OH)₂ ready)",
                "ಪರೀಕ್ಷಿಸಿದ (Tested — litmus test done, red→blue, proves basic)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# NON-METAL OXIDE REACTION (KN) — Chapter 4
# =============================================================================
SIMULATIONS["nonmetal_oxide_reaction_kn"] = {
    "name": "ಅಲೋಹ ಆಕ್ಸೈಡ್ ಪ್ರತಿಕ್ರಿಯೆ (Non-metal Oxide Reaction)",
    "language": "kannada",
    "description": (
        "ಸಲ್ಫರ್ ಸುಡಿ → SO₂ ಕರಗಿಸಿ → ಲಿಟ್ಮಸ್ ಪರೀಕ್ಷೆ — ಅಲೋಹ ಆಕ್ಸೈಡ್ ಆಮ್ಲೀಯ ಎಂದು ತೋರಿಸಿ.\n"
        "Burn S → dissolve SO₂ in water → test with litmus — proves non-metal oxides are acidic."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation8_nonmetal_oxide_reaction_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರಯೋಗ ಹಂತ / Experiment Step",
            "default": "initial",
            "options": ["initial", "burned", "dissolved", "tested"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — sulfur powder ready, not yet burned)",
                "ಸುಟ್ಟ (Burned — sulfur burned with blue flame, SO₂ collected)",
                "ಕರಗಿಸಿದ (Dissolved — SO₂ dissolved, H₂SO₃ sulfurous acid formed)",
                "ಪರೀಕ್ಷಿಸಿದ (Tested — litmus test done, blue→red, proves acidic)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# METALS vs NON-METALS COMPARISON (KN) — Chapter 4
# =============================================================================
SIMULATIONS["metals_nonmetals_compare_kn"] = {
    "name": "ಲೋಹ ಮತ್ತು ಅಲೋಹ ಹೋಲಿಕೆ (Metals vs Non-metals Comparison)",
    "language": "kannada",
    "description": (
        "8 ಗುಣಗಳ ಸಂವಾದಾತ್ಮಕ ಹೋಲಿಕೆ — ದ್ಯುತಿ, ನಮ್ಯತೆ, ಸೆಳೆತ, ಧ್ವನಿ, ಉಷ್ಣ, ವಿದ್ಯುತ್, ಕಾಠಿಣ್ಯ, ಆಕ್ಸೈಡ್.\n"
        "8-property interactive comparison: tap a property to see metal vs non-metal side by side."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter4_simulation9_metals_nonmetals_compare_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ಪ್ರದರ್ಶಿಸಲು ಗುಣ / Property to Display",
            "default": "initial",
            "options": [
                "initial", "malleability", "ductility", "sonority",
                "heat_conduction", "electrical_conduction", "hardness", "oxide_nature"
            ],
            "option_labels": [
                "ದ್ಯುತಿ (Lustre — shiny vs dull)",
                "ನಮ್ಯತೆ (Malleability — flatten vs shatter)",
                "ಸೆಳೆತ (Ductility — wire vs snap)",
                "ಧ್ವನಿ (Sonority — ring vs thud)",
                "ಉಷ್ಣ ವಾಹಕತೆ (Heat Conduction — good vs poor)",
                "ವಿದ್ಯುತ್ ವಾಹಕತೆ (Electrical Conduction — conductor vs insulator)",
                "ಕಾಠಿಣ್ಯ (Hardness — generally hard vs soft)",
                "ಆಕ್ಸೈಡ್ ಸ್ವಭಾವ (Oxide Nature — basic vs acidic)"
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
    "topic": "Science – Materials: Metals & Non-metals (ಲೋಹ ಮತ್ತು ಅಲೋಹ)"
}

# =============================================================================
# WEATHERING AND EROSION (KN) — Chapter 5
# =============================================================================
SIMULATIONS["weathering_erosion_kn"] = {
    "name": "ವಾತಾವರಣ ಮತ್ತು ಕೊರೆತ (Weathering and Erosion)",
    "language": "kannada",
    "description": (
        "ಪರ್ವತ, ನದಿ, ಸಮುದ್ರ ಬಂಡೆ ದೃಶ್ಯಗಳಲ್ಲಿ ಲಕ್ಷಾಂತರ ವರ್ಷ ಕಾಲ-ಪ್ರಯಾಣ ಮಾಡಿ ಭೂರೂಪ ಬದಲಾವಣೆ ನೋಡಿ.\n"
        "Time-travel through mountain, river, and sea-cliff scenes to see landscapes shaped over millions of years."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation10_weathering_erosion_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "ದೃಶ್ಯ / ಸ್ಥಿತಿ — Scene / Time State",
            "default": "initial",
            "options": [
                "initial", "mountain", "river", "cliff",
                "mountain_aged", "river_aged", "cliff_aged"
            ],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — mountain scene, time = 0)",
                "ಪರ್ವತ (Mountain — fresh peak, snow cap, time = 0)",
                "ನದಿ (River — angular rocks, time = 0)",
                "ಸಮುದ್ರ ಬಂಡೆ (Sea Cliff — intact cliff face, time = 0)",
                "ಹಳೆಯ ಪರ್ವತ (Mountain Aged — 1M yrs, peak eroded, sediment spread)",
                "ಹಳೆಯ ನದಿ (River Aged — 1M yrs, smooth rounded pebbles, sand)",
                "ಹಳೆಯ ಸಮುದ್ರ ಬಂಡೆ (Cliff Aged — 1M yrs, cave + sea stack formed)"
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
    "topic": "Science – Earth & Landforms (ಭೂಮಿ ಮತ್ತು ಭೂರೂಪ)"
}

SIMULATIONS["physical_changes_kn"] = {
    "name": "ಭೌತಿಕ ಬದಲಾವಣೆಗಳು (Physical Changes)",
    "language": "kannada",
    "description": (
        "ಆರು ಉದಾಹರಣೆಗಳ ಮೂಲಕ ಭೌತಿಕ ಬದಲಾವಣೆ ಅಧ್ಯಯನ ಮಾಡಿ — ಹೊಸ ಪದಾರ್ಥ ರೂಪುಗೊಳ್ಳುವುದಿಲ್ಲ.\n"
        "Explore physical changes through 6 examples — same substance, different form."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation1_physical_changes_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Example to Show / ಉದಾಹರಣೆ ಆಯ್ಕೆ",
            "default": "ice",
            "options": ["initial", "paper", "chalk", "ice", "balloon", "rubber", "spring"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — no example selected)",
                "ಕಾಗದ ಮಡಚಿ (Paper Folding — reversible)",
                "ಸೀಮೆಸುಣ್ಣ ಚೂರ್ಣ (Chalk Crushing — irreversible)",
                "ಬರ್ಫ ಕರಗಿಸಿ (Ice Melting — reversible state change)",
                "ಬಲೂನ್ ಊದಿ (Balloon Inflating — reversible)",
                "ಬ್ಯಾಂಡ್ ಚಾಚಿ (Rubber Stretching — reversible)",
                "ಸ್ಪ್ರಿಂಗ್ ಒತ್ತಿ (Spring Compressing — reversible)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# CHEMICAL CHANGES SIMULATION (Kannada)
# ರಾಸಾಯನಿಕ ಬದಲಾವಣೆಗಳು – ಹೊಸ ಪದಾರ್ಥಗಳು
# =============================================================================
SIMULATIONS["chemical_changes_kn"] = {
    "name": "ರಾಸಾಯನಿಕ ಬದಲಾವಣೆಗಳು (Chemical Changes)",
    "language": "kannada",
    "description": (
        "ವಿನಿಗರ್+ಬೇಕಿಂಗ್ ಸೋಡಾ ಮತ್ತು ಸುಣ್ಣದ ನೀರಿನ CO₂ ಪರೀಕ್ಷೆ ಮೂಲಕ ರಾಸಾಯನಿಕ ಬದಲಾವಣೆ ಅಧ್ಯಯನ.\n"
        "Observe chemical changes: vinegar+baking soda reaction and the CO₂ limewater test."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation2_chemical_changes_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Experiment State / ಪ್ರಯೋಗ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "vinegar_reacted", "limewater", "limewater_reacted"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — vinegar + baking soda, unmixed)",
                "ವಿನಿಗರ್ ಪ್ರತಿಕ್ರಿಯೆ (Vinegar Reacted — CO₂ bubbles visible)",
                "ಸುಣ್ಣದ ನೀರು (Limewater — clear, before CO₂)",
                "ಸುಣ್ಣದ ನೀರು ಹಾಲಿನಂತೆ (Limewater Reacted — milky white CaCO₃)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# REVERSIBLE & IRREVERSIBLE CHANGES SIMULATION (Kannada)
# ಹಿಮ್ಮುಖ ಮತ್ತು ಅಹಿಮ್ಮುಖ ಬದಲಾವಣೆಗಳು
# =============================================================================
SIMULATIONS["reversible_irreversible_kn"] = {
    "name": "ಹಿಮ್ಮುಖ ಮತ್ತು ಅಹಿಮ್ಮುಖ (Reversible & Irreversible Changes)",
    "language": "kannada",
    "description": (
        "10 ದೈನಂದಿನ ಬದಲಾವಣೆಗಳನ್ನು ಹಿಮ್ಮುಖ ಅಥವಾ ಅಹಿಮ್ಮುಖ ಎಂದು ವರ್ಗೀಕರಿಸಿ.\n"
        "Quiz: classify 10 everyday changes as reversible or irreversible."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation3_reversible_irreversible_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Quiz State / ಕ್ವಿಜ್ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "show_reversible", "show_irreversible"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — first question: melting ice)",
                "ಹಿಮ್ಮುಖ ತೋರಿಸಿ (Show Reversible — answer melting ice as reversible)",
                "ಅಹಿಮ್ಮುಖ ತೋರಿಸಿ (Show Irreversible — jump to burning paper, answer irreversible)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# STATES OF MATTER SIMULATION (Kannada)
# ದ್ರವ್ಯದ ಸ್ಥಿತಿಗಳು – ನೀರಿನ ಪರಿವರ್ತನೆಗಳು
# =============================================================================
SIMULATIONS["states_of_matter_kn"] = {
    "name": "ದ್ರವ್ಯದ ಸ್ಥಿತಿಗಳು (States of Matter – Water)",
    "language": "kannada",
    "description": (
        "ಉಷ್ಣತಾಮಾನ ಸ್ಲೈಡರ್ ಮೂಲಕ ನೀರಿನ ಮೂರು ಸ್ಥಿತಿಗಳು: ಘನ, ದ್ರವ ಮತ್ತು ಅನಿಲ ಅನ್ವೇಷಿಸಿ.\n"
        "Slide the temperature to see water as solid (ice), liquid, or gas (steam)."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation4_states_of_matter_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "State of Water / ನೀರಿನ ಸ್ಥಿತಿ",
            "default": "liquid",
            "options": ["solid", "liquid", "gas"],
            "option_labels": [
                "ಘನ (Solid — ice at −10°C)",
                "ದ್ರವ (Liquid — water at 25°C)",
                "ಅನಿಲ (Gas — steam at 110°C)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# FIRE TRIANGLE SIMULATION (Kannada)
# ಅಗ್ನಿ ತ್ರಿಕೋಣ – ದಹನಕ್ಕೆ ಅಗತ್ಯಗಳು
# =============================================================================
SIMULATIONS["fire_triangle_kn"] = {
    "name": "ಅಗ್ನಿ ತ್ರಿಕೋಣ (Fire Triangle – Combustion Conditions)",
    "language": "kannada",
    "description": (
        "ಇಂಧನ, ಆಮ್ಲಜನಕ ಮತ್ತು ಉಷ್ಣ — ಮೂರು ಅಂಶ ಒಟ್ಟಿಗೆ ಇದ್ದಾಗ ಮಾತ್ರ ಅಗ್ನಿ.\n"
        "Toggle fuel, oxygen, and heat — fire lights only when all three are present."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter5_simulation5_fire_triangle_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Fire Triangle State / ಅಗ್ನಿ ತ್ರಿಕೋಣ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "fire", "no_fuel", "no_oxygen", "no_heat"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — no elements, no fire)",
                "ಅಗ್ನಿ (Fire — all three: fuel + oxygen + heat)",
                "ಇಂಧನ ಇಲ್ಲ (No Fuel — oxygen + heat only, no fire)",
                "ಆಮ್ಲಜನಕ ಇಲ್ಲ (No Oxygen — fuel + heat only, no fire)",
                "ಉಷ್ಣ ಇಲ್ಲ (No Heat — fuel + oxygen only, no fire)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# OXYGEN AND COMBUSTION SIMULATION (KANNADA) — Chapter 5 Sim 6
# =============================================================================
SIMULATIONS["oxygen_combustion_kn"] = {
    "name": "ಉರಿಯಲು ಆಮ್ಲಜನಕ ಅಗತ್ಯ (Oxygen Required for Combustion)",
    "language": "kannada",
    "description": (
        "Candle-and-glass-jar experiment demonstrating that oxygen is essential for "
        "combustion. Light the candle, then cover it — oxygen depletes, CO₂ builds up, "
        "flame extinguishes. Proves the role of oxygen in sustaining fire."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter5_simulation6_oxygen_combustion_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Experiment State / ಪ್ರಯೋಗ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "lit", "covered_extinguished"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — candle unlit, no jar)",
                "ಉರಿಯುತ್ತಿದೆ (Lit — candle burning freely)",
                "ಮುಚ್ಚಿ ಆರಿಸಿ (Covered & Extinguished — jar seals, O₂ depletes, flame dies)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# CANDLE BURNING — DUAL CHANGE SIMULATION (KANNADA) — Chapter 5 Sim 7
# =============================================================================
SIMULATIONS["candle_burning_kn"] = {
    "name": "ಮೇಣ ಉರಿಯುವಿಕೆ – ಭೌತಿಕ ಮತ್ತು ರಾಸಾಯನಿಕ ಬದಲಾವಣೆ (Candle Burning)",
    "language": "kannada",
    "description": (
        "Two-tab simulation showing that a burning candle involves BOTH a physical "
        "change (wax melting) AND a chemical change (wax combustion) simultaneously. "
        "Toggle between the two views to compare."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter5_simulation7_candle_burning_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Change Type / ಬದಲಾವಣೆಯ ಪ್ರಕಾರ",
            "default": "physical",
            "options": ["physical", "chemical"],
            "option_labels": [
                "ಭೌತಿಕ ಬದಲಾವಣೆ (Physical — wax melting: solid → liquid, reversible)",
                "ರಾಸಾಯನಿಕ ಬದಲಾವಣೆ (Chemical — wax burning: wax + O₂ → CO₂ + H₂O, irreversible)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# COMBUSTION EXAMPLES SIMULATION (KANNADA) — Chapter 5 Sim 8
# =============================================================================
SIMULATIONS["combustion_examples_kn"] = {
    "name": "ವಿವಿಧ ಪದಾರ್ಥಗಳ ದಹನ (Combustion Examples)",
    "language": "kannada",
    "description": (
        "Select from six materials (magnesium, paper, wood, charcoal, sulfur, match) "
        "and observe each burning with its characteristic flame colour and chemical products. "
        "Teaches that all combustion requires oxygen and produces oxides."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter5_simulation8_combustion_examples_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Material to Burn / ಸುಡಬೇಕಾದ ಪದಾರ್ಥ",
            "default": "magnesium",
            "options": ["initial", "magnesium", "paper", "wood", "charcoal", "sulfur", "match"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — no material selected)",
                "ಮೆಗ್ನೀಸಿಯಂ (Magnesium — 2Mg + O₂ → 2MgO, bright white flame)",
                "ಹಾಳೆ/ಕಾಗದ (Paper — yellow flame, CO₂ + H₂O + grey ash)",
                "ಮರ (Wood — orange-yellow flame, CO₂ + H₂O + smoke)",
                "ಇದ್ದಲು (Charcoal — red glow, no flame, C + O₂ → CO₂)",
                "ಗಂಧಕ (Sulfur — blue flame, S + O₂ → SO₂)",
                "ಬೆಂಕಿಕಡ್ಡಿ (Match — two-stage: head then wood ignites)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# DESIRABLE AND UNDESIRABLE CHANGES SIMULATION (KANNADA) — Chapter 5 Sim 9
# =============================================================================
SIMULATIONS["desirable_undesirable_kn"] = {
    "name": "ಅಪೇಕ್ಷಣೀಯ ಮತ್ತು ಅನಪೇಕ್ಷಿತ ಬದಲಾವಣೆಗಳು (Desirable & Undesirable Changes)",
    "language": "kannada",
    "description": (
        "Quiz simulation classifying 10 real-world changes (milk curdling, rusting, cooking, "
        "rotting, germination, pollution, composting, tooth decay, bread making, global warming) "
        "as desirable or undesirable, with detailed feedback."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter5_simulation9_desirable_undesirable_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Quiz State / ಪ್ರಶ್ನೋತ್ತರ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "show_desirable", "show_undesirable"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — first question shown, no answer yet)",
                "ಅಪೇಕ್ಷಣೀಯ ತೋರಿಸಿ (Show Desirable — auto-answers Q1 correctly as desirable)",
                "ಅನಪೇಕ್ಷಿತ ತೋರಿಸಿ (Show Undesirable — auto-answers Q1 incorrectly as undesirable)"
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
    "topic": "Science – Changes Around Us (ನಮ್ಮ ಸುತ್ತಲಿನ ಬದಲಾವಣೆಗಳು)"
}


# =============================================================================
# SAY NO TO HARMFUL SUBSTANCES SIMULATION (KANNADA) — Chapter 6 Sim 10
# =============================================================================
SIMULATIONS["say_no_kn"] = {
    "name": "ಹಾನಿಕರ ವಸ್ತುಗಳಿಗೆ 'ಇಲ್ಲ' ಹೇಳಿ (Say No to Harmful Substances)",
    "language": "kannada",
    "description": (
        "Scenario-based refusal training (Chapter 6): 5 peer-pressure situations involving "
        "tobacco, alcohol, vaping, pills, and social settings. Students practice saying NO "
        "with immediate feedback. Helpline: 14446."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation10_say_no_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Scenario State / ಸನ್ನಿವೇಶ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "show_no", "show_yes"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — scenario 1 shown, no response yet)",
                "'ಇಲ್ಲ' ತೋರಿಸಿ (Show NO — correct refusal choice with positive feedback)",
                "'ಹೌದು' ತೋರಿಸಿ (Show YES — wrong acceptance choice with consequences feedback)"
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
    "topic": "Science – Knowing About Tobacco, Alcohol and Drugs (ತಂಬಾಕು, ಮದ್ಯ ಮತ್ತು ಮಾದಕ ದ್ರವ್ಯಗಳ ಬಗ್ಗೆ)"
}


# =============================================================================
# LIFE STAGES OF HUMANS SIMULATION (KANNADA) — Chapter 6 Sim 1
# =============================================================================
SIMULATIONS["life_stages_kn"] = {
    "name": "ಮಾನವ ಜೀವನದ ಹಂತಗಳು (Human Life Stages)",
    "language": "kannada",
    "description": (
        "Interactive timeline showing the five stages of human life: infancy, childhood, "
        "adolescence, adulthood, and old age. Clicking each stage reveals its key characteristics. "
        "Adolescence is highlighted as the central stage students are currently experiencing."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation1_life_stages_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Life Stage / ಜೀವನ ಹಂತ",
            "default": "adolescence",
            "options": ["infant", "childhood", "adolescence", "adulthood", "old_age"],
            "option_labels": [
                "👶 ಶಿಶು ಅವಧಿ (Infancy — 0-2 yrs: rapid growth, first words)",
                "🧒 ಬಾಲ್ಯ (Childhood — 3-9 yrs: learning, play, social skills)",
                "⭐ ಕೌಮಾರ (Adolescence — 10-19 yrs: puberty, identity) [default]",
                "👨 ಪ್ರೌಢಾವಸ್ಥೆ (Adulthood — 20-60 yrs: career, family)",
                "👴 ವೃದ್ಧಾವಸ್ಥೆ (Old Age — 60+ yrs: wisdom, guidance)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# GROWTH CHART DURING ADOLESCENCE SIMULATION (KANNADA) — Chapter 6 Sim 2
# =============================================================================
SIMULATIONS["growth_chart_kn"] = {
    "name": "ಕೌಮಾರದಲ್ಲಿ ಬೆಳವಣಿಗೆ ಚಾರ್ಟ್ (Growth Chart During Adolescence)",
    "language": "kannada",
    "description": (
        "Age slider (5-20 years) showing average height and weight at each age, "
        "with animated person figure and growth-rate indicators. "
        "The rocket icon appears during the growth spurt (≥6 cm/year gain)."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation2_growth_chart_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Age to Display / ತೋರಿಸಬೇಕಾದ ವಯಸ್ಸು",
            "default": "age_12",
            "options": ["age_8", "age_10", "age_12", "age_13", "age_14", "age_15", "age_16", "age_18", "age_20"],
            "option_labels": [
                "ವಯಸ್ಸು 8 (Age 8 — 128cm, 26kg, steady growth)",
                "ವಯಸ್ಸು 10 (Age 10 — 138cm, 32kg, pre-puberty)",
                "ವಯಸ್ಸು 12 (Age 12 — 149cm, 40kg, growth spurt begins) [default]",
                "ವಯಸ್ಸು 13 (Age 13 — 156cm, 45kg, 🚀 peak spurt +7cm/yr)",
                "ವಯಸ್ಸು 14 (Age 14 — 162cm, 50kg, rapid growth)",
                "ವಯಸ್ಸು 15 (Age 15 — 167cm, 55kg, slowing)",
                "ವಯಸ್ಸು 16 (Age 16 — 170cm, 58kg, near adult)",
                "ವಯಸ್ಸು 18 (Age 18 — 173cm, 62kg, near-adult height)",
                "ವಯಸ್ಸು 20 (Age 20 — 175cm, 65kg, adult height reached)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# PHYSICAL CHANGES IN PUBERTY SIMULATION (KANNADA) — Chapter 6 Sim 3
# =============================================================================
SIMULATIONS["puberty_physical_changes_kn"] = {
    "name": "ಯೌವನದಲ್ಲಿ ಭೌತಿಕ ಬದಲಾವಣೆಗಳು (Physical Changes in Puberty)",
    "language": "kannada",
    "description": (
        "Three-tab simulation: common changes (all genders), boys-specific, girls-specific. "
        "Each tab lists puberty changes with tap-to-expand detail and a 'completely normal' badge. "
        "Explains secondary sexual characteristics."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation3_physical_changes_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Change Category / ಬದಲಾವಣೆ ವರ್ಗ",
            "default": "common",
            "options": ["common", "boys", "girls"],
            "option_labels": [
                "🔄 ಸಾಮಾನ್ಯ (Common — all genders: growth spurt, body hair, acne) [default]",
                "👦 ಹುಡುಗರಲ್ಲಿ (Boys — voice deepening, broad shoulders, facial hair)",
                "👧 ಹುಡುಗಿಯರಲ್ಲಿ (Girls — wider hips, breast development, menstruation)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# VOICE CHANGES IN PUBERTY SIMULATION (KANNADA) — Chapter 6 Sim 4
# =============================================================================
SIMULATIONS["voice_changes_kn"] = {
    "name": "ಯೌವನದಲ್ಲಿ ಧ್ವನಿ ಬದಲಾವಣೆಗಳು (Voice Changes in Puberty)",
    "language": "kannada",
    "description": (
        "SVG larynx diagram × gender (boys/girls) × puberty stage (before/during/after) "
        "giving 6 explorable states. Shows larynx size, vocal cord positions, Adam's apple, "
        "wave visualisation of voice pitch, and explanation of voice cracking. "
        "Comparison panel: boys drop ~1 octave; girls only ~3 semitones."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation4_voice_changes_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Gender × Stage / ಲಿಂಗ × ಹಂತ",
            "default": "boys_before",
            "options": ["boys_before", "boys_during", "boys_after", "girls_before", "girls_during", "girls_after"],
            "option_labels": [
                "👦 ಯೌವನ ಮೊದಲು (Boys before — small larynx, high pitch) [default]",
                "👦 ಯೌವನ ಸಮಯ (Boys during — larynx growing, voice cracking)",
                "👦 ಯೌವನ ನಂತರ (Boys after — large larynx, deep voice, Adam's apple)",
                "👧 ಯೌವನ ಮೊದಲು (Girls before — small larynx, high pitch)",
                "👧 ಯೌವನ ಸಮಯ (Girls during — slight growth, subtle change)",
                "👧 ಯೌವನ ನಂತರ (Girls after — modest change, mature female voice)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# MENSTRUAL CYCLE SIMULATION (KANNADA) — Chapter 6 Sim 5
# =============================================================================
SIMULATIONS["menstrual_cycle_kn"] = {
    "name": "ಋತುಚಕ್ರ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು (Understanding the Menstrual Cycle)",
    "language": "kannada",
    "description": (
        "28-day cycle ring diagram with day slider and 4-phase legend. "
        "Clicking/dragging updates phase info for: Menstruation (d.1-5), "
        "Follicular (d.6-13), Ovulation (d.14), Luteal (d.15-28). "
        "Myth-buster panel challenges impurity/exercise misconceptions."
    ),
    "base_url": f"{GITHUB_PAGES_BASE_KN}/science_chapter6_simulation5_menstrual_cycle_kn.html",
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Cycle Phase / ಚಕ್ರ ಹಂತ",
            "default": "menstruation",
            "options": ["menstruation", "follicular", "ovulation", "luteal"],
            "option_labels": [
                "🔴 ಋತುಚಕ್ರ (Menstruation — days 1-5: uterine lining sheds) [default]",
                "🟠 ಫಾಲಿಕ್ಯುಲರ್ (Follicular — days 6-13: lining rebuilds)",
                "🟢 ಅಂಡೋತ್ಸರ್ಜನ (Ovulation — day 14: egg released)",
                "🔵 ಲ್ಯೂಟಿಯಲ್ (Luteal — days 15-28: waiting period)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}



# =============================================================================
# EMOTIONAL CHANGES IN ADOLESCENCE (KN) — Chapter 6 Sim 6
# =============================================================================
SIMULATIONS["emotional_changes_kn"] = {
    "name": "ಕೌಮಾರದಲ್ಲಿ ಭಾವನಾತ್ಮಕ ಬದಲಾವಣೆಗಳು (Emotional Changes in Adolescence)",
    "language": "kannada",
    "description": (
        "5-scenario emotion-recognition simulation: each scenario presents a common adolescent "
        "situation (friend drift, exam failure, body changes, parental rules, being teased) "
        "and validates all emotional responses with science-based explanations.\n"
        "Teaches that mood swings, hormone-driven emotions, and social anxiety are all normal "
        "during adolescence, and provides healthy coping strategies for each."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter6_simulation6_emotional_changes_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Scenario / ಸನ್ನಿವೇಶ",
            "default": "scenario1",
            "options": [
                "scenario1", "scenario2", "scenario3",
                "scenario4", "scenario5", "completed"
            ],
            "option_labels": [
                "ಸ್ನೇಹಿತ ದೂರ (Scenario 1 — friend spends time with others) [default]",
                "ಪರೀಕ್ಷೆ ವಿಫಲ (Scenario 2 — exam failure despite studying)",
                "ದೇಹ ಬದಲಾವಣೆ (Scenario 3 — body changing faster/slower than peers)",
                "ಪೋಷಕರ ನಿಯಮ (Scenario 4 — parents' rules seem unfair)",
                "ಅಪಹಾಸ್ಯ (Scenario 5 — being teased about appearance/behaviour)",
                "ಪೂರ್ಣ (Completed — all scenarios explored)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# NUTRITION FOR ADOLESCENTS (KN) — Chapter 6 Sim 7
# =============================================================================
SIMULATIONS["nutrition_adolescence_kn"] = {
    "name": "ಕೌಮಾರ ವಯಸ್ಕರಿಗೆ ಪೋಷಣೆ (Nutrition for Adolescents)",
    "language": "kannada",
    "description": (
        "Interactive plate model with 4 nutrient group tabs (carbohydrates, proteins, "
        "vitamins & minerals, healthy fats). Tapping each section shows food examples "
        "and the science behind why that nutrient is especially important during "
        "adolescence. Special panel on girls' increased iron, calcium, and B12 needs.\n"
        "Teaches balanced diet principles and the specific nutritional demands of the "
        "adolescent growth spurt."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter6_simulation7_nutrition_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Nutrient Group / ಪೋಷಕಾಂಶ ಗುಂಪು",
            "default": "carbs",
            "options": ["carbs", "protein", "veggies", "fats"],
            "option_labels": [
                "🍚 ಕಾರ್ಬೋಹೈಡ್ರೇಟ್ (Carbs — energy source; rice, roti, millets) [default]",
                "🍗 ಪ್ರೋಟೀನ್ (Protein — body building; dal, eggs, chicken, nuts)",
                "🥦 ಜೀವಸತ್ವ ಮತ್ತು ಖನಿಜ (Vitamins & Minerals — regulators; colourful vegetables)",
                "🥜 ಆರೋಗ್ಯಕರ ಕೊಬ್ಬು (Healthy Fats — brain & energy; nuts, fish, seeds)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# PERSONAL HYGIENE IN ADOLESCENCE (KN) — Chapter 6 Sim 8
# =============================================================================
SIMULATIONS["personal_hygiene_kn"] = {
    "name": "ಕೌಮಾರದಲ್ಲಿ ವೈಯಕ್ತಿಕ ಶುಚಿತ್ವ (Personal Hygiene in Adolescence)",
    "language": "kannada",
    "description": (
        "7-item daily hygiene checklist. Students tap each item to mark it done; "
        "each check reveals a specific tip explaining the science behind that step. "
        "Includes a menstrual hygiene panel (for girls) covering product types, "
        "changing frequency, and safe disposal.\n"
        "Teaches why puberty increases hygiene needs (more sweat and oil glands) and "
        "which specific daily practices prevent body odour, acne, and infection."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter6_simulation8_hygiene_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Checklist State / ಪಟ್ಟಿ ಸ್ಥಿತಿ",
            "default": "initial",
            "options": ["initial", "all_complete"],
            "option_labels": [
                "ಆರಂಭಿಕ (Initial — empty checklist, 0/7 items done) [default]",
                "ಎಲ್ಲ ಪೂರ್ಣ (All Complete — all 7 items auto-checked with tips)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# HEALTHY HABITS FOR ADOLESCENTS (KN) — Chapter 6 Sim 9
# =============================================================================
SIMULATIONS["healthy_habits_kn"] = {
    "name": "ಕೌಮಾರ ವಯಸ್ಕರಿಗೆ ಆರೋಗ್ಯಕರ ಅಭ್ಯಾಸಗಳು (Healthy Habits for Adolescents)",
    "language": "kannada",
    "description": (
        "4-tab simulation covering the pillars of adolescent health: physical activity "
        "(60 min/day), sleep (8-10 hrs/night), healthy social life, and mental wellness. "
        "Animated icons and 4-point benefit lists for each habit. Online safety tips "
        "panel covers responsible internet use and cyberbullying response.\n"
        "Teaches evidence-based health habits and how each specifically supports the "
        "unique physiological and emotional needs of adolescence."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter6_simulation9_healthy_habits_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Habit Category / ಅಭ್ಯಾಸ ವಿಭಾಗ",
            "default": "exercise",
            "options": ["exercise", "sleep", "social", "mental"],
            "option_labels": [
                "⚽ ವ್ಯಾಯಾಮ (Exercise — 60 min/day; builds bones, mood, and focus) [default]",
                "😴 ನಿದ್ರೆ (Sleep — 8-10 hrs/night; growth hormone + memory consolidation)",
                "👥 ಸಾಮಾಜಿಕ (Social — healthy relationships; communication + emotional support)",
                "🧘 ಮಾನಸಿಕ (Mental — mindfulness + stress management + online safety)"
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
    "topic": "Science – Growing Up (ಬೆಳೆಯುವಿಕೆ)"
}


# =============================================================================
# WATER CONSERVATION (KN) — Chapter 7 Sim 10
# =============================================================================
SIMULATIONS["water_conservation_kn"] = {
    "name": "ಜಲ ಸಂರಕ್ಷಣೆ (Water Conservation)",
    "language": "kannada",
    "description": (
        "3-method animated simulation of water conservation techniques: "
        "(1) Rainwater harvesting — roof → gutter → pipe → storage tank animation; "
        "(2) Recharge pit — cross-section showing percolation through gravel + sand "
        "     layers back into the aquifer; "
        "(3) Ice Stupa (Ladakh) — night scene showing water spray freezing into an "
        "     artificial conical glacier that melts in summer for irrigation.\n"
        "Problem panel explains groundwater depletion: over-extraction and concrete "
        "blocking natural percolation. Teaches how each method directly addresses "
        "a different dimension of the water crisis."
    ),
    "base_url": (
        f"{GITHUB_PAGES_BASE_KN}"
        "/science_chapter7_simulation10_water_conservation_kn.html"
    ),
    "parameters": [
        {
            "name": "initialState",
            "type": "select",
            "display_name": "Conservation Method / ಸಂರಕ್ಷಣಾ ವಿಧಾನ",
            "default": "rwh",
            "options": ["rwh", "pit", "stupa"],
            "option_labels": [
                "🏠 ವರ್ಷಾಧಾರ ಸಂಗ್ರಹಣೆ (Rainwater Harvesting — roof collection → storage tank) [default]",
                "🕳️ ರಿಚಾರ್ಜ್ ಗುಂಡಿ (Recharge Pit — water percolating into aquifer)",
                "🏔️ ಐಸ್ ಸ್ತೂಪ (Ice Stupa — Ladakh artificial glacier, melts in summer)"
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
    "topic": "Science – Water: Our Lifeline (ನೀರು: ನಮ್ಮ ಜೀವನಾಡಿ)"
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
