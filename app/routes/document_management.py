from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os

router = APIRouter()

DOCUMENTS_DIR = "backend/data/uploaded_files"

@router.get("/")
async def list_documents():
    try:
        files = os.listdir(DOCUMENTS_DIR)
        return {"documents": files}
    except Exception:
        return JSONResponse(status_code=500, content={"error": "Failed to list documents."})