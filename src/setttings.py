import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SYSTEM_ID = os.getenv("SYSTEM_ID")
    API_TOKEN = os.getenv("API_TOKEN")
    API_URL = os.getenv("API_URL")
    
    BROKER_HOST=os.getenv("BROKER_HOST")
    BROKER_PORT=os.getenv("BROKER_PORT")
    BROKER_USER=os.getenv("BROKER_USER")
    BROKER_PASSWORD=os.getenv("BROKER_PASSWORD")