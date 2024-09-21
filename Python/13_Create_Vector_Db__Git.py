# Importing necessary libraries and modules
import AI_Tools as tls
import time
from loguru import logger # Import logger
from git import Repo
from langchain_community.document_loaders import GitLoader

if __name__ == "__main__":
    # Configure the logger to write logs to a file with specific settings
    logger.add("Log/13_Create_Vector_Db__Git.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('13_Create_Vector_Db__Git............')
    start_time = time.time()

    # Load existing repository from disk
    repo = Repo.clone_from('https://github.com/kvoloshenko/Kind_Doctor_TG_Bot_01.git',
                           to_path="./Git_Kind_Doctor")
    # branch = repo.head.reference
    branch = "master"

    branch = repo.head.reference
    loader = GitLoader(repo_path="./Git_Kind_Doctor/", branch=branch)
    data = loader.load()
    logger.debug(len(data))
    logger.debug(data[0])

    # Filtering files to load
    # e.g. loading only python files
    loader = GitLoader(
        repo_path="./Git_Kind_Doctor",
        file_filter=lambda file_path: file_path.endswith(".py"),
    )
    docs = loader.load()
    logger.debug(len(docs))

    doc_sources = [doc.metadata["source"] for doc in docs]
    logger.debug(doc_sources)

    # Splitting documents
    git_source_chunks = tls.split_documents(docs)

    # Creating Vector Knowledge Base
    git_db_file_name = './Db/Git_Kind_Doctor'
    git_db = tls.create_db(git_source_chunks, tls.embeddings, git_db_file_name)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'13_Create_Vector_Db__Git elapsed_time = {elapsed_time} sec')

