from pathlib import Path
from fastapi import UploadFile


class FileService:

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


""" 
  def exists(self, path: str) -> bool:
    return (self.base_dir, path).exists()
  
  def stat(self, path: str):
    return (self.base_dir, path).stat()
"""
