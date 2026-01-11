from dataclasses import dataclass
from app.models.base import BaseModel


@dataclass(kw_only=True)
class Chunk(BaseModel):
    id: str
    document_id: str
    text: str
    order: int
