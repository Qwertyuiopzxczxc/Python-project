""" =========================================================
    Task — шаблон задачи.
    =========================================================
"""
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class Task:
    """Модель одной задачи."""
    title: str
    description: str = ""
    status: bool = False
    author: str = "—"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    id: int | None = None

    def to_dict(self) -> dict:
        """Сериализовать задачу в dict для StorageManager."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Восстановить Task из dict."""
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            status=bool(data.get("status", False)),
            author=data.get("author", "—"),
            created_at=data.get("created_at", datetime.now().isoformat(timespec="seconds"))
        )
