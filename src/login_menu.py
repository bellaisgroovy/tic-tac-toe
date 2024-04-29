from src.menu import Menu
from src.tic_tac_toe.data.game_state import GameState


class LoginMenu(Menu):
    current_user = None

    def __init__(self, game, login_handler):
        super().__init__(game)
        self.login_handler = login_handler

    def play(self):
        end_state = self.game.play()
        if end_state == GameState.DRAW:
            print('It was a draw.')
        elif end_state == GameState.LOSS:
            print('O won!')
        elif self.current_user is None and end_state.value == GameState.WIN.value:
            print('X won!')
        else:
            print(f'{self.current_user} won!')
        return end_state

    def quit(self):
        print('bye xo')
        exit(0)

    def login(self):
        self.current_user = self.login_handler.login()

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
