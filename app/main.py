from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import upload, query, document_management

app = FastAPI(title="Theme Identifier Chatbot", version="1.0.0")

# Include your route modules
app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(document_management.router, prefix="/documents", tags=["documents"])

# Serve static frontend files
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")