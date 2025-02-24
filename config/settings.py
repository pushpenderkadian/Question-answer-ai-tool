import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# API keys and credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")