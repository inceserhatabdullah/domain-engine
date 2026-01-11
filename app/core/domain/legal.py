from app.core.domain.base import DomainProfile


class LegalDomain(DomainProfile):
    name: str = "legal"

    def chunking_rules(self) -> dict:
        return {"max_token": 800, "overlap": 100, "respect_section": True}

    def metadata_schema(self) -> dict:
        return {"jurisdiction": str, "document_type": str, "effective_data": str}

    def detect_sections(self, text: str) -> list[str]:
        # placeholder – regex / NLP
        return super().detect_sections(text)