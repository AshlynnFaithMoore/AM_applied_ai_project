from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Owner:
    owner_id: str
    name: str
    daily_time_budget_minutes: int = 60
    preferred_start_time: str = "08:00"
    preferred_end_time: str = "20:00"

    def set_time_budget(self, minutes: int) -> None:
        pass

    def set_preferred_window(self, start: str, end: str) -> None:
        pass

    def can_fit(self, total_minutes: int) -> bool:
        pass


@dataclass
class Task:
    task_id: str
    title: str
    category: str
    duration_minutes: int
    priority: str
    required: bool = False
    due_by: Optional[str] = None
    active: bool = True

    def priority_weight(self) -> int:
        pass

    def is_due_window_valid(self, owner: Owner) -> bool:
        pass

    def summary(self) -> str:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: Optional[int] = None
    care_notes: str = ""
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: str) -> bool:
        pass

    def get_active_tasks(self) -> list[Task]:
        pass


class Scheduler:
    def __init__(self, strategy: str = "priority_first", buffer_minutes: int = 0) -> None:
        self.strategy = strategy
        self.buffer_minutes = buffer_minutes

    def rank_tasks(self, tasks: list[Task]) -> list[Task]:
        pass

    def generate_daily_plan(self, owner: Owner, pet: Pet) -> list[dict]:
        pass

    def explain_plan(self, owner: Owner, plan: list[dict]) -> list[str]:
        pass
