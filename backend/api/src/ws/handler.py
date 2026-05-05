from src.services.combat_service import CombatService
from src.models import Event


service = CombatService()

async def handle_ws(room, websocket, user, msg, roll_dice, broadcast):

    result = await service.handle(room, msg, user, roll_dice)

    if result:
        room.add_event(Event(
            type=result["type"],
            user=result.get("user", "system"),
            data=result
        ))

    await broadcast(room, {
        "type": "state_update",
        "state": room.state
    })