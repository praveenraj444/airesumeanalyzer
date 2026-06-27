import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    print("❌ API Key not found in .env file!")
    exit()

try:
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Hello, are you working?'
    )
    print("✅ Gemini API is working!")
    print(f"Response: {response.text}")

except Exception as e:
    print(f"❌ Error: {e}")