# from dotenv import load_dotenv
# import os
import google.generativeai as genAI

# load_dotenv()
# genAI.configure(api_key= os.getenv('GOOGLE_API_KEY'))
# model = genAI.GenerativeModel('gemini-1.5-flash')
system_prompt = """
You are a compassionate and professional mental health therapist. 
Your role is to provide empathetic, non-judgmental support and guidance. 
Always listen carefully to the user's concerns and provide thoughtful, supportive responses. 
Remember to encourage healthy coping mechanisms and positive thinking.
"""

def start_chat(api_key):
    """
    Start a new chat session with the system prompt included in the initial history.
    """
    genAI.configure(api_key= api_key)
    model = genAI.GenerativeModel('gemini-1.5-flash')
    initial_history = [{'text': system_prompt}]
    chat = model.start_chat()
    chat.send_message({'text': system_prompt})  # Set initial system prompt
    return chat

def get_bot_response(chat, user_message):
    """
    Generate a response from the Google Generative AI model.
    
    Parameters:
    - chat (ChatSession): The chat session object.
    - user_message (str): The latest message from the user.

    Returns:
    - str: The response from the bot.
    """
    response = chat.send_message({'text': user_message})
    # Assuming the response object has an attribute `text` for the response
    return response.text