import re
import AI_Tools as tls
from loguru import logger # Import logger
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load JSON data into a Langchain TextLoader
json_file_path = './Dataset/moon_flight_system_data_10k.json'
loader = TextLoader(json_file_path, encoding = 'UTF-8')
documents = loader.load()

# Split the loaded documents using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0)
confluence_source_chunks = text_splitter.split_documents(documents)

# Loading an existing Vector Knowledge Base
confluence_db_file_name = './Db/DB_Confluence'
confluence_db = tls.load_db(confluence_db_file_name, tls.embeddings)

if __name__ == "__main__":
    logger.add("Log/22_RAG_Confluence.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('22_RAG_Confluence............')
    confluence_topic = "How to install Moon Flight System? Give me the main details."
    confluence_message_content = tls.get_message_content_ensemble(confluence_topic, confluence_db, confluence_source_chunks, 10)
    system_content = '''You are a useful assistant.
    You have data on the necessary docs in Confluence.'''
    user_content = f'{confluence_topic}. The data is here: {confluence_message_content}'
    response = tls.gpt_request(user_content, system_content)
    logger.debug(f'response={response}')