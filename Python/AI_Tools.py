import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS # Import FAISS module
from loguru import logger # Import logger
import time
# Import necessary modules for splitting text into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# Loading values from the ".env" file
API_KEY = os.environ.get("API_KEY")
os.environ["OPENAI_API_KEY"] = API_KEY
LL_MODEL='gpt-4o'
client = OpenAI(api_key=API_KEY)

# Function for requesting ChatGPT
def gpt_request(user_content, system_content):
  response = client.chat.completions.create(
    model=LL_MODEL,
    messages=[
      {"role": "system", "content": system_content}, # <-- This is the system message that provides context to the model
      {"role": "user", "content": user_content}     # <-- This is the user message for which the model will generate a response
    ]
  )
  return response.choices[0].message.content

# Function for Splitting documents
# RecursiveCharacterTextSplitter see here:
# https://python.langchain.com/v0.2/docs/how_to/recursive_text_splitter/
def split_documents(documents):
  # Function to split documents into chunks using RecursiveCharacterTextSplitter
    logger.debug('split_documents............')
    start_time = time.time()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0)
    source_chunks = text_splitter.split_documents(documents)
    logger.debug(type(source_chunks))
    logger.debug(len(source_chunks))
    logger.debug(source_chunks[10].metadata)
    # logger.debug(source_chunks[10].page_content)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'split_documents elapsed_time = {elapsed_time} sec')
    return source_chunks

# Function for Getting Embeddings Model from HuggingFace
# HuggingFaceEmbeddings see here:
# https://api.python.langchain.com/en/latest/huggingface/embeddings/langchain_huggingface.embeddings.huggingface.HuggingFaceEmbeddings.html#
def get_embeddings(type='cpu'):
  # Function to get the embeddings model from HuggingFace
    logger.debug('get_embeddings............')
    start_time = time.time()
    model_id = 'intfloat/multilingual-e5-large'
    if type=='cpu':
        model_kwargs = {'device': 'cpu'}
    else:
        model_kwargs = {'device': 'cuda'}
    embeddings = HuggingFaceEmbeddings(
        model_name=model_id,
        model_kwargs=model_kwargs
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'get_embeddings elapsed_time = {elapsed_time} sec')
    return embeddings

# Initialize embeddings
# embeddings = get_embeddings(type='cuda')

# Getting OpenAIEmbeddings
embeddings = embeddings = OpenAIEmbeddings()

# Function for creating a new Vector Knowledge Base
def create_db(source_chunks, embeddings, db_file_name):
  # Function to create FAISS vector database from document chunks
    start_time = time.time()
    logger.debug('create_db............')
    db = FAISS.from_documents(source_chunks, embeddings)
    db.save_local(db_file_name)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'create_db elapsed_time = {elapsed_time} sec')
    return db

# Function for loading an existing Vector Knowledge Base
def load_db(db_file_name, embeddings):
  logger.debug('load_db............')
  start_time = time.time()
  new_db = FAISS.load_local(db_file_name, embeddings, allow_dangerous_deserialization=True)
  end_time = time.time()
  elapsed_time = end_time - start_time
  logger.debug(f'load_db elapsed_time = {elapsed_time} sec')
  return new_db