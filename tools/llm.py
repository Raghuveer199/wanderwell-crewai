import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# Gemini Flash LLM setup
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)
