import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "backend/data")
VECTOR_STORE_DIR = os.getenv("VECTOR_STORE_DIR", "backend/data/vector_store")