# PawPal+ Presentation Outline (5-7 minutes)

## 1. Opening: What I built (30-45 seconds)
- PawPal+ is an AI-assisted pet care planner.
- It helps a user organize pet tasks, explain why tasks were chosen, and surface safety warnings.
- The project started as a class-based scheduling system and evolved into an integrated RAG + agentic workflow.

## 2. Problem and why it matters (30-45 seconds)
- Pet care is repetitive, time-sensitive, and safety-sensitive.
- Owners need a system that can prioritize feeding, meds, walks, and urgent follow-up when symptoms appear.
- The value of the project is explainable planning, not just task sorting.

## 3. System walkthrough (1-2 minutes)
- Show the architecture diagram in the README or assets folder.
- Explain the flow: user input -> Streamlit app -> retrieval -> agent guardrails -> scheduler -> output.
- Point out where human review and automated tests fit in.

## 4. Live demo (1-2 minutes)
- Demo 1: standard schedule generation with owner + pet tasks.
- Demo 2: symptoms and medications triggering guardrails and urgent vet escalation.
- Demo 3: recurring task rollover for daily/weekly items.
- Highlight the AI confidence score, retrieved context, and explanations.

## 5. Reliability and testing (45-60 seconds)
- Share the current test result: 35 out of 35 tests passed.
- Mention what is covered: validation, ranking, recurrence, conflict detection, retrieval, and guardrails.
- Explain that human evaluation was used alongside automated tests.

## 6. What I learned (30-45 seconds)
- AI systems need guardrails, not just outputs.
- Deterministic logic plus tests made the system trustworthy.
- I learned to treat explainability and safety as first-class features.

## 7. Close (15-30 seconds)
- Summarize the project as an example of building a practical, responsible AI workflow.
- Invite questions about the retrieval design, guardrails, or testing approach.
