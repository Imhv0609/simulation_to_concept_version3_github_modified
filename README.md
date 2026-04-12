# Adaptive Teaching Backend: Two-Way Communication Guide

This README explains only the core backend two-way communication in simple terms.

Scope of this document:
- Included: FastAPI + LangGraph session communication used by Android integration
- Excluded: Streamlit/frontend bridge details

It covers:
- How the app talks to the backend
- How the backend replies
- How simulation parameter changes move in both directions
- How session state is preserved across turns
- How quiz mode communication works

## 1. Big Picture

There are two communication loops happening together:

1. App/API loop (text + state)
- Client sends a request to FastAPI
- Backend processes the request through LangGraph
- Backend returns updated teaching state

2. Simulation loop (parameters)
- Backend can push simulation parameters to client
- Student can change simulation sliders
- Client sends student-changed parameters back to backend in next turn

Together, this gives true two-way communication: both teacher-agent and student can influence the simulation and the conversation.

## 2. Main Files and Roles

- `api_server.py`
  - FastAPI routes (start session, respond, restore session, submit quiz, list simulations)
- `api_integration.py`
  - Converts between API format and internal LangGraph state
  - Stores per-session language and simulation mappings
- `api_models.py`
  - Pydantic request/response contracts
- `graph.py`
  - LangGraph workflow, interrupt points, checkpointing, session continuation
- `state.py`
  - Complete shared state schema (`TeachingState`)
- `nodes/content_loader.py`
  - Loads concepts for selected simulation
- `nodes/teacher.py`
  - Generates teacher response and decides simulation display hints
- `nodes/evaluator.py`
  - Classifies student input and evaluates understanding
- `nodes/trajectory.py`
  - Detects improving/stagnating/regressing learning trend
- `nodes/strategy.py`
  - Chooses next teaching strategy and advancement logic
- `nodes/quiz_evaluator.py`
  - Quiz initialization, evaluation, and quiz routing

## 3. Backend API Endpoints

Base service: `api_server.py`

- `GET /`
  - Health check
- `POST /api/session/start`
  - Starts a new teaching session
- `POST /api/session/{session_id}/respond`
  - Sends student response and optional student-changed simulation params
- `GET /api/session/{session_id}`
  - Restores current session state
- `POST /api/session/{session_id}/submit-quiz`
  - Evaluates quiz submission
- `GET /api/simulations`
  - Returns supported simulation IDs and metadata

## 4. Data Contracts (Simple View)

### 4.1 Start Session Request

```json
{
  "simulation_id": "simple_pendulum",
  "student_id": "student_12345",
  "language": "english"
}
```

### 4.2 Student Response Request

```json
{
  "student_response": "I think shorter length swings faster",
  "student_changed_params": {
    "length": 3,
    "number_of_oscillations": 10
  }
}
```

`student_response` may be empty if student only changed simulation controls.

### 4.3 Session Response (Important Fields)

```json
{
  "session_id": "api_session_xxxxxxxx",
  "simulation": {
    "id": "simple_pendulum",
    "html_url": "...",
    "show_simulation": true,
    "current_params": {
      "length": 3,
      "number_of_oscillations": 10
    },
    "param_change": {
      "parameter": "length",
      "before": 5,
      "after": 3,
      "reason": "..."
    }
  },
  "teacher_message": {
    "text": "Great observation...",
    "requires_response": true
  },
  "learning_state": {
    "understanding_level": "partial",
    "strategy": "continue",
    "session_complete": false
  }
}
```

## 5. Two-Way Communication Flow (Step by Step)

## A. Session Start

1. Client calls `POST /api/session/start`.
2. `api_server.py` validates simulation and calls `create_teaching_session(...)`.
3. `api_integration.py` builds initial state with:
   - selected simulation
   - initial params
   - language
4. `graph.start_session(...)` runs graph until interrupt.
5. Interrupt is configured before evaluator, so first teacher message is ready and backend waits for student input.
6. API returns session response with:
   - `session_id`
   - current simulation URL and params
   - first teacher message

## B. Student -> Backend (Direction 1)

1. Student sends text and/or manual simulation changes.
2. Client calls `POST /api/session/{session_id}/respond`.
3. Backend receives:
   - `student_response`
   - `student_changed_params` (optional)
4. `graph.continue_session(...)` writes this into checkpointed state.
5. Graph resumes from interrupt and processes nodes:
   - `evaluator` -> `trajectory` -> `strategy` -> `teacher`
6. Updated state is returned as API response.

## C. Backend -> Student (Direction 2)

