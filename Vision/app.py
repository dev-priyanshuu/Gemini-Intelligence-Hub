import streamlit as st
from vision import get_gemini_response
from PIL import Image


st.title("Gemini vision")
api_key = st.text_input("Enter your Google API Key:", type="password")
st.markdown("[How to Get an API key | Gemini API - Google AI for Developers?](https://ai.google.dev/gemini-api/docs/api-key)")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if api_key:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption = "Uploaded Image", use_column_width=True)
        
        submit=st.button("Tell me about the image")
        
        ## If ask button is clicked
        if submit:  
            response=get_gemini_response(input,image,api_key)
            st.subheader("The Response is")
            st.write(response)
else:
    st.error("Please enter your Google API Key in the input box to proceed.")
