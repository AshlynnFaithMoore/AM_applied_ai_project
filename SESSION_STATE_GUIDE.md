# Session State Integration Guide

## What Changed

Your Streamlit app now uses `st.session_state` to persist the Owner and Pet instances across page reruns, enabling a stateful workflow.

## How It Works

### 1. Initialization (Lines 7-10)
```python
if "owner" not in st.session_state:
    st.session_state.owner = None
    st.session_state.owner_initialized = False
```

- Checks if the Owner key already exists in the session vault
- If not, creates it with initial value `None`
- Adds a flag `owner_initialized` to track whether the user has set up their owner

**Key:** This runs every time the page reruns, but the condition only executes once because the key persists after first creation.

### 2. Creating Owner & Pet (Lines 50-67)
```python
if st.button("Initialize Owner & Pet"):
    st.session_state.owner = Owner(...)  # Store in session
    st.session_state.owner.add_pet(pet)
    st.session_state.owner_initialized = True
    st.rerun()  # Refresh UI with new state
```

- When user clicks "Initialize Owner & Pet", a new Owner is created and stored in the session vault
- The Pet is added to the Owner
- `st.rerun()` forces a page refresh to show the new UI (task input form becomes available)

### 3. Adding Tasks (Lines 84-94)
```python
if st.button("Add task"):
    task = Task(...)
    st.session_state.owner.get_pets()[0].add_task(task)  # Add to persistent owner
    st.success(f"✅ Task '{task_title}' added!")
```

- Retrieves the persistent Owner from session_state
- Creates a Task and adds it to the pet
- The task is now stored in the Owner, which will survive the next page rerun

### 4. Generating Schedule (Lines 110-140)
```python
owner = st.session_state.owner  # Retrieve persistent owner
pet = owner.get_pets()[0]       # Get the pet
scheduler = Scheduler()
plan = scheduler.generate_daily_plan(owner, pet)
```

- Uses the persistent Owner and all its tasks to generate the schedule
- All tasks added via "Add task" button are included in the plan

## Session State Lifecycle

| Action | Owner State | Result |
|--------|-------------|--------|
| Load app | Not in session_state | Initialized to `None`, flag = False |
| Click "Initialize Owner & Pet" | Created and stored | Owner persists, UI updates |
| Click "Add task" (multiple times) | Existing Owner retrieved | Tasks accumulate in the pet's task list |
| Click "Generate schedule" | Uses persisted Owner + all tasks | Schedule reflects all accumulated tasks |
| Browser refresh (F5) | ❌ Cleared | Session state resets, start from beginning |

## Why This Matters

**Without session_state:**
- Every button click reruns the entire script from top to bottom
- Creating a new Owner at the top would recreate it empty every time
- Tasks would be lost on each rerun

**With session_state:**
- Owner is created once and reused across all reruns
- Tasks accumulate and persist
- Scheduler always has access to all previously entered data

## Best Practices Applied

✅ **Guard clause pattern** — `if "owner" not in st.session_state`  
✅ **Separate initialization flag** — track setup state independently  
✅ **Use `st.rerun()`** — refresh UI after state changes  
✅ **Retrieve from session before using** — always fetch `st.session_state.owner`  
✅ **Error handling** — checks for uninitialized state before operations  

## Testing the Flow

1. Run `streamlit run app.py` in your terminal
2. Enter owner name and pet name
3. Click "Initialize Owner & Pet"
4. Add multiple tasks (notice they accumulate)
5. Click "Generate schedule" to see all tasks planned
6. Notice that if you add more tasks, they remain in the list (persistent!)
