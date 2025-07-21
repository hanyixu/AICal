import os

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("No API key found!")
else:
    print(f"Your Gemini API key is: {api_key[:4]}... (hidden for security)")
    # Here you would use the API key to call Gemini API 