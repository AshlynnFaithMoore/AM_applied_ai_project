# PawPal+: AI-Assisted Pet Care Planner

## Original Project (Modules 1-3)
My original project from Modules 1-3 is **PawPal+**, an AI-assisted pet care planner that helps owners organize daily care tasks across one or more pets. The original goal was to model owner constraints, pet needs, and task priority so the system could produce explainable daily schedules instead of a static to-do list. Over the module sequence, it evolved from class design and UML into a tested scheduling engine with validation, recurrence handling, and a Streamlit interface.

## Title and Summary
PawPal+ generates practical, explainable pet-care schedules using owner time limits, task urgency, and due-time constraints. This matters because pet care is repetitive and high-stakes: missing feeding or medication can affect health, while overloading owners leads to skipped tasks. The project demonstrates how structured AI-style planning can make day-to-day routines more reliable and transparent.

## Architecture Overview
The system combines a target AI architecture view and the current implemented core:

- **Integrated RAG + agentic pipeline (in main app logic):** `app.py` now calls `Scheduler.generate_agentic_plan(...)`, which retrieves pet-care knowledge, applies guardrails, and then generates the schedule.
- **Retriever behavior:** `Scheduler.retrieve_knowledge(...)` selects context snippets from a local knowledge base (feeding guidance, medication safety, breed-specific needs) based on the user question, symptom notes, medications, pet species, and active tasks.
- **Agentic behavior:** guardrails can insert an urgent task (for red-flag symptoms), escalate overdue medication tasks, and flag medication interaction risks before scheduling.
- **Implemented core** still uses Owner/Pet/Task domain models, deterministic ranking, explanation output, and conflict-warning detection.
- **Human and test checkpoints** are explicit: users review generated plans/warnings, and pytest validates ranking, filtering, recurrence, and conflict logic.

System diagram assets:

- Source diagram: `assets/pawpal_target_architecture.mmd`
- Rendered diagram: `assets/pawpal_target_architecture.svg`

![PawPal Target Architecture](assets/pawpal_target_architecture.svg)

## Setup Instructions
1. Clone this repository and move into the project directory.
2. Use Python 3.12+ (validated on Python 3.12.1).
3. Create a virtual environment.
4. Activate the environment.
5. Install dependencies from `requirements.txt`.
6. Run the Streamlit app.

```bash
git clone <your-repo-url>
cd AM_applied_ai_project-1
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Reproducibility checks:

```bash
python -m pytest -q
python main.py
```

What to verify in the UI after `streamlit run app.py`:

1. Enter AI Context Inputs (`Question for AI planner`, `Symptoms observed`, `Active medications`).
2. Click `Generate schedule`.
3. Confirm the app shows AI Confidence, Retrieved Knowledge Context, Agent Actions, and Guardrail Warnings when applicable.

## Sample Interactions
Below are examples captured from real runs.

### Example 1: Conflict detection (main demo script)
Input:
- Owner has two pets (Mochi and Whiskers) with overlapping morning tasks.

Output:
```text
⚠️ Conflict: Mochi - Feed Breakfast (08:00-08:10) overlaps with Whiskers - Feed Breakfast (08:00-08:10).
⚠️ Conflict: Mochi - Morning Walk (08:10-08:40) overlaps with Whiskers - Litter Box Cleaning (08:10-08:20).
```

### Example 2: Integrated RAG + agentic guardrails (scheduler pipeline)
Input:
- Question: "What should I prioritize if my dog is not eating?"
- Symptoms: "vomiting and not eating"
- Medications: "nsaid, steroid"

Output:
```text
confidence 0.68
warnings 2
- Red-flag symptoms detected. Vet follow-up was added as an urgent task.
- Potential medication interaction: NSAID + steroid can increase GI risk. Contact a vet before combining.
actions 2
- Inserted urgent vet escalation task from symptom guardrail.
- Flagged medication interaction risk from retrieved safety rules.
plan ['Urgent Vet Call', 'Short Walk']
```

### Example 3: Recurring task rollover
Input:
- Complete one daily task and one weekly task.

Output:
```text
Completed Mochi task 't2' (daily).
  Auto-created next daily task: t2-next-2026-03-29 due_date=2026-03-29 due_by=08:00
Completed Whiskers task 't6' (weekly).
  Auto-created next weekly task: t6-next-2026-04-04 due_date=2026-04-04 due_by=08:15
```

## Logging and Guardrails
- **Logging:** `app.py` logs schedule-generation requests, whether symptoms/medications were supplied, and final plan size + confidence.
- **Guardrails:** `generate_agentic_plan()` can add urgent vet escalation tasks for red-flag symptoms and raise medication interaction warnings.
- **Error handling:** domain validation raises clear `ValueError`s for invalid durations, priorities, and date/time formats; the UI catches exceptions and shows user-safe errors.

## Design Decisions and Trade-offs
- I used clear domain classes (`Owner`, `Pet`, `Task`, `Scheduler`) to keep business rules testable and separate from UI code.
- Scheduling is deterministic (required -> priority -> due time -> duration -> title), which improves explainability and repeatability.
- I kept a straightforward overlap-based conflict detector rather than a more complex optimized approach because clarity and debuggability were more important for this project scale.
- I chose string-based `HH:MM` and `YYYY-MM-DD` fields with strict validation for readability in UI/testing, accepting that richer date-time objects would be better for larger production systems.

## Testing Summary
- **Automated tests:** 35 out of 35 tests passed (`python -m pytest -q`). Coverage includes validation rules, ranking order, budget/window enforcement, sorting, filtering, recurrence rollover, conflict detection, knowledge retrieval, and integrated agentic guardrails.
- **Error handling:** invalid task/owner inputs fail fast with `ValueError` checks (duration, priority, date/time format, and invalid planning windows), which prevents silent bad state.
- **Human evaluation:** schedule outputs and conflict warnings were manually reviewed via both `python main.py` and the Streamlit UI to confirm explanations match ranking behavior.
- **Confidence scoring:** implemented in `generate_agentic_plan()` as a bounded score based on retrieval signal and guardrail risk penalties.

Concise reliability result:

`35 out of 35 tests passed; the integrated RAG + agentic path now adds urgent escalation and interaction checks in-plan, with confidence values exposed in the UI and pipeline outputs.`

## Reflection
This project taught me that AI-oriented problem solving is strongest when design, implementation, and verification are tightly coupled. I learned to treat explainability as a product feature, not an afterthought, by making every scheduled item include a reason and by surfacing conflicts rather than hiding them. I also learned that practical trade-offs matter: a simpler, testable approach often wins over theoretical optimization for early-stage systems.

## Demo Screenshot
![PawPal App Demo](pawpal_demo.png)
