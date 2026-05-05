```md
# 🎲 Taverna RPG Engine

Backend experimental para um sistema de RPG em tempo real inspirado em **Foundry VTT / Roll20**, com:

- ⚡ FastAPI (WebSocket + REST API)
- 🎲 Engine de rolagem em Haskell (WAI/Warp)
- 🧠 Sistema de eventos (Event Sourcing leve)
- 🏰 Sistema de salas (rooms)
- ⚔️ Combat Engine estilo D&D 5e (HP, AC, turnos, initiative)
- 🔄 Estado sincronizado via WebSocket

---

# 🚀 Visão geral

O projeto separa responsabilidades em três camadas:

### 1. API (Python / FastAPI)
Responsável por:
- WebSockets
- Rooms
- Players
- Combat flow
- Event handling
- Broadcast de estado

---

### 2. Engine de dados (Haskell)
Responsável por:
- Parsing de expressões tipo `2d6+3`
- Rolagem determinística / pseudo-aleatória
- Retorno estruturado dos dados

---

### 3. State System (Event Sourcing leve)
Cada sala mantém:
- Estado atual (`room.state`)
- Lista de eventos (`room.events`)
- Rebuild do estado a partir dos eventos

---

# 📡 WebSocket Protocol

### Conexão:
```

ws://localhost:8000/ws/{room_id}

````

### Primeiro pacote obrigatório:
```json
{
  "name": "PlayerName"
}
````

---

## 🎮 Eventos suportados

### 🎲 Roll

```json
{
  "type": "roll",
  "expression": "2d6+3"
}
```

---

### ⚔️ Combat start

```json
{
  "type": "combat_start"
}
```

---

### 🎯 Initiative

```json
{
  "type": "initiative"
}
```

---

### ▶️ Next turn

```json
{
  "type": "next_turn"
}
```

---

# 🧠 Combat System (D&D 5e simplificado)

Cada room possui:

```json
"combat": {
  "active": false,
  "round": 0,
  "turn_index": 0,
  "initiative": [],
  "current_turn_user_id": null
}
```

---

## 📌 Regras implementadas

* Initiative roll (1d20)
* Turn order por maior iniciativa
* Round tracking
* Turn rotation automática
* HP system (em progresso)
* Status effects (poisoned, dead, etc)
* AC (planejado)
* Spells (planejado)

---

# 🧾 Event Sourcing

Cada ação gera um evento:

```python
Event(
    type="roll",
    user="player1",
    data={...}
)
```

### Eventos possíveis:

* `user_joined`
* `roll`
* `combat_start`
* `initiative_roll`
* `damage`
* `heal`
* `status_applied`
* `turn_changed`

---

## 🔁 Rebuild state (core idea)

```python
def rebuild_state(self):
    self.state = initial_state()

    for event in self.events:
        self.apply(event)
```

---

# ⚙️ Backend (FastAPI)

## Rodar API:

```bash
uv run uvicorn main:app --reload
```

ou:

```bash
python -m uvicorn main:app --reload
```

---

## Debug endpoint:

```
GET /debug/{room_id}
```

---

# 🎲 Haskell Dice Engine

## Rodar engine:

```bash
cd backend/engine
stack run
```

ou:

```bash
cabal run
```

---

## Endpoint:

```
POST /engine/roll
```

### Exemplo:

```bash
curl -X POST http://localhost:8080/engine/roll \
  -H "Content-Type: application/json" \
  -d '{"expression": "2d6+3"}'
```

---

## Resposta:

```json
{
  "result": 13,
  "rolls": [4, 6],
  "modifier": 3
}
```

---

# 🧪 Testes WebSocket

```bash
uv run python3 scripts/wstest.py
```

---

# 🧩 Estrutura do projeto

```
backend/
 ├── api/
 │   ├── main.py
 │   ├── src/
 │   │   ├── ws/
 │   │   ├── services/
 │   │   ├── combat/
 │   │   ├── models/
 │   │   ├── room.py
 │   │   └── connection_manager.py
 │   └── scripts/
 │       └── wstest.py
 │
 ├── engine/
 │   ├── Main.hs
 │   ├── Dice.hs
 │   └── Parser.hs
```

---

# 🧠 TO-DO (Roadmap real do projeto)

## 🔥 Core (próximo passo)

* [ ] Fix final do event system (type-safe events)
* [ ] Replace dict events por dataclasses
* [ ] Persistência (SQLite / Postgres)
* [ ] Redis pub/sub para rooms

---

## ⚔️ Combat Engine (Foundry-lite)

* [ ] HP system completo
* [ ] AC + hit/miss system
* [ ] Damage types
* [ ] Spells system (JSON-driven)
* [ ] Buff/Debuff system
* [ ] Status durations
* [ ] Reactions (opportunity attack)

---

## 🧠 AI / Rules Engine

* [ ] Rule resolver (D&D 5e ruleset)
* [ ] Advantage / disadvantage
* [ ] Critical hits
* [ ] Saving throws
* [ ] Skill checks

---

## 🌐 WebSocket improvements

* [ ] Reconnect system
* [ ] Presence system
* [ ] Room persistence
* [ ] Spectator mode
* [ ] Chat system

---

## 🎮 UX (Frontend futuro)

* [ ] Battle map
* [ ] Initiative tracker UI
* [ ] Dice animation
* [ ] Character sheets

---

## 🧪 Testes

* [ ] Testes unitários combat engine
* [ ] Testes de event sourcing
* [ ] Load test WebSocket

---

# 🧨 Problemas conhecidos

* Eventos ainda usam `dict` (precisa padronizar)
* Combat engine pode quebrar com lista vazia
* Status system ainda incompleto
* Falta validação de payload WebSocket

---

# 🧭 Ideia final do projeto

O objetivo é evoluir isso para:

> Um **Foundry VTT backend minimalista**, open-source, modular e hackável.

---

# ⚡ Stack

* Python (FastAPI)
* Haskell (Dice Engine)
* WebSocket (real-time state sync)
* Event Sourcing (custom)
* JSON protocol simples

---

# 📜 Licença

MIT (ou livre, depende do seu uso futuro)

---

```
