# from dotenv import load_dotenv
# import os 
import google.generativeai as genAI
from PIL import Image

#load environment variables
# load_dotenv()
# configure generativeai
# genAI.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load model
# model = genAI.GenerativeModel("gemini-1.5-flash")

# function to get response from model
def get_gemini_response(input,image,api_key):
   genAI.configure(api_key=api_key)
   
   model = genAI.GenerativeModel("gemini-1.5-flash")
   if input!="":
      response = model.generate_content([input,image])
   else:
      response = model.generate_content(image)
   return response.text