
import sys
import google.generativeai as genai

# Hardcoded API key
API_KEY = "AIzaSyDSlz3awT3TBjH_zWrV0jBqo1nh3YFWzTQ"

def generate_response(prompt):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Please try again."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bard_interaction.py <prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]
    user_prompt = user_prompt + ".Note:i dont want lengthly responses,just give me the basic info and keep it correct.keep it simple and direct!"

    response = generate_response(user_prompt)
    print(response)
