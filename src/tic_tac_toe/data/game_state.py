from enum import Enum


class GameState(Enum):
    ONGOING = -1
    LOSS = 0
    DRAW = 1
    WIN = 2
