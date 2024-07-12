import streamlit as st
from streamlit_option_menu import option_menu
from YoutubeSummarizer.youtube_summarizer import get_transcript_text, generate_gemini_content
from ChatWithPDF.chat_with_pdf import user_input, get_pdf_text, get_text_chunks, get_vector_store

# Set page title and configuration
st.set_page_config(page_title="Google Gemini Projects", layout="wide")

# Sidebar navigation
with st.sidebar:
    # Use option_menu from streamlit_option_menu for selection
    project_selection = option_menu('Google Gemini Projects',
                          ['Youtube Summarizer',
                           'Chat with PDF'],
                          icons=['youtube','book'],
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
