from abc import ABC
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class BaseModel(ABC):
    metadata: dict | None = field(default_factory=dict)
