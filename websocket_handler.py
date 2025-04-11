from fastapi import WebSocket
from typing import List

# 接続中のクライアントリスト保持
connected_clients: List[WebSocket] = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                if client.client_state.name == "CONNECTED":
                    await client.send_text(f"受け取ったで: {data}")
    except:
        pass
    finally:
        connected_clients.remove(websocket)
