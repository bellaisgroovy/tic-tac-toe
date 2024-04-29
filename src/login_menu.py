from src.menu import Menu
from tic_tac_toe.data.game_state import GameState


class LoginMenu(Menu):
    current_user = None

    def __init__(self, game, login_handler):
        super().__init__(game)
        self.login_handler = login_handler

    def play(self):
        end_state = self.game.play()
        if end_state == GameState.DRAW:
            print('It was a draw.')
        if self.current_user is None:
            if end_state.value == GameState.WIN.value:
                print('X won!')
            if end_state == GameState.LOSS:
                print('O won!')
        else:
            if end_state == GameState.WIN:
                print(f'{self.current_user} won!')
            if end_state == GameState.LOSS:
                print('O won!')
        return end_state

    def quit(self):
        quit('bye xo')

    def login(self):
        self.current_user = self.login_handler.login()

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
