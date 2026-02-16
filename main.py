import os
from dotenv import load_dotenv

from src.msdown_repository import MsDownRepository

load_dotenv()

SYSTEM_ID = os.getenv("SYSTEM_ID")

response = MsDownRepository.get_services(SYSTEM_ID)
