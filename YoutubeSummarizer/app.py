import streamlit as st
from youtube_summarizer import get_transcript_text, generate_gemini_content

st.title("Youtube Summarizer")
api_key = st.text_input("Enter your Google API Key:", type="password")
youtube_url = st.text_input("Enter YouTube Video Link:")
if api_key:
    if youtube_url:
        video_id = youtube_url.split("/")[-1].split("?")[0]
        # display youtube thumbnail
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Summarize"):
        if youtube_url:
            transcript = get_transcript_text(youtube_url)
            summary = generate_gemini_content(transcript,api_key)
            st.markdown("## Detailed Notes:")
            st.write(summary)
        else:
            st.write("Please enter a valid YouTube URL")
else:
    st.error("Please enter your Google API Key in the input box to proceed.")