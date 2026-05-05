import httpx


ENGINE_URL = "http://localhost:8080/engine/roll"

async def roll_dice(expression: str):
    async with httpx.AsyncClient(timeout=2.0) as client:
        try:
            response = await client.post(
                ENGINE_URL,
                json={"expression": expression}
            )

            response.raise_for_status()
            return response.json()

        except httpx.RequestError:
            return {"error": "Engine unavailable"}

        except httpx.HTTPStatusError as e:
            return {"error": f"Engine error: {e.response.text}"}
