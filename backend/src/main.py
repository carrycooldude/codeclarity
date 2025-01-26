import os
import tempfile
import shutil
from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .code_analysis import CodeClarity
from .utils import validate_input

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="CodeClarity API",
    description="AI-powered legacy code analysis tool",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_codebase(files: List[UploadFile] = File(...)):
    """
    Analyze uploaded codebase files
    
    :param files: List of code files to analyze
    :return: Analyzed documentation
    """
    codeclarity = CodeClarity()
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        file_paths = []
        for file in files:
            # Validate file
            if not validate_input(file.filename):
                raise HTTPException(status_code=400, detail="Invalid file type")
            
            # Save file
            file_path = os.path.join(temp_dir, file.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())
            file_paths.append(file_path)
        
        # Process codebase
        documentation = codeclarity.process_codebase(temp_dir)
        
        return {
            "codebase": file_paths,
            "documentation": documentation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)

@app.post("/query")
async def query_codebase(question: str):
    """
    Query the analyzed codebase
    
    :param question: Natural language question about the code
    :return: Contextual answer
    """
    try:
        codeclarity = CodeClarity()
        answer = codeclarity.qna_engine.query(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def main():
    """
    Entry point for the backend application
    """
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()