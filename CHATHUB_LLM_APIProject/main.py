import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Adding custom CSS for background styles
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E; 
            color: #FFFFFF; 
            font-family: 'Roboto', sans-serif; 
            padding: 20px; 
        }
        .stApp {
            max-width: 100%; 
        }
        h1, h2, h3, h4, h5, h6 {
            color: #000000; 
        }
        .stButton {
            width: 100%; 
            text-align: center; 
            padding: 20px; 
            font-size: 14px; 
        }
        .stTextInput input {
            background-color: #C0C0C0; 
            color: #000000; 
            font-size: 14px;
        }
        .sidebar-content .stTextInput label, .sidebar-content .stTextInput input {
            color: #000000;
            font-size: 14px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #FFFFFF;
            color: #000000;
            text-align: right;
            padding: 10px;
            font-size: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML and CSS for the main title with animation
st.write(
    """
    <div>
        <h1 id="title" style='text-align: center; margin-left: 0; animation: moveTitle 1s infinite;'>LLM-ChatHub: AI Data Analyst 📊</h1>
        <style>
            @keyframes moveTitle {
                0% { margin-left: 0; }
                50% { margin-left: 40px; }
                100% { margin-left: 0; }
            }
        </style>
    </div>
    """,
    unsafe_allow_html=True
)

# Adding loading animation
with st.spinner("Unwrapping the BOT......"):
    try:
        time.sleep(2)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Using customized fonts
st.markdown(
    """
    <style>
        body {
            font-family: 'Roboto', sans-serif; 
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Using markdown for the sidebar title
st.sidebar.markdown(
    """
    <h1>Reference URLs......</h1>
    """,
    unsafe_allow_html=True
)

# Prompting the user for the number of URLs
num_urls = st.sidebar.number_input("Enter the number of URLs to be put", min_value=1, max_value=10, value=3)

# Creating an empty list to store URLs
urls = []

# Using a for loop to get user input for URLs
for i in range(num_urls):

    url = st.sidebar.text_input(f"URL {i+1}", value=st.session_state.get(f"url_input_{i}", ""))
    st.session_state[f"url_input_{i}"] = url
    urls.append(url)

# Adding a button to trigger processing
process_url_clicked = st.sidebar.button("Process URLs", key="process_button")

# Defining the file path for saving the FAISS index
file_path = "faiss_store_openai.pkl"

# Creating a main placeholder for updating messages
main_placeholder = st.empty()

# Initializing OpenAI with specific parameters
llm = OpenAI(temperature=0.9, max_tokens=500)

# Checking if the "Process URLs" button is clicked
if process_url_clicked:

    # Loading data from the provided URLs
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Loading data... 📚")
    data = loader.load()

    # Splitting data into documents
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Splitting text... 📄")
    docs = text_splitter.split_documents(data)

    # Creating embeddings and saving to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Building embedding vectors... 🚀")
    time.sleep(2)

    # Saving the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

# Displaying a question input field
query = st.text_input("Ask a question:")
if query:
    # Checking if the FAISS index file exists
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)

            # Creating a retrieval chain
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

            # Getting the result for the given question
            result = chain({"question": query}, return_only_outputs=True)

            # Displaying the answer
            st.header("Answer:")
            st.write(result["answer"])

            # Displaying sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(source)

# Adding a footer with copyright notice
st.markdown(
    """
    <div class="footer">
        © 2023 LLMChatBot. All rights reserved.
        <br>
        Version 1.0 | Last Updated: January 2, 2024
    </div>
    """,
    unsafe_allow_html=True
)
