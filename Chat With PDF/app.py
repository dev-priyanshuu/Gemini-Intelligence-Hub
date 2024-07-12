import streamlit as st
from chat_with_pdf import user_input, get_pdf_text, get_text_chunks, get_vector_store

st.set_page_config("Chat PDF")
st.title("Chat with PDF using Gemini💁")

# Redesigned content outside the sidebar
st.header("Upload PDF")
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

if st.button("Submit & Process"):
    with st.spinner("Processing..."):
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks)
        st.success("Done")
# Ask user for a question
user_question = st.text_input("Ask a Question from the PDF Files")

# Handle user input
if user_question:
    response = user_input(user_question)
    st.write("Reply: ", response["output_text"])


