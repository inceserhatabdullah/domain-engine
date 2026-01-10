from fastapi import APIRouter, UploadFile, File
from services.ingest_service import IngestService

router = APIRouter()


@router.post("/file")
async def upload(file: UploadFile = File(...)):
    ingest_service = IngestService()
    return await ingest_service.ingest(file)