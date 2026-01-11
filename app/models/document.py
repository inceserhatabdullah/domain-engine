from dataclasses import dataclass

@dataclass
class Document:
  id: str
  size: int | None
  path: str
  content_type: str
  original_name: str