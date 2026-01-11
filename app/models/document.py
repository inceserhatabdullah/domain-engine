from dataclasses import dataclass
from typing import Iterable
from app.models.base import BaseModel


@dataclass(kw_only=True)
class Document(BaseModel):
    id: str
    file_id: str
    pages: Iterable[str]
    parser: str
