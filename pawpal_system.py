from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, TypedDict


class ScheduleItem(TypedDict):
    """Represents one task in the daily schedule."""
    task_id: str
    task_title: str
    duration_minutes: int
    priority: str
    start_time: str
    end_time: str
    reason: str


@dataclass
class Owner:
    """Represents the pet owner and their planning constraints."""
    owner_id: str
    name: str
    daily_time_budget_minutes: int = 60
    preferred_start_time: str = "08:00"
    preferred_end_time: str = "20:00"

    def __post_init__(self) -> None:
        """Validate owner attributes on creation."""
        pass

    def set_time_budget(self, minutes: int) -> None:
        """Update the daily time budget for pet care tasks."""
        pass

    def set_preferred_window(self, start: str, end: str) -> None:
        """Update the preferred planning window (HH:MM format)."""
        pass

    def can_fit(self, total_minutes: int) -> bool:
        """Check if total_minutes fits within the daily budget."""
        pass


@dataclass
class Task:
    """Represents a single pet care task."""
    task_id: str
    title: str
    category: str
    duration_minutes: int
    priority: str
    required: bool = False
    due_by: Optional[str] = None
    active: bool = True

    def __post_init__(self) -> None:
        """Validate task attributes on creation."""
        pass

    def priority_weight(self) -> int:
        """Return numeric weight for this task's priority (for sorting)."""
        pass

    def is_due_window_valid(self, owner: Owner) -> bool:
        """Check if task's due_by time (if set) falls within owner's preferred window."""
        pass

    def summary(self) -> str:
        """Return a human-readable summary of the task."""
        pass


@dataclass
class Pet:
    """Represents a pet and manages its care tasks."""
    pet_id: str
    name: str
    species: str
    age: Optional[int] = None
    care_notes: str = ""
    owner: Optional[Owner] = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a new task to this pet's task list."""
        pass

    def remove_task(self, task_id: str) -> bool:
        """Remove a task by ID; return True if removed, False if not found."""
        pass

    def get_active_tasks(self) -> list[Task]:
        """Return only active tasks (active=True)."""
        pass


class Scheduler:
    """Orchestrates task ranking and daily schedule generation."""

    def __init__(self, strategy: str = "priority_first", buffer_minutes: int = 0) -> None:
        """Initialize scheduler with a ranking strategy and optional time buffer.

        Args:
            strategy: Ranking algorithm name (e.g., 'priority_first').
            buffer_minutes: Minutes to reserve as a safety margin in the daily plan.
        """
        self.strategy = strategy
        self.buffer_minutes = buffer_minutes
        self.plan: list[ScheduleItem] = []

    def rank_tasks(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by ranking criteria (required, priority, due time, duration, title)."""
        pass

    def generate_daily_plan(self, owner: Owner, pet: Pet) -> list[ScheduleItem]:
        """Build and cache a daily schedule for the pet within owner's constraints.

        Returns:
            List of ScheduleItem dicts with task, timing, and reasoning.
        """
        pass

    def explain_plan(self, owner: Owner, plan: Optional[list[ScheduleItem]] = None) -> list[str]:
        """Return human-readable explanations for plan selection.

        Args:
            plan: Plan items to explain (defaults to self.plan if not provided).
        """
        pass
