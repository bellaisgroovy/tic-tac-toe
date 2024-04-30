from src.tic_tac_toe.game.game import Game
from src.tic_tac_toe.data.game_state import GameState


class StubWinGame(Game):
    def play(self):
        return GameState.WIN


class StubDrawGame(Game):
    def play(self):
        return GameState.DRAW


class StubLoseGame(Game):
    def play(self):
        return GameState.LOSS


class FakeWinLoseWin(Game):
    def __init__(self):
        self.counter = 0

    def play(self):
        self.counter += 1
        if self.counter % 2 == 1:
            return GameState.WIN
        else:
            return GameState.LOSS
