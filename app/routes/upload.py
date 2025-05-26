from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from typing import Optional

router = APIRouter()

UPLOAD_DIR = "backend/data/uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    filename: Optional[str] = file.filename
    if not filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    if not filename.lower().endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF or TXT files allowed.")

    file_location = os.path.join(UPLOAD_DIR, filename)
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    return JSONResponse(content={"filename": filename, "message": "File uploaded successfully"})