import requests
from src.celery import app

@app.task
def request_healthcheck(url: str):
    return requests.get(url)