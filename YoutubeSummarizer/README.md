# YouTube Summarizer

A web application that summarizes YouTube videos by extracting their transcripts and generating concise summaries using Google's Generative AI.

## Features
- Extracts transcript text from YouTube videos.
- Generates a summary of the transcript using Google's Generative AI.
- Displays the YouTube video thumbnail.
- Simple and intuitive user interface built with Streamlit.

## Requirements

- Python 3.7 or higher
- Streamlit
- python-dotenv
- google-generativeai
- youtube-transcript-api

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/priyxnshuuu/Google-Gemini.git
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
   streamlit run '.\Youtube Summarizer\app.py'

2. Open your browser and go to `http://localhost:8501`.

3. Enter the YouTube video URL you want to summarize and click on the "Summarize" button.

## Project Structure

   ```bash

   Google-Gemini/
   ├── .env                      # Environment variables
   ├── .gitignore                # Git ignore file
   ├── LICENSE                   # License file
   ├── README.md                 # Project documentation
   ├── requirements.txt          # Required Python packages
   └── YoutubeSummarizer/        # Directory containing the application
      ├── youtube_summarizer.py  # Script containing the summarizer functions
      ├── app.py                 # Main Streamlit application
      └── README.md              # Detailed documentation for the application