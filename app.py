import streamlit as st
from streamlit_option_menu import option_menu
from YoutubeSummarizer.youtube_summarizer import get_transcript_text, generate_gemini_content
from ChatWithPDF.chat_with_pdf import user_input, get_pdf_text, get_text_chunks, get_vector_store
from Vision.vision import get_gemini_response
from MentalTherapist.mental_therapist import start_chat, get_bot_response

from PIL import Image

# Set page title and configuration
st.set_page_config(page_title="Google Gemini Projects", layout="wide")

# Sidebar navigation
with st.sidebar:
    # Use option_menu from streamlit_option_menu for selection
    project_selection = option_menu('Google Gemini Projects',
                          ['Youtube Summarizer',
                           'Chat with PDF',
                           'Google Vision',
                           'Mental Therapist'],
                          icons=['youtube', 'file-text', 'eye', 'heart'],
                          default_index=0)  

# Main content area
if project_selection == 'Youtube Summarizer':
    st.header("Youtube Summarizer")
    youtube_url = st.text_input("Enter YouTube Video Link:")

    if st.button("Summarize"):
        if youtube_url:
            video_id = youtube_url.split("/")[-1].split("?")[0]
            # Display YouTube thumbnail
            st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

            transcript = get_transcript_text(youtube_url)
            if transcript:
                summary = generate_gemini_content(transcript)
                st.markdown("## Detailed Notes:")
                st.write(summary)
            else:
                st.write("Transcript not available for this video.")
        else:
            st.write("Please enter a valid YouTube URL")

elif project_selection == 'Chat with PDF':
    st.header("Chat with PDF using Gemini💁")

    # Upload PDF files
    st.header("Upload PDF")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

    if st.button("Submit & Process"):
        if pdf_docs:
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing complete")

    # User input for questions
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        response = user_input(user_question)
        st.write("Reply: ", response["output_text"])
        
elif project_selection == 'Google Vision':
    st.header("Gemini vision")
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

elif project_selection == 'Mental Therapist':
    if 'chat' not in st.session_state:
        st.session_state.chat = start_chat()

    # Streamlit application
    st.title("Mental Health Chatbot")

    # Display conversation history
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Inject custom CSS for button styling
    st.markdown("""
        <style>
        .stButton > button {
            background-color: #0e1117; /* Initial button color */
            color: white; /* Text color */
            margin-top:25px;
            border: none; /* Remove border */
            border-radius: 5px; /* Rounded corners */
            padding: 5px 15px; /* Padding */
            cursor: pointer; /* Pointer cursor on hover */
            font-size: 16px; /* Font size */
        }
        .stButton > button:hover {
            background-color: gray; /* Color on hover */
        }
        </style>
    """, unsafe_allow_html=True)

    # Create a form for the input box and button
    with st.form(key='chat_form', clear_on_submit=True):
        # Create a horizontal layout for the input box and button
        col1, col2 = st.columns([8 , 1])  # Adjust column widths as needed

        with col1:
            # Input box for user message
            user_input = st.text_input("You:", "")

        with col2:
            # Add a button to send the message
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            # Append user message to conversation history
            st.session_state.conversation_history.append(f"User: {user_input}")

            # Show loading spinner while waiting for response
            with st.spinner('Waiting for the bot to respond...'):
                # Get response from AI handler
                bot_response = get_bot_response(st.session_state.chat, user_input)

            # Append bot response to conversation history
            st.session_state.conversation_history.append(f"Bot: {bot_response}")

    # Display updated conversation history
    for message in st.session_state.conversation_history:
        if message.startswith("User:"):
            st.markdown(
                f'''
                <div style="border: 2px solid gray; border-radius: 5px; padding: 10px; margin-bottom: 10px; ">
                    <strong>{message}</strong>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'''
                <div style="padding: 10px; margin-bottom: 10px; ">
                    <strong>{message}</strong>
                </div>
                ''',
                unsafe_allow_html=True
            )
