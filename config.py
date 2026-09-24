import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROVIDER = os.getenv("PROVIDER", "groq")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

if PROVIDER == "groq":
    API_KEY = os.getenv("GROQ_API_KEY")
    BASE_URL = "https://api.groq.com/openai/v1"
else:
    raise SystemExit("Unsupported provider")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY is missing in .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

def banner(system_name):
    print(f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n")