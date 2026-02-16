# Bot - MySystemDown
Este repositório contém o código-fonte do BOT responsável por monitorar a disponibilidade de endpoints (healthcheck) previamente configurados no ecossistema MySystemDown.

---

# Como Rodar

## Pré-Requisitos
Para o BOT funcionar normalmente é necessário primeiramente ter um *serviço de filas*, como Redis ou RabbitMQ.

O sistema depende de dois processos simultâneos:
- **Celery Beat**: O "relógio" que agenda as verificações.
- **Celery Worker**: O "executor" que realiza as requisições de healthcheck.

## Configure as variáveis de ambiente
Configure as variáveis de ambiente corretamente, indicando o endereço do serviço de mensageria e da API do MySystemDown. 
```shell
cp .env.example .env
```

## Iniciando Celery Worker
``` shell
uv run celery -A src.celery worker --loglevel=INFO
```

## Iniciando Celery Beat
``` shell
uv run celery -A src.celery beat --loglevel INFO
```