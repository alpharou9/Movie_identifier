import google.generativeai as genai

# PASTE YOUR NEW KEY HERE
GEMINI_API_KEY = 'AIzaSyDYVZ3e4NmpDyJh0c56gbpVRAwhWRJlQ2Y'

genai.configure(api_key=GEMINI_API_KEY)

try:
    for model in genai.list_models():
        print(f"✓ {model.name}")
        break  # Just test if it works
    print("\n✅ API KEY IS VALID!")
except Exception as e:
    print(f"❌ API KEY INVALID: {e}")