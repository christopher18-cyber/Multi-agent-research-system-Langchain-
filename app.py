import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client directly
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fetch and print all available model IDs for your account
models = client.models.list()
print("Available models for your API key:")
for model in models.data:
    print(f"- {model.id}")