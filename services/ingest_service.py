from fastapi import UploadFile
from services.file_service import FileService
from domain.file_model import File
import uuid


class IngestService:

    def __init__(self, directory = "data/uploads") -> None:
        self.directory=directory
        self.file_service = FileService(self.directory)
        pass

    async def ingest(self, file: UploadFile) -> File:

        file_id = str(uuid.uuid4())
        relative_path = f"{self.directory}/{file_id}"

        await self.file_service.upload(file, relative_path)

        return File(
            id=file_id,
            size=file.size,
            original_name=str(file.filename),
            path=relative_path,
            content_type=str(file.content_type),
        )
