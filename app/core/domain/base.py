from abc import ABC, abstractmethod

class DomainProfile(ABC):
  name: str
  
  @abstractmethod
  def chunking_rules(self) -> dict:
    pass
  
  @abstractmethod
  def metadata_schema(self) -> dict:
    pass
  
  @abstractmethod
  def detect_sections(self, text: str) -> list[str]:
    pass
