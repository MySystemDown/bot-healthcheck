import requests
from uuid import UUID

from src.setttings import Settings

class MsDownRepository:
    API_TOKEN = Settings.API_TOKEN
    API_URL = Settings.API_URL

    BASE_HEADERS = {"api-token": f"{API_TOKEN}"}

    @staticmethod
    def get_services(system_id: UUID):
        return requests.get(
            f"{MsDownRepository.API_URL}/systems/{system_id}/services", 
            headers=MsDownRepository.BASE_HEADERS)