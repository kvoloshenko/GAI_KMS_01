import re
import AI_Tools as tls
from loguru import logger # Import logger
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load JSON data into a Langchain TextLoader
json_file_path = './Dataset/jira_tickets_10k.json'
loader = TextLoader(json_file_path, encoding = 'UTF-8')
documents = loader.load()

# Split the loaded documents using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0)
jira_source_chunks = text_splitter.split_documents(documents)

# Loading an existing Vector Knowledge Base
jira_db_file_name = './Db/DB_Jira'
jira_db = tls.load_db(jira_db_file_name, tls.embeddings)

if __name__ == "__main__":
    logger.add("Log/21_RAG_Jira.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('21_RAG_Jira............')
    jira_topic = "Give me tickets related to Moon Flight System. I need Ticket id, Summary and Project name."
    jira_message_content = tls.get_message_content_ensemble(jira_topic, jira_db, jira_source_chunks, 10)
    system_content = '''You are a useful assistant.
    You have data on the necessary tickets in Jira..'''
    user_content = f'{jira_topic}. The data is here: {jira_message_content}'
    response = tls.gpt_request(user_content, system_content)
    logger.debug(f'response={response}')