# Mental Health Chatbot

The Mental Health Chatbot is a web application designed to provide a supportive and interactive platform for users seeking mental health assistance. Built using Streamlit and powered by the Google Gemini API, this chatbot aims to simulate multi-turn conversations with stateless interactions, maintaining context throughout the chat.

## Features
- **Interactive Chat Interface**: Engage in conversations with the chatbot in a user-friendly interface.
- **Multi-turn Conversations**: Each new message includes the previous messages to maintain context.
- **Highlighting**: Each question in the conversation history is highlighted for easy reference.
- **Stateless Interactions**: The app maintains past messages without refreshing the entire screen.


## Requirements

- Python 3.7 or higher
- Streamlit
- Python-dotenv
- Google-generativeai

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/priyxnshuuu/Gemini-Intelligence-Hub.git
   cd Google-Gemini

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Create a .env file in the root directory and add your Google API key::
   ```bash
   GOOGLE_API_KEY=your_google_api_key

## Usage

1. Run the Streamlit application::
   ```bash
   streamlit run '.\MentalTherapist\app.py'

2. Open your browser and navigate to `http://localhost:8501` to interact with the chatbot.


## Project Structure

   ```bash

   Google-Gemini/
   ├── .env                      # Environment variables
   ├── .gitignore                # Git ignore file
   ├── LICENSE                   # License file
   ├── README.md                 # Project documentation
   ├── requirements.txt          # Required Python packages
   └── MentalTherapist/          # Directory containing the application
      ├── mental_therapist.py    # Script containing the chat functions
      ├── app.py                 # Main Streamlit application
      └── README.md              # Detailed documentation for the application
