from datetime import timedelta
from src.models.service_model import Service

class TaskService:

    @staticmethod
    def create_tasks(data: dict) -> dict:
        services = (
            Service(
                title=service["title"],
                url=service["url"],
                interval=service["health_check_interval"]
            ) 
            for service in data
        )

        beat_schedule = {}

        for service in services:
            beat_schedule[service.title.strip().lower().replace(" ", "_")] = {
                "task": "src.tasks.request_healthcheck",
                "schedule": timedelta(minutes=service.interval),
                "args": (service.url,)
            }
        
        return beat_schedule
