import os
from pathlib import Path
from vertexai.language_models import TextGenerationModel
import vertexai
from google.oauth2 import service_account
from dotenv import load_dotenv
from google.cloud import aiplatform

load_dotenv()

credentials_path_relative = os.getenv("GCP_CREDENTIALS")

if credentials_path_relative is None:
    raise ValueError("GCP_CREDENTIALS environment variable not set.")

# ***Correct and Robust Path Construction***
# Get the directory of the *main* script (not necessarily vertex_ai.py)
main_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = Path(main_script_dir).parents[1]  # <--- Correct navigation

absolute_credentials_path = project_root / credentials_path_relative

# Check if the file exists
if not absolute_credentials_path.exists():
    raise FileNotFoundError(f"Credentials file not found at: {absolute_credentials_path}")

try:
    credentials = service_account.Credentials.from_service_account_file(str(absolute_credentials_path))
except Exception as e:
    raise Exception(f"Error loading credentials: {e}")

# 2. Initialize Vertex AI (Use the Credentials Object)
vertexai.init(
    project=os.getenv("GCP_PROJECT"),
    location=os.getenv("GCP_REGION"),
    credentials=credentials  # Pass the credentials object
)

aiplatform.init(  # Initialize aiplatform as well
    project=os.getenv("GCP_PROJECT"),
    location=os.getenv("GCP_REGION"),
    credentials=credentials  # Pass the credentials object
)

model = TextGenerationModel.from_pretrained("text-bison@001")

def generate_doc(code: str) -> str:
    response = model.predict(
        f"""Generate markdown documentation for:
        {code}
        Include parameters, returns, examples, and edge cases."""
    )
    return response.text