# Android Integration Guide — Adaptive Teaching Agent

> **For the Android Developer**
> This document explains how the backend works, what APIs are available, and exactly what you need to build on the Android side to integrate the teaching agent with interactive simulations.

---

## Table of Contents

1. [What Is This System?](#1-what-is-this-system)
2. [How the Backend Works (Simple Overview)](#2-how-the-backend-works-simple-overview)
3. [Starting the Backend Server](#3-starting-the-backend-server)
4. [API Endpoints — Complete Reference](#4-api-endpoints--complete-reference)
5. [Full Session Response Structure](#5-full-session-response-structure)
6. [The Main Loop — How a Conversation Works](#6-the-main-loop--how-a-conversation-works)
7. [The Two-Way Communication (Most Important Part)](#7-the-two-way-communication-most-important-part)
8. [Quiz Mode](#8-quiz-mode)
9. [All Available Simulations](#9-all-available-simulations)
10. [What the Android Developer Needs to Build](#10-what-the-android-developer-needs-to-build)
11. [Screen-by-Screen UI Guide](#11-screen-by-screen-ui-guide)
12. [Error Handling](#12-error-handling)
13. [Session Recovery (Crash Handling)](#13-session-recovery-crash-handling)
14. [Real JSON Examples](#14-real-json-examples)

---

## 1. What Is This System?

This is an **AI-powered 1-on-1 tutoring system** for school students. It teaches science/math concepts using interactive HTML5 simulations.

**How it works:**
- The student sees a simulation (e.g., a swinging pendulum) inside the app
- An AI teacher talks to the student through a chat interface
- The AI teacher changes simulation parameters (e.g., makes the pendulum longer) to visually demonstrate concepts
- The student can also drag sliders in the simulation and the AI teacher responds to that
- After all concepts are taught, the student takes a quiz by setting simulation parameters themselves

**The key feature (2-way communication):**
- Agent → Student: AI changes simulation sliders to demonstrate things
- Student → Agent: Student drags simulation sliders and AI responds to what they explored

---

## 2. How the Backend Works (Simple Overview)

```
┌─────────────────────────────────────────────────────────────┐
│                      BACKEND (Python)                       │
│                                                             │
│   FastAPI Server  ←→  LangGraph AI Agent  ←→  Gemini LLM  │
│        │                      │                            │
│   REST API                Checkpointer                     │
│   (port 8000)           (PostgreSQL / RAM)                 │
└─────────────────────────────────────────────────────────────┘
          ↑
          │ HTTP REST calls
          ↓
┌─────────────────────────────────────────────────────────────┐
│                    ANDROID APP                              │
│                                                             │
│   Chat UI  +  WebView (HTML5 simulation)  +  Progress UI   │
└─────────────────────────────────────────────────────────────┘
```

**Key point for Android:** The Android app only talks to the FastAPI REST server. All AI logic, state management, and concept tracking happen on the backend. The app just sends HTTP requests and renders the responses.

**What the backend remembers per session:**
- Current concept being taught
- Student's understanding level (none → partial → mostly → complete)
- All simulation parameter changes made so far
- Whether it's in teaching mode or quiz mode

---

## 3. Starting the Backend Server

```bash
# Install dependencies
pip install -r requirements_api.txt

# Set environment variables in .env file (developer must provide these)
GOOGLE_API_KEY=...
GEMINI_MODEL=gemma-3-27b-it
POSTGRES_DATABASE_URL=...        # optional, uses RAM if missing
GITHUB_PAGES_BASE_URL=...        # base URL for simulation HTML files

# Start server
uvicorn api_server:app --host 0.0.0.0 --port 8000
```

- **API Base URL:** `http://<server-ip>:8000`
- **Interactive Docs:** `http://<server-ip>:8000/docs`  ← test all endpoints here before coding
- **CORS:** Already enabled for all origins (`*`), so Android can call it freely

---

## 4. API Endpoints — Complete Reference

### 4.1 Health Check
```
GET /
```
Use this on app launch to check if the server is running.

**Response:**
```json
{
  "status": "online",
  "service": "Teaching Agent API",
  "version": "1.0.0",
  "available_simulations": ["simple_pendulum", "earth_rotation_revolution", "light_shadows", ...]
}
```

---

### 4.2 List All Simulations
```
GET /api/simulations
```
Use this to populate the simulation picker screen.

**Response:**
```json
{
  "simulations": [
    {
      "id": "simple_pendulum",
      "title": "Time & Pendulums",
      "description": "Explore how pendulum length affects swing time",
      "concepts_count": 2
    },
    {
      "id": "light_shadows",
      "title": "Light & Shadows",
      "description": "...",
      "concepts_count": 3
    }
  ]
}
```

---

### 4.3 Start a Session
```
POST /api/session/start
HTTP 201 Created
```

**Request Body:**
```json
{
  "simulation_id": "simple_pendulum",
  "student_id": "student_12345",
  "language": "english"
}
```

| Field | Required | Values | Description |
|---|---|---|---|
| `simulation_id` | Yes | See Section 9 | Which simulation to teach |
| `student_id` | No | Any string | For your own tracking |
| `language` | No | `"english"` or `"kannada"` | Controls translation of all teacher messages |

**Returns:** Full `SessionResponse` (see Section 5)

**Save `session_id` from the response** — you will need it for every other call.

**Error Responses:**
| Code | Meaning |
|---|---|
| `400` | `simulation_id` not found — check available IDs |
| `500` | Server error |

---

### 4.4 Send Student Input (Main Interaction Endpoint)
```
POST /api/session/{session_id}/respond
```
This is the most-used endpoint. Called every time the student:
- Types a message
- Drags a simulation slider
- Does both at the same time

**Request Body:**
```json
{
  "student_response": "I think longer pendulum swings faster",
  "student_changed_params": null
}
```

| Field | Required | Description |
|---|---|---|
| `student_response` | No (defaults to `""`) | What the student typed. Send empty string if student only changed sliders. |
| `student_changed_params` | No (defaults to `null`) | Dict of slider changes student made. E.g. `{"length": 5}`. Null if student didn't touch sliders. |

**Three usage patterns:**

```json
// Student typed only
{ "student_response": "I think it swings faster", "student_changed_params": null }

// Student moved slider only
{ "student_response": "", "student_changed_params": {"length": 3} }

// Student did both
{ "student_response": "I made it shorter", "student_changed_params": {"length": 3} }
```

**Returns:** Full `SessionResponse` (see Section 5)

**Error Responses:**
| Code | Meaning |
|---|---|
| `404` | Session not found or expired. Make user start a new session. |
| `500` | Server error |

---

### 4.5 Get Session State (Recovery)
```
GET /api/session/{session_id}
```
Use this when the app is reopened and you need to restore the session.

**Returns:** Full `SessionResponse`

**Error:** `404` if session expired

---

### 4.6 Submit Quiz Answer
```
POST /api/session/{session_id}/submit-quiz
```
Used only during the quiz phase. The student sets the simulation parameters and taps "Submit".

**Request Body:**
```json
{
  "question_id": "pendulum_q1",
  "submitted_parameters": {
    "length": 5.0,
    "number_of_oscillations": 10
  },
  "attempt_number": 1
}
```

| Field | Required | Values | Description |
|---|---|---|---|
| `question_id` | Yes | From current teacher message | ID of the quiz question |
| `submitted_parameters` | Yes | Current slider values as dict | What the student set in the simulation |
| `attempt_number` | Yes | 1, 2, or 3 | Which attempt (max 3 per question) |

**Returns:** `QuizEvaluationResponse` (see Section 8)

---

## 5. Full Session Response Structure

Every call to `/start`, `/respond`, and `GET /session/{id}` returns this same structure:

```json
{
  "session_id": "api_session_3f8a1b2c",

  "simulation": {
    "id": "simple_pendulum",
    "title": "Time & Pendulums",
    "html_url": "https://...simple_pendulum.html?length=8&oscillations=10&autoStart=true",
    "show_simulation": true,
    "current_params": {
      "length": 8,
      "number_of_oscillations": 10
    },
    "param_change": {
      "parameter": "length",
      "before": 5,
      "after": 8,
      "reason": "To demonstrate that longer pendulum swings slower"
    }
  },

  "concepts": {
    "total": 2,
    "current_index": 0,
    "current_concept": {
      "id": 1,
      "title": "Time Period of a Pendulum",
      "description": "How the length of a pendulum affects how long it takes to complete one swing.",
      "key_insight": "Longer pendulum = longer time period (slower swings)",
      "related_params": ["length"]
    },
    "all_concepts": [...],
    "all_completed": false,
    "previous_concept": null
  },

  "teacher_message": {
    "text": "Not quite! A longer pendulum actually swings SLOWER. Watch the simulation now...",
    "timestamp": "2026-04-15T10:16:30Z",
    "requires_response": true,
    "correction_made": true,
    "asks_for_reasoning": false,
    "concept_transition": false,
    "session_ending": false
  },

  "learning_state": {
    "understanding_level": "none",
    "understanding_reasoning": "Student gave incorrect answer",
    "exchange_count": 1,
    "concept_complete": false,
    "session_complete": false,
    "strategy": "continue",
    "teacher_mode": "encouraging",
    "trajectory_status": "improving",
    "needs_deeper": false
  },

  "language": "english",

  "summary": null
}
```

### What Each Field Means and What to Do With It

**`simulation` object:**

| Field | Type | What to do |
|---|---|---|
| `html_url` | string | Load in WebView **only when** `show_simulation == true` |
| `show_simulation` | boolean | `true` = reload WebView now. `false` = this is a text-only turn, do NOT refresh the WebView |
| `current_params` | dict | Current parameter values (for reading current slider state) |
| `param_change` | object or null | If not null, optionally show a pill like "Length: 5 → 8" |

**`teacher_message` object:**

| Field | Type | What to do |
|---|---|---|
| `text` | string | Always display this in the chat |
| `requires_response` | boolean | `true` = show the text input. `false` = hide input (session ending) |
| `correction_made` | boolean | Optionally style the message differently (e.g. amber border) |
| `concept_transition` | boolean | Optionally show a concept transition animation/banner |
| `session_ending` | boolean | Show "Session Complete" state |

**`learning_state` object:**

| Field | Type | What to do |
|---|---|---|
| `understanding_level` | string | `"none"` / `"partial"` / `"mostly"` / `"complete"` — update progress bar |
| `session_complete` | boolean | `true` = show summary screen |
| `concept_complete` | boolean | `true` = student mastered current concept |
| `exchange_count` | int | How many messages exchanged for this concept |

**`concepts` object:**

| Field | Type | What to do |
|---|---|---|
| `current_index` | int | Current concept number (0-based) |
| `total` | int | Total concepts |
| `current_concept.title` | string | Show in header/chip |
| `all_completed` | boolean | All concepts done → quiz mode starts automatically next turn |

**`summary` object** (only present when `session_complete == true`):
```json
{
  "concepts_mastered": 2,
  "total_exchanges": 12,
  "parameter_changes_made": 5,
  "understanding_progression": ["none", "partial", "mostly", "complete"]
}
```
Show this on the results/summary screen.

---

## 6. The Main Loop — How a Conversation Works

```
App Launch
    │
    ▼
GET /                          ← check server health
    │
    ▼
Student picks simulation
    │
    ▼
POST /api/session/start        ← save session_id in SharedPreferences
    │
    ▼
Show teacher_message.text      ← display in chat
Show simulation in WebView     ← load html_url (show_simulation = true on start)
    │
    ▼
Student types / moves slider
    │
    ▼
POST /api/session/{id}/respond ← send student input
    │
    ├─→ if show_simulation == true  → reload WebView with html_url
    ├─→ if param_change != null     → show "param: old → new" indicator
    ├─→ always show teacher_message.text in chat
    ├─→ update progress bar from learning_state.understanding_level
    │
    └─→ if session_complete == true → go to Summary Screen
        if concepts.all_completed == true → backend switches to Quiz Mode automatically
                                           (teacher message will contain quiz challenge)
```

---

## 7. The Two-Way Communication (Most Important Part)

This is the critical feature: **the simulation runs in a WebView, and when the student drags a slider, the Android app must capture that change and send it to the API.**

### How the HTML Simulations Work

The simulation HTML files (hosted on GitHub Pages) run inside a WebView. When the student drags a slider in the simulation, the HTML fires a `postMessage` event like this:

```json
{"type": "simulation_params", "params": {"length": 5}}
```
or just raw:
```json
{"length": 5}
```

Different simulations may use slightly different message formats, but all of them send a JSON object containing the changed parameter values.

### What Android Needs to Do

**Step 1: Enable JavaScript and inject a bridge script into the WebView**

```kotlin
webView.settings.javaScriptEnabled = true
webView.settings.domStorageEnabled = true

// Inject JS to forward postMessage events to Android
webView.webViewClient = object : WebViewClient() {
    override fun onPageFinished(view: WebView?, url: String?) {
        // Inject bridge: catch postMessages from simulation and call Android
        view?.evaluateJavascript("""
            window.addEventListener('message', function(event) {
                var data = event.data;
                if (typeof data === 'string') {
                    try { data = JSON.parse(data); } catch(e) {}
                }
                if (typeof data === 'object' && data !== null) {
                    Android.onSimulationUpdate(JSON.stringify(data));
                }
            });
        """.trimIndent(), null)
    }
}

// Add the Android bridge
webView.addJavascriptInterface(SimulationBridge(viewModel), "Android")
```

**Step 2: Create the bridge class**

```kotlin
class SimulationBridge(private val viewModel: TeachingViewModel) {

    @JavascriptInterface
    fun onSimulationUpdate(paramsJson: String) {
        try {
            val jsonObj = JSONObject(paramsJson)

            // Extract params - handle multiple message formats
            val params = when {
                jsonObj.has("params") -> jsonObj.getJSONObject("params")
                jsonObj.has("simulation_params") -> jsonObj.getJSONObject("simulation_params")
                else -> jsonObj  // raw format
            }

            // Filter out non-param fields
            val paramMap = mutableMapOf<String, Any>()
            val ignoredKeys = setOf("type", "__t", "autoStart")
            params.keys().forEach { key ->
                if (key !in ignoredKeys) {
                    paramMap[key] = params.get(key)
                }
            }

            if (paramMap.isNotEmpty()) {
                // Store pending slider changes
                viewModel.setPendingSliderChanges(paramMap)
            }
        } catch (e: Exception) {
            // Ignore malformed messages
        }
    }
}
```

**Step 3: Handle the "first load echo" problem**

When a simulation HTML loads, it fires a `postMessage` immediately with its initial/default params (autostart behavior). This must be ignored — it is NOT a student interaction.

```kotlin
class TeachingViewModel : ViewModel() {

    private var baselineParamsRecorded = false
    private var baselineParams: Map<String, Any> = emptyMap()
    private var _pendingSliderChanges = MutableStateFlow<Map<String, Any>?>(null)
    val pendingSliderChanges = _pendingSliderChanges.asStateFlow()

    fun onNewSimulationLoaded() {
        // Reset baseline whenever a new simulation URL is loaded
        baselineParamsRecorded = false
        baselineParams = emptyMap()
    }

    fun setPendingSliderChanges(params: Map<String, Any>) {
        if (!baselineParamsRecorded) {
            // First message after load = baseline (autostart echo), ignore it
            baselineParams = params
            baselineParamsRecorded = true
            return
        }

        // Only save if params differ from baseline (real student interaction)
        if (params != baselineParams) {
            _pendingSliderChanges.value = params
        }
    }

    fun clearPendingSliderChanges() {
        _pendingSliderChanges.value = null
    }
}
```

**Step 4: Send slider changes when student taps Send**

```kotlin
fun onSendButtonClicked(typedText: String) {
    val sliderChanges = _pendingSliderChanges.value

    // Build request
    val request = StudentResponseRequest(
        studentResponse = typedText,
        studentChangedParams = sliderChanges  // null if no slider changes
    )

    // Clear pending changes immediately
    clearPendingSliderChanges()

    // Call API
    sendStudentResponse(sessionId, request)
}
```

**Step 5: (Optional) Auto-send slider changes without typing**

Add a "Send Slider Changes" button that appears only when `pendingSliderChanges != null`:

```kotlin
// In UI: show this button only when there are pending slider changes
if (pendingSliderChanges != null) {
    Button(onClick = { onSendButtonClicked("") }) {
        Text("Send My Changes")
    }
}
```

### The Complete Flow Visualized

```
Student drags slider in WebView
         │
         ▼
HTML postMessage fires: {"length": 5}
         │
         ▼
Android SimulationBridge.onSimulationUpdate() called
         │
         ├── Is this the first message after load? → YES → ignore (baseline echo)
         │
         └── Params differ from baseline? → YES → store in pendingSliderChanges
                                                          │
                                            Student taps Send button
                                                          │
                                                          ▼
                                POST /respond { student_changed_params: {"length": 5} }
                                                          │
                                                          ▼
                                Backend: AI acknowledges the exploration
                                         merges params into current_params
                                         sets show_simulation = true
                                                          │
                                                          ▼
                                Response: show_simulation=true, new html_url
                                                          │
                                                          ▼
                                Reload WebView with new URL (slider confirmed by agent)
```

---

## 8. Quiz Mode

Quiz mode starts **automatically** — you do not need to call a different endpoint. When all teaching concepts are complete, the backend transitions to quiz mode internally. The next `SessionResponse` will have a teacher message containing the quiz challenge text.

### How to Detect Quiz Mode

```kotlin
// In your response handler:
if (response.concepts.allCompleted && !response.learningState.sessionComplete) {
    // Quiz mode has started or is ongoing
    // The teacher_message.text will contain the challenge
    showQuizSubmitButton = true
}
```

### Quiz UI Flow

```
Teacher message contains: "Set the pendulum so it takes 2 seconds per swing. Try it!"
         │
         ▼
Student adjusts sliders in WebView
         │
         ▼
Student taps "Submit Answer" button
         │
         ▼
Read current slider values from WebView (or from last postMessage)
         │
         ▼
POST /api/session/{id}/submit-quiz
{
  "question_id": "pendulum_q1",          // from teacher message or stored state
  "submitted_parameters": {"length": 5},  // what sliders are set to right now
  "attempt_number": 1
}
         │
         ▼
Handle QuizEvaluationResponse:
  - Show feedback text
  - if allow_retry == true  → let student try again (increment attempt_number)
  - if next_question != null → load next question
  - if quiz_complete == true → go to summary screen
```

### Quiz Evaluation Response

```json
{
  "session_id": "api_session_abc123",
  "question_id": "pendulum_q1",
  "score": 0.5,
  "status": "PARTIALLY_RIGHT",
  "feedback": "Close! The pendulum is a bit too short. Try making it a bit longer.",
  "attempt": 1,
  "allow_retry": true,
  "quiz_complete": false,
  "quiz_progress": {
    "current_question": 1,
    "total_questions": 2,
    "questions_completed": 0,
    "questions_remaining": 2,
    "average_score": 0.5,
    "perfect_count": 0,
    "partial_count": 1,
    "wrong_count": 0
  },
  "next_question": null
}
```

| `status` | `score` | `allow_retry` | Action |
|---|---|---|---|
| `RIGHT` | `1.0` | `false` | Show success animation, check `next_question` |
| `PARTIALLY_RIGHT` | `0.5` | `true` | Show feedback, let student retry |
| `WRONG` | `0.0` | `true` | Show feedback, let student retry |
| Any | Any | `false` (after 3 tries) | Move to next question regardless |

When `next_question != null`, load the new question's challenge text.
When `quiz_complete == true`, the session is fully done — show summary screen.

---

## 9. All Available Simulations

### English Simulations

| ID | Title | Parameters |
|---|---|---|
| `simple_pendulum` | Time & Pendulums | `length`, `number_of_oscillations` |
| `simple_pendulum_new` | Time & Pendulums (v2) | `length`, `number_of_oscillations` |
| `earth_rotation_revolution` | Earth's Rotation & Revolution | `rotationSpeed`, `revolutionSpeed` |
| `light_shadows` | Light & Shadows | `lightDistance`, `objectType`, `objectSize` |
| `parallel_lines_angles` | Parallel Lines & Transversal | angle-related params |
| `speed_race` | Speed Race | `speed`, `time` |
| `time_units` | Time Units | `hours`, `minutes`, `seconds` |
| `speed_calculator` | Speed Calculator | `distance`, `time` |
| `brackets_signs` | Brackets & Signs | expression params |
| `distributive` | Distributive Property | expression params |
| `angle_sum_property` | Angle Sum Property | angle params |
| `angle_sum_interactive` | Angle Sum Interactive | angle params |

### Kannada Simulations (use with `language: "kannada"`)

Use IDs: `brackets_signs_kn`, `distributive_kn`, `expression_compare_kn`, `expression_engineer_kn`, `decimal_number_line_kn`, and others. Fetch the full list from `GET /api/simulations`.

---

## 10. What the Android Developer Needs to Build

This section is a checklist of everything that needs to be implemented on the Android side.

### 10.1 Networking Layer

- [ ] HTTP client setup (Retrofit or OkHttp recommended)
- [ ] Base URL configuration (configurable for dev/prod)
- [ ] All 6 API endpoints implemented as Retrofit interfaces or equivalent
- [ ] JSON deserialization for `SessionResponse` and `QuizEvaluationResponse`
- [ ] Global error handler for `404` (session expired) and `500` (server error)
- [ ] Loading state management during API calls (disable input while waiting)

**Retrofit interface example:**
```kotlin
interface TeachingApi {
    @GET("/")
    suspend fun healthCheck(): HealthCheckResponse

    @GET("/api/simulations")
    suspend fun listSimulations(): SimulationsListResponse

    @POST("/api/session/start")
    suspend fun startSession(@Body request: StartSessionRequest): SessionResponse

    @POST("/api/session/{sessionId}/respond")
    suspend fun sendResponse(
        @Path("sessionId") sessionId: String,
        @Body request: StudentResponseRequest
    ): SessionResponse

    @GET("/api/session/{sessionId}")
    suspend fun getSession(@Path("sessionId") sessionId: String): SessionResponse

    @POST("/api/session/{sessionId}/submit-quiz")
    suspend fun submitQuiz(
        @Path("sessionId") sessionId: String,
        @Body request: QuizSubmissionRequest
    ): QuizEvaluationResponse
}
```

### 10.2 Data Models (Kotlin Data Classes)

Create Kotlin data classes matching the JSON structures.

**Core classes needed:**
```kotlin
data class StartSessionRequest(
    val simulation_id: String,
    val student_id: String? = null,
    val language: String = "english"
)

data class StudentResponseRequest(
    val student_response: String = "",
    val student_changed_params: Map<String, Any>? = null
)

data class QuizSubmissionRequest(
    val question_id: String,
    val submitted_parameters: Map<String, Any>,
    val attempt_number: Int
)

data class SessionResponse(
    val session_id: String,
    val simulation: SimulationState,
    val concepts: ConceptsState,
    val teacher_message: TeacherMessage,
    val learning_state: LearningState,
    val language: String,
    val summary: Map<String, Any>?
)

data class SimulationState(
    val id: String,
    val title: String,
    val html_url: String,
    val show_simulation: Boolean,
    val current_params: Map<String, Any>,
    val param_change: ParameterChange?
)

data class ParameterChange(
    val parameter: String,
    val before: Any,
    val after: Any,
    val reason: String
)

data class TeacherMessage(
    val text: String,
    val timestamp: String,
    val requires_response: Boolean,
    val correction_made: Boolean = false,
    val asks_for_reasoning: Boolean = false,
    val concept_transition: Boolean = false,
    val session_ending: Boolean = false
)

data class LearningState(
    val understanding_level: String,
    val understanding_reasoning: String?,
    val exchange_count: Int,
    val concept_complete: Boolean,
    val session_complete: Boolean,
    val strategy: String,
    val teacher_mode: String,
    val trajectory_status: String?,
    val needs_deeper: Boolean
)

data class ConceptsState(
    val total: Int,
    val current_index: Int,
    val current_concept: ConceptInfo?,
    val all_concepts: List<ConceptInfo>,
    val all_completed: Boolean,
    val previous_concept: Map<String, Any>?
)

data class ConceptInfo(
    val id: Int,
    val title: String,
    val description: String,
    val key_insight: String,
    val related_params: List<String>
)
```

### 10.3 Session State Management

- [ ] Store `session_id` in SharedPreferences immediately after `/start`
- [ ] On app launch, check SharedPreferences for existing `session_id`
- [ ] If found, call `GET /api/session/{session_id}` to restore state
- [ ] If `404` returned (session expired), start a fresh session
- [ ] Clear `session_id` from SharedPreferences when session is complete

```kotlin
class SessionManager(private val prefs: SharedPreferences) {
    fun saveSessionId(sessionId: String) = prefs.edit().putString("session_id", sessionId).apply()
    fun getSessionId(): String? = prefs.getString("session_id", null)
    fun clearSessionId() = prefs.edit().remove("session_id").apply()
}
```

### 10.4 WebView Setup

- [ ] Create a `WebView` in the teaching screen layout
- [ ] Enable JavaScript: `webView.settings.javaScriptEnabled = true`
- [ ] Enable DOM storage: `webView.settings.domStorageEnabled = true`
- [ ] Inject the postMessage bridge script on `onPageFinished`
- [ ] Add `SimulationBridge` as a JavaScript interface named `"Android"`
- [ ] Implement baseline echo filter (ignore first postMessage after each URL load)
- [ ] Store pending slider changes in ViewModel
- [ ] On `show_simulation == true` in response: call `webView.loadUrl(response.simulation.html_url)`
- [ ] On `show_simulation == false`: do NOT reload the WebView (leave it as-is)

### 10.5 Chat UI

- [ ] Scrollable list of chat messages (RecyclerView or LazyColumn)
- [ ] Teacher message bubble (left-aligned)
- [ ] Optional: different styling for `correction_made == true` messages
- [ ] Optional: concept transition banner when `concept_transition == true`
- [ ] Text input field + Send button at the bottom
- [ ] Hide/disable input when `requires_response == false`
- [ ] Loading indicator while API call is in progress (disable Send button)

### 10.6 Progress UI

- [ ] Concept progress indicator: `current_index + 1 / total` (e.g., "Concept 1 of 2")
- [ ] Understanding level badge: `"none"` → `"partial"` → `"mostly"` → `"complete"`
- [ ] Optional: parameter change pill (when `param_change != null`): "length: 5 → 8"

### 10.7 Quiz UI

- [ ] Detect quiz mode: `concepts.all_completed == true`
- [ ] Show "Submit Answer" button (in place of or alongside Send)
- [ ] On submit: read current slider state, call `/submit-quiz`
- [ ] Display quiz feedback from `QuizEvaluationResponse.feedback`
- [ ] Handle retry logic (track `attempt_number` locally, max 3)
- [ ] Show quiz progress: `quiz_progress.questions_completed / quiz_progress.total_questions`
- [ ] When `quiz_complete == true`: navigate to summary screen

### 10.8 Summary Screen

Show when `learning_state.session_complete == true`:

```
Concepts Mastered: 2/2
Total Exchanges:   12
Slider Changes:    5
Understanding:     none → partial → mostly → complete
[Start New Session Button]
```

---

## 11. Screen-by-Screen UI Guide

### Screen 1: Home / Simulation Picker
- Call `GET /api/simulations` on load
- Display list of simulations with title and description
- Student taps one → go to Teaching Screen

### Screen 2: Teaching Screen (Main Screen)

**Layout:**
```
┌─────────────────────────────────────┐
│  [Back]  Time & Pendulums  Concept 1/2  │  ← header
│  [====●==========] Understanding: Partial │  ← progress
├─────────────────────────────────────┤
│                                     │
│  ┌──────────────────────────────┐   │
│  │   WebView: simulation HTML   │   │  ← simulation (shown conditionally)
│  └──────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐    │
│  │ Teacher: "What do you think │    │  ← chat messages
│  │ happens when we make it...  │    │
│  └─────────────────────────────┘    │
│                                     │
│  ┌─────────────────────────────┐    │
│  │ You: "It swings faster?"    │    │
│  └─────────────────────────────┘    │
│                                     │
├─────────────────────────────────────┤
│  [Type your answer...    ] [Send]   │  ← input
└─────────────────────────────────────┘
```

**Behaviors:**
- Simulation is shown/hidden based on `show_simulation`
- Input is enabled/disabled based on `requires_response`
- If `concepts.all_completed`: show "Submit Answer" button for quiz

### Screen 3: Summary Screen
- Show when `session_complete == true`
- Display summary data from response
- "Start a New Session" button → clear session_id → go to Screen 1

---

## 12. Error Handling

| HTTP Status | Cause | What to Show |
|---|---|---|
| `400` | Bad simulation ID | "This simulation is not available" |
| `404` | Session expired | "Your session has expired. Please start again." + clear session_id |
| `500` | Server error | "Something went wrong. Please try again." |
| Network timeout | No connectivity | "Check your internet connection" |

**Important:** For `404` on session recovery, clear the stored `session_id` and take the user to the home screen to start fresh.

---

## 13. Session Recovery (Crash Handling)

```kotlin
// On app launch (in ViewModel init or SplashActivity)
val savedSessionId = sessionManager.getSessionId()

if (savedSessionId != null) {
    viewModelScope.launch {
        try {
            val response = api.getSession(savedSessionId)
            // Session alive: restore UI from response
            restoreSession(response)
        } catch (e: HttpException) {
            if (e.code() == 404) {
                // Session expired on server
                sessionManager.clearSessionId()
                navigateToHome()
            }
        }
    }
} else {
    navigateToHome()
}
```

---

## 14. Real JSON Examples

These are real request/response pairs you can use to test your implementation.

### Example A: Starting a session

**Request:**
```
POST /api/session/start
{
  "simulation_id": "simple_pendulum",
  "language": "english"
}
```

**Response:**
```json
{
  "session_id": "api_session_3f8a1b2c",
  "simulation": {
    "id": "simple_pendulum",
    "title": "Time & Pendulums",
    "html_url": "https://imhv0609.github.io/simulation_to_concept_version3_github/simulations/simple_pendulum.html?length=5&oscillations=10&autoStart=true",
    "show_simulation": true,
    "current_params": {"length": 5, "number_of_oscillations": 10},
    "param_change": null
  },
  "concepts": {
    "total": 2,
    "current_index": 0,
    "current_concept": {
      "id": 1,
      "title": "Time Period of a Pendulum",
      "description": "How the length of a pendulum affects swing time.",
      "key_insight": "Longer pendulum = longer time period (slower swings)",
      "related_params": ["length"]
    },
    "all_concepts": [...],
    "all_completed": false,
    "previous_concept": null
  },
  "teacher_message": {
    "text": "Hi friend! Today we're going to explore pendulums... What do you think happens to the swing when we make the pendulum longer?",
    "timestamp": "2026-04-15T10:15:00Z",
    "requires_response": true,
    "correction_made": false,
    "session_ending": false
  },
  "learning_state": {
    "understanding_level": "none",
    "exchange_count": 0,
    "concept_complete": false,
    "session_complete": false,
    "strategy": "continue",
    "teacher_mode": "encouraging"
  },
  "language": "english",
  "summary": null
}
```

---

### Example B: Student types a wrong answer

**Request:**
```
POST /api/session/api_session_3f8a1b2c/respond
{
  "student_response": "I think it swings faster?",
  "student_changed_params": null
}
```

**Response (agent changes simulation parameter to demonstrate):**
```json
{
  "simulation": {
    "html_url": "...simple_pendulum.html?length=8&oscillations=10&autoStart=true",
    "show_simulation": true,
    "current_params": {"length": 8, "number_of_oscillations": 10},
    "param_change": {
      "parameter": "length",
      "before": 5,
      "after": 8,
      "reason": "To demonstrate that longer pendulum swings slower"
    }
  },
  "teacher_message": {
    "text": "Not quite, friend. Actually, a longer pendulum swings SLOWER. I've changed the length from 5 to 8. Watch the simulation now — do you see how it takes more time?",
    "requires_response": true,
    "correction_made": true
  },
  "learning_state": {
    "understanding_level": "none",
    "exchange_count": 1
  }
}
```

---

### Example C: Student drags a slider themselves

**Request:**
```
POST /api/session/api_session_3f8a1b2c/respond
{
  "student_response": "",
  "student_changed_params": {"length": 3}
}
```

**Response (agent acknowledges with excitement, simulation updates):**
```json
{
  "simulation": {
    "html_url": "...simple_pendulum.html?length=3&oscillations=10&autoStart=true",
    "show_simulation": true,
    "current_params": {"length": 3, "number_of_oscillations": 10},
    "param_change": {
      "parameter": "length",
      "before": 5,
      "after": 3,
      "reason": "Student explored by changing length"
    }
  },
  "teacher_message": {
    "text": "Oh interesting! You made the pendulum shorter! What did you notice — does it swing faster or slower compared to before?",
    "requires_response": true,
    "correction_made": false
  }
}
```

---

### Example D: Session complete with summary

**Response (when final concept mastered):**
```json
{
  "teacher_message": {
    "text": "Excellent! You've understood both concepts perfectly. Great job exploring pendulums!",
    "requires_response": false,
    "session_ending": true
  },
  "learning_state": {
    "understanding_level": "complete",
    "session_complete": true
  },
  "summary": {
    "concepts_mastered": 2,
    "total_exchanges": 9,
    "parameter_changes_made": 4,
    "understanding_progression": ["none", "none", "partial", "mostly", "complete"]
  }
}
```

---

## Quick Decision Checklist (for Every API Response)

```
On every SessionResponse:
  ✅ Always → show teacher_message.text in chat
  ✅ if show_simulation == true → reload WebView with html_url
  ✅ if show_simulation == false → do NOT touch the WebView
  ✅ if param_change != null → optionally show change indicator
  ✅ if requires_response == false → hide/disable text input
  ✅ if session_complete == true → navigate to summary screen
  ✅ if concepts.all_completed == true → switch to quiz UI mode
  ✅ always → update progress indicators from learning_state + concepts
```

---

*Backend codebase: `simulation_to_concept_version3_github_modified/`*
*API server file: `api_server.py` | Models: `api_models.py` | Logic: `api_integration.py`*
*Start server: `uvicorn api_server:app --host 0.0.0.0 --port 8000`*
*Interactive docs: `http://<server>:8000/docs`*
