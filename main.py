from typing import Union
from fastapi import FastAPI
import requests
from prometheus_fastapi_instrumentator import Instrumentator
import logging.config

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # logger.info("Testing logger")
    return {"item_id": item_id, "q": q}

Instrumentator().instrument(app).expose(app)