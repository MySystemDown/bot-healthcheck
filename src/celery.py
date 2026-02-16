from celery import Celery

from src.services.task_service import TaskService
from src.repositories.msdown_repository import MsDownRepository
from src.setttings import Settings

app = Celery('bot-msdown', 
                broker=f'pyamqp://{Settings.BROKER_USER}@{Settings.BROKER_HOST}:{Settings.BROKER_PORT}//',
                include=['src.tasks'] 
            )

# Busca os serviços do sistema para realizar o healthcheck
response = MsDownRepository.get_services(Settings.SYSTEM_ID)

# Cria as tarefas
app.conf.beat_schedule = TaskService.create_tasks(response.json())