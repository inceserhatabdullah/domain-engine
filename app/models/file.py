from dataclasses import dataclass
from app.models.base import BaseModel


@dataclass(kw_only=True)
class File(BaseModel):
    id: str
    size: int | None
    path: str
    content_type: str
    original_name: str