In the response, backend sends:
- Teacher feedback message
- Updated learning state
- `simulation.current_params`
- `simulation.show_simulation` flag
- Optional `simulation.param_change` metadata

Client uses this to show text, progress, and simulation updates.

## D. Student Parameter Changes -> Backend (Reverse Parameter Flow)

This is the most important part of two-sided communication.

1. Student changes simulation controls in the client app (Android).
2. Android collects changed parameter values.
3. Android sends them in `/api/session/{session_id}/respond` as `student_changed_params`.
4. Backend writes these into session state and marks `student_changed_params_this_turn = true`.
5. Evaluator and strategy use this flag to treat exploration turns correctly (instead of misclassifying them as normal text-only answers).

Result: student actions in the simulation directly influence the teaching logic.

### D.1 What Happens Inside Nodes When Student Parameters Are Changed

When Android sends `student_changed_params`, the same graph pipeline runs, but node behavior changes in a specific way:

1. `graph.continue_session(...)` stage
- The backend writes:
  - `student_changed_params = {...}`
  - `student_changed_params_this_turn = true`
- Then it resumes execution from the interrupt point.

2. `evaluator` node behavior
- It detects `student_changed_params_this_turn = true`.
- It short-circuits normal LLM answer evaluation.
- It returns `response_type = "student_param_change"`.
- It preserves existing understanding instead of marking the student wrong.

3. `trajectory` node behavior
- It still executes in the pipeline.
- Since understanding was preserved during the evaluator short-circuit, this turn does not force an artificial regression.

4. `strategy` node behavior
- It checks `response_type`.
- If `response_type == "student_param_change"`, it takes the exploration branch:
  - keeps current strategy (no major strategy switch)
  - sets teacher mode to encouraging
  - does not scaffold
  - does not increment `exchange_count`
- This makes exploration turns effectively "free" and avoids penalizing curiosity.

5. `teacher` node behavior
- It reads the student-changed parameter values.
- It generates a response that acknowledges the student's action and asks for observation (not right/wrong grading).
- It merges student values into `current_params`.
- It appends parameter history entries with `initiated_by = "student"`.
- It sets `show_simulation = true` for that turn.
- It resets:
  - `student_changed_params_this_turn = false`
  - `student_changed_params = {}`

Net effect: when a student changes parameters, the backend treats that turn as exploratory behavior, preserves learning-state integrity, updates simulation state from student input, and continues teaching from the new state.

## 6. Internal Graph Flow and Interrupt Model

Graph core in `graph.py`:

Teaching path:
- `content_loader` -> `teacher` -> [interrupt] -> `evaluator` -> `trajectory` -> `strategy` -> (loop)

Quiz path:
- `quiz_initializer` -> `quiz_teacher` -> [interrupt] -> `quiz_evaluator` -> (retry/next/end)

Interrupts are configured with:
- `interrupt_before=["evaluator", "quiz_evaluator"]`

Meaning:
- Graph pauses after teacher speaks
- Backend waits for next student input
- Next API call resumes from correct checkpoint

## 7. Session Persistence and Recovery

The backend uses a checkpointer:
- Primary: PostgreSQL (`PostgresSaver`) when `POSTGRES_DATABASE_URL` is configured
- Fallback: in-memory (`MemorySaver`) if Postgres is unavailable

Why this matters:
- `session_id` maps to graph thread state
- Client can call `GET /api/session/{session_id}` to recover current state
- Multi-turn conversations stay consistent without re-sending full history

## 8. How Parameter Updates Are Decided

Parameter updates can originate from two places:

1. Agent-driven
- Teacher node decides to demonstrate concept with parameter change
- Change is appended to `parameter_history`
- Response may set `show_simulation=true`

2. Student-driven
- Student changes controls in the Android app
- Android sends `student_changed_params`
- Backend records this as student-initiated change

To avoid noise:
- `show_simulation` controls whether UI should render/update simulation this turn
- `param_change` in API is only returned when relevant for current turn

## 9. Language Flow (English/Kannada)

Language handling is done at API boundary:

- Internal graph logic stays in English for stable evaluation
- Incoming student text can be translated to English
- Outgoing teacher/messages can be translated back (for example Kannada)
- Session language is tracked per `session_id`

This keeps model behavior consistent while still supporting multilingual UX.

## 10. Error Handling Behavior

Common API behaviors:

- Invalid simulation -> `400`
- Missing/expired session -> `404`
- Wrong quiz state or invalid request -> `400`
- Unexpected backend failure -> `500`

All routes return structured JSON details for easier app-side handling.





