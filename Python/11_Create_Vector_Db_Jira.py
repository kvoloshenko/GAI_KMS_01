import AI_Tools as tls
from loguru import logger # Import logger
# Converting a CSV file to an JSON file
# Import csv and json modules
import csv
import json
# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader

def csv_to_json(csv_file_path, json_file_path):
    # Function to convert a CSV file to a JSON file
    # Read CSV file and transform data
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        rows = list(csv_reader)

    # Write data to JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    logger.add("Log/11_Create_Vector_Db_Jira.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('11_Create_Vector_Db_Jira............')
    # Define file paths and convert CSV file to JSON file
    csv_file_path = './Dataset/jira_tickets_10k.csv'
    json_file_path = './Dataset/jira_tickets_10k.json'
    csv_to_json(csv_file_path, json_file_path)

    # Load JSON data into a Langchain TextLoader
    loader = TextLoader(json_file_path, encoding='UTF-8')
    documents = loader.load()


