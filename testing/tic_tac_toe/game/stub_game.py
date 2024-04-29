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
