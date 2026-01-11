from fastapi import UploadFile
from app.services.storage import StorageService
from app.models.file import File
from app.const.default import ingest_document_upload_directory
import uuid


class IngestService:

    def __init__(self, directory=ingest_document_upload_directory) -> None:
        self.directory = directory
        self.file_service = StorageService(self.directory)
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
