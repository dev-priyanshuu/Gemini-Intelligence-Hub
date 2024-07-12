from dotenv import load_dotenv
import os
import google.generativeai as genAI
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# load all env file
load_dotenv()
genAI.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# system prompt
prompt = """You are Youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 350 words. Please provide the summary of the text given here: """

# getting the transcript text 
def get_transcript_text(video_url):
    try:
        video_id = video_url.split("/")[-1].split("?")[0]
        # getting the transcript text
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i['text']
        
        return transcript

    except TranscriptsDisabled as e:
        return None
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text):
    # load model
    model = genAI.GenerativeModel("gemini-pro")

    # generate content
    response=model.generate_content(prompt+transcript_text)

    return response.text