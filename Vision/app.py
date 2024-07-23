import streamlit as st
from vision import get_gemini_response
from PIL import Image


st.title("Gemini vision")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption = "Uploaded Image", use_column_width=True)
    
    submit=st.button("Tell me about the image")
    
    ## If ask button is clicked
    if submit:  
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)

