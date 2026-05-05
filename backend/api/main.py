import uuid
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from src.engine_client import roll_dice
from src.schemas.roll import RollRequest
from src.room import initial_state
from src.services.room_manager import RoomManager
from src.connection_manager import ConnectionManager
from src.ws.handler import handle_ws
from src.models import Event


app = FastAPI()
room_manager = RoomManager()
conn_manager = ConnectionManager()

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    room = room_manager.get(room_id)

    init = await websocket.receive_json()
    name = init.get("name", "Anonymous")

    user = {
        "id": str(uuid.uuid4()),
        "name": name
    }

    # 🔥 1. REGISTRAR PLAYER NO STATE (ESSENCIAL)
    room.state["players"][user["id"]] = {
        "id": user["id"],
        "name": name,
        "hp": 30,
        "ac": 12,
        "status": []
    }

    # 🔥 2. EVENT: JOIN
    room.add_event(Event(
        type="user_joined",
        user=name,
        data=user
    ))

    await conn_manager.broadcast(room, {
        "type": "state_sync",
        "state": room.state
    })

    try:
        while True:
            msg = await websocket.receive_json()

            await handle_ws(
                room,
                websocket,
                user,
                msg,
                roll_dice,
                conn_manager.broadcast
            )

    except WebSocketDisconnect:
        # 🔥 cleanup importante
        room.state["players"].pop(user["id"], None)

        room.add_event(Event(
            type="user_left",
            user=name,
            data=user
        ))

        await conn_manager.broadcast(room, {
            "type": "state_sync",
            "state": room.state
        })


# ------------------------
# REST API fallback
# ------------------------
@app.post("/roll")
async def roll(req: RollRequest):
    result = await roll_dice(expression=req.expression)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result


@app.get("/debug/{room_id}")
def debug(room_id: str):
    room = room_manager.get(room_id)
    return {
        "state": room.state,
        "events": len(room.events)
    }