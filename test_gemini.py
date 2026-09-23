import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
API_KEY = os.environ.get('GEMINI_API_KEY')

if not API_KEY:
    print("❌ API Key not found in .env file!")
    print("Please add GEMINI_API_KEY=your_key to .env")
    exit()

print(f"✅ API Key loaded: {API_KEY[:15]}...")

try:
    # Initialize the new client
    client = genai.Client(api_key=API_KEY)

    # Test the model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Hello, are you working?'
    )

    print("✅ Gemini API is working!")
    print(f"Response: {response.text}")

except Exception as e:
    print(f"❌ Error: {e}")