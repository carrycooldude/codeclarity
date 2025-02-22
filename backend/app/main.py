from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.raptor import RAPTORProcessor
from app.vertex_ai import generate_doc
import os

app = FastAPI()
raptor = RAPTORProcessor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_code(file: UploadFile):
    code = (await file.read()).decode()
    return {
        "documentation": generate_doc(code),
        **raptor.process(code)
    }