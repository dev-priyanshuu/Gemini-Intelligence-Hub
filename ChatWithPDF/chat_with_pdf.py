from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import google.generativeai as genAI
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# from dotenv import load_dotenv

# load all env file
# load_dotenv()
# genAI.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# get pdf and extract all its text
def get_pdf_text(pdf_doc):
    text = ""

    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


# get all text chunks from pdf
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000, chunk_overlap=10000
    )
    chunk = text_splitter.split_text(text)

    return chunk


def get_vector_store(text_chunk,api_key):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunk, embedding=embedding)
    vector_store.save_local("faiss_index")


def get_conversational_chain(api_key):

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer. and give answer in both points and paragraph\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    genAI.configure(api_key=api_key)
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3,google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question,api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001",google_api_key=api_key)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain(api_key)

    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    return response



    