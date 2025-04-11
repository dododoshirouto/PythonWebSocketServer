import os
import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from websocket_handler import websocket_endpoint

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)

base_dir = get_base_dir()
static_dir = os.path.join(base_dir)

app = FastAPI()

app.websocket("/ws")(websocket_endpoint)
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
