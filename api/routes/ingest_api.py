from fastapi import APIRouter, UploadFile, File

router=APIRouter()

@router.post('/file')
async def upload(file: UploadFile = File(...)):
  return file