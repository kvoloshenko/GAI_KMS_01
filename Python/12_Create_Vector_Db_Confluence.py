import AI_Tools as tls
from loguru import logger # Import logger
# Converting a CSV file to an JSON file
# Import csv and json modules
import csv
import json
from langchain_core.documents import Document
# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

if __name__ == "__main__":
    logger.add("Log/12_Create_Vector_Db_Confluence.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('12_Create_Vector_Db_Confluence............')
    # Load JSON content from the file
    file_name = './Dataset/moon_flight_system_data_10k.json'
    with open(file_name, 'r') as f:
        confluence_data = json.load(f)
    # Create Langchain Document objects from JSON data
    confluence_documents = []
    for d in confluence_data:
        confluence_documents.append(Document(page_content=d['page_content'], metadata=d['metadata']))
    logger.debug(len(confluence_documents))
    # Split Confluence documents into chunks
    logger.debug(len(confluence_documents))
    confluence_source_chunks = tls.split_documents(confluence_documents)
    # Create the FAISS vector database for Confluence data
    confluence_db_file_name = './Db/DB_Confluence'
    confluence_db = tls.create_db(confluence_source_chunks, tls.embeddings, confluence_db_file_name)