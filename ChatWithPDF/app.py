import streamlit as st
from chat_with_pdf import user_input, get_pdf_text, get_text_chunks, get_vector_store

if "processed" not in st.session_state:
    st.session_state.processed = False
    
st.set_page_config("Chat PDF")
st.title("Chat with PDF using Gemini💁")

# Redesigned content outside the sidebar
st.header("Upload PDF")
api_key = st.text_input("Enter your Google API Key:", type="password")
st.markdown("[How to Get an API key | Gemini API - Google AI for Developers?](https://ai.google.dev/gemini-api/docs/api-key)")
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

if api_key:
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            st.session_state.processed = True
            st.success("Done")
    # Ask user for a question
if st.session_state.processed:
    user_question = st.text_input("Ask a Question from the PDF Files")
    if user_question:
        response = user_input(user_question, api_key)
        st.write("Reply: ", response["output_text"])
else:
    st.info("Please upload and process your PDFs before asking a question.")

