from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
async def query_theme(q: str = Query(..., min_length=1)):
    # Dummy response, replace with real query logic
    response = f"Query received: {q}. Theme identification logic goes here."
    return {"response": response}