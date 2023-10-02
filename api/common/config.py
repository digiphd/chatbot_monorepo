import os 
from dotenv import load_dotenv, find_dotenv
from loguru import logger
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
