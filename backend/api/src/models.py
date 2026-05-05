from dataclasses import dataclass
from typing import Any
import time


@dataclass
class Event:
    type: str
    user: str | None
    data: Any
    timestamp: float = time.time()