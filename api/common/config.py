import os 
from dotenv import load_dotenv, find_dotenv
from loguru import logger
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if OPENAI_API_KEY:
    logger.debug("OPENAI_API_KEY was loaded successfully!")
else:
    logger.debug("Failed to load OPENAI_API_KEY from the .env file.")
