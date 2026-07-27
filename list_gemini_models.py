"""List available Gemini models"""
import google.generativeai as genai

GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'
genai.configure(api_key=GEMINI_API_KEY)

print("Available Gemini models:")
print("-" * 60)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Description: {model.description}")
        print(f"  Supports: {', '.join(model.supported_generation_methods)}")
        print()
