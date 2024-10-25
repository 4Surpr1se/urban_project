import asyncio

import websockets
import json


async def test_websocket():
    uri = "ws://localhost:8000/graphql"
    async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
        subscription_message = {
            "id": "1",
            "type": "start",
            "payload": {
                "query": "subscription { count }"
            }
        }

        await websocket.send(json.dumps(subscription_message))
        response = {'type': 'data'}
        while response['type'] == 'data':
            response = json.loads(await websocket.recv())
            print("Received:", response)




asyncio.run(test_websocket())
