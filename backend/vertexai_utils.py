# vertexai_utils.py
import vertexai
from vertexai.language_models import TextGenerationModel

def init_vertexai(project_id: str ="codeclarity", location: str = "asia-south1") -> None:
    """Initialize VertexAI with GCP project credentials."""
    vertexai.init(project=project_id, location=location)

def generate_docstring(code: str) -> str:
    """Generate docstrings for code using VertexAI."""
    model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = f"""
    Generate a Python docstring for this code:
    {code}
    Include:
    - Functionality
    - Parameters (types, purpose)
    - Return value (type, meaning)
    - Example usage
    """
    response = model.predict(prompt, max_output_tokens=1024)
    return response.text

def answer_question(code: str, question: str) -> str:
    """Answer questions about code using VertexAI."""
    model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = f"""
    Code:
    {code}
    Question: {question}
    Answer:
    """
    response = model.predict(prompt, max_output_tokens=1024)
    return response.text