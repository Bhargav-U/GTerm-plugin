import os
import sys
import google.generativeai as genai

API_KEY = "ENTER YOUR API KEY"

def generate_response(prompt):
    try:
        genai.configure(api_key=API_KEY)
        # Assuming the correct method to generate content
        model = genai.GenerativeModel()
        response = model.generate_content(prompt)
        return response.text  # Modify according to the actual response object structure
    except Exception as e:
        return f"Error encountered, please try again: {str(e)}"

def create_conversation_file():
    with open("conversation.txt", "w") as file:
        file.write("NOTE: Keep the conversations to the point, keep it direct and sharp!\n")

def delete_conversation_file():
    if os.path.exists("conversation.txt"):
        os.remove("conversation.txt")

def read_conversation_file():
    with open("conversation.txt", "r") as file:
        return file.read()

def append_to_conversation_file(user_input, response):
    with open("conversation.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {response}\n")

def process_input(user_input):
    if user_input == "start convo":
        create_conversation_file()
        return "Conversation started."

    if user_input == "stop convo":
        delete_conversation_file()
        return "Conversation stopped."

    if os.path.exists("conversation.txt"):
        past_conversations = read_conversation_file()
        user_input = "please use the above as reference:\n" + past_conversations + "now please only answer the latest question, keep it short and direct, to the point:\n" + "new question:" + user_input
        response = generate_response(user_input)
        append_to_conversation_file(user_input, response)
        return response
    else:
        return generate_response(user_input)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bot.py <prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]
    response = process_input(user_prompt)
    print(response)
