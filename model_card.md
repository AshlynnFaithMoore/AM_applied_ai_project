# PawPal+ Model Card

## Model Overview
PawPal+ is an AI-assisted pet care planning system built from the original Modules 1-3 project. It combines a pet-care knowledge retriever, an agentic guardrail layer, and a deterministic scheduler to produce explainable care plans for one or more pets.

## Intended Use
The system is intended to help a pet owner organize daily pet-care tasks such as feeding, walks, enrichment, grooming, and medication reminders. It is designed to support planning and prioritization, not to replace veterinary judgment.

## Inputs
- Owner name, time budget, and preferred planning window
- Pet profile data such as name, species, age, and care notes
- Task metadata such as title, category, priority, duration, due time, recurrence, and required/optional status
- Optional AI context inputs such as question text, symptoms, and active medications

## Outputs
- A daily schedule with start/end times
- Human-readable explanations for why each task was chosen
- Retrieved knowledge context from the local pet-care knowledge base
- Guardrail warnings and agent actions when symptoms or medication risks are detected
- A confidence score for the integrated planning result

## Architecture
The implemented system uses:
- A local retrieval step over a small handcrafted knowledge base
- Guardrails that can escalate red-flag symptoms or medication risks
- Deterministic ranking and scheduling logic
- Human review through the Streamlit UI and the console demo script
- Automated tests in `tests/test_pawpal.py`

## Limitations and Biases
- The retriever uses a small handcrafted knowledge base, so it may miss topics not represented in the current rules.
- Confidence scoring is heuristic and not clinically calibrated.
- Outputs may reflect the assumptions encoded by the project author, especially around pet-care priorities and warning thresholds.
- The system does not perform real veterinary diagnosis or use a medically validated clinical model.

## Misuse Risks and Mitigations
The system could be misused as a substitute for veterinary care or as a decision engine for medical treatment. To reduce that risk, the system:
- Surfaces red-flag symptom warnings and urgent vet escalation tasks
- Flags possible medication interaction risks
- Logs schedule-generation activity
- Keeps human review in the loop through UI output and explanations

## Reliability and Testing
Testing was used to prove the system works rather than merely appears to work.

### Automated Tests
Current result: 35 out of 35 tests passed with `python -m pytest -q`.

Test coverage includes:
- Task validation
- Owner validation and time-window checks
- Pet task management
- Scheduler ranking and time sorting
- Filtering behavior
- Recurring task rollover
- Conflict detection
- Knowledge retrieval
- Agentic guardrails and confidence bounds

### Human Evaluation
The system was manually reviewed through:
- `python main.py` console output
- The Streamlit UI with AI context inputs enabled

### What I Learned During Testing
- Edge cases around recurrence and overlap logic are easy to miss without targeted tests.
- An apparently simple time comparison can fail if date assumptions are inconsistent.
- Guardrails make the system safer, but they must be tested directly to ensure they actually affect behavior.

## AI Collaboration
AI was helpful for:
- Suggesting edge-case tests
- Structuring the retrieval and guardrail pipeline
- Improving documentation clarity

AI was flawed when it suggested an overly simplified timing check for overdue medication logic. That approach looked clean but used the wrong temporal comparison until it was corrected and re-tested.

## Responsible Use Guidance
Use this system as a planning aid, not a substitute for professional advice. If symptoms are severe, rapidly worsening, or unusual, the user should contact a veterinarian directly.
