from fastapi import APIRouter, UploadFile, File
from app.services.ingest import IngestService

router = APIRouter()


@router.post("/document")
async def upload(file: UploadFile = File(...)):
    ingest_service = IngestService()
    return await ingest_service.ingest(file)
