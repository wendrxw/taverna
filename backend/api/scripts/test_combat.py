import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8000/ws/test-room"

    async with websockets.connect(uri) as ws:

        # login
        await ws.send(json.dumps({
            "name": "Tester"
        }))

        print("✅ conectado")

        # iniciar combate
        await ws.send(json.dumps({
            "type": "combat_start"
        }))

        # initiative
        await ws.send(json.dumps({
            "type": "initiative"
        }))

        await ws.send(json.dumps({
            "type": "initiative"
        }))

        # start round
        await ws.send(json.dumps({
            "type": "start_round"
        }))

        # next turn
        await ws.send(json.dumps({
            "type": "next_turn"
        }))

        # ouvir respostas
        while True:
            msg = await ws.recv()
            print("📥", msg)

asyncio.run(test())