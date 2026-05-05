import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8000/ws/test-room"

    print("🔌 conectando...")

    async with websockets.connect(uri) as ws:
        print("✅ conectado")

        print("📤 enviando nome...")
        await ws.send(json.dumps({
            "name": "Tester"
        }))

        print("📤 enviando roll...")
        await ws.send(json.dumps({
            "type": "roll",
            "expression": "2d6+3"
        }))

        print("⏳ esperando resposta...")
        response = await ws.recv()

        print("📥 resposta:", response)

asyncio.run(test())