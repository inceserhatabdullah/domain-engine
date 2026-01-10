from pathlib import Path
from fastapi import UploadFile


class StorageService:

    def __init__(self, directory: str) -> None:
        self.directory = directory
        Path(directory).mkdir(parents=True, exist_ok=True)

    async def upload(self, file: UploadFile, path: str, chunk_size=1024 * 1024):
        with open(path, "wb") as buffer:
            while True:
                chunk = file.file.read(chunk_size)
                if not chunk:
                    break
                buffer.write(chunk)
