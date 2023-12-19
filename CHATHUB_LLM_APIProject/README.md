
# LLM-ChatHub: AI Data Analyst 📊

The LLM-ChatHub is an AI-powered data analyst chatbot designed to assist users in extracting valuable insights from unstructured text data available in different sources. The chatbot integrates various natural language processing (NLP) techniques and utilizes the LangChain library, including OpenAI models for language understanding and FAISS for efficient document retrieval.

## Features of this Chatbot:

  - Importing URLs or uploading text documents containing web links for article retrieval.
  - Utilizing LangChain's UnstructuredURL Loader to analyze and preprocess article content.
  - Generating embedding vectors using OpenAI's embeddings, enhancing the efficiency of information retrieval.
  - Employing FAISS, a robust similarity search library, to swiftly retrieve pertinent data.
  - Engaging with the LLM (Chatgpt) by entering queries and receiving responses alongside source URLs.


## How to install:

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Smohanta23/LLM_CHATBOT.git

```
2. Download the required packages and libraries using pip:

```bash
  pip install -r requirements.txt
```
4.Get your OpenAI API key by creating a .env file in the project root and adding your API

# You can get your API key from https://platform.openai.com/api-keys
```bash
  OPENAI_API_KEY=your_api_key_here
```
## How to run:

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```
  - Access the web application through your browser.

  - Enter URLs directly in the sidebar for quick input.

  - Start the data loading and processing by selecting "Process URLs."

  - Witness the system executing text splitting, creating embedding vectors, and optimizing indexing with FAISS.

  - Save and index the embeddings using FAISS, boosting retrieval speed.

  - Store the FAISS index in a local file path in pickle format for future reference.

  - Now, inquire and receive answers based on the curated news articles.

## Project Structure

  - main.py: Primary script for the Streamlit application.
  - requirements.txt: Document listing necessary Python packages for the project.
  - faiss_store_openai.pkl: Pickle file housing the FAISS index.
  - .env: Configuration file for secure storage of your OpenAI API key.