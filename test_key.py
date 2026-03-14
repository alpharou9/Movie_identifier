import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise RuntimeError('GEMINI_API_KEY environment variable is not set')

genai.configure(api_key=GEMINI_API_KEY)

try:
    for model in genai.list_models():
        print(f"✓ {model.name}")
        break  # Just test if it works
    print("\n✅ API KEY IS VALID!")
except Exception as e:
    print(f"❌ API KEY INVALID: {e}")