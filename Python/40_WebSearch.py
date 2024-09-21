# Importing necessary libraries and modules
from loguru import logger # Import logger
import time
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

if __name__ == "__main__":
    # Configure the logger to write logs to a file with specific settings
    logger.add("Log/40_WebSearch.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB",
               compression="zip")
    logger.debug('40_WebSearch............')
    start_time = time.time()
    # Request data, system prompt
    search_query = 'Describe how to use Sy policy in 5g'
    search_results = search.run(search_query)
    logger.debug(f'search_results={search_results}')
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.debug(f'40_WebSearch elapsed_time = {elapsed_time} sec')