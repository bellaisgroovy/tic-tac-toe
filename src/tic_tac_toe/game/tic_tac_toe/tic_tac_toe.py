from src.tic_tac_toe.game.game import Game
from src.tic_tac_toe.player.player import Player
from src.tic_tac_toe.board.board import Board
from src.tic_tac_toe.board_checker.board_checker import BoardChecker
from src.tic_tac_toe.display.display import Display


class TicTacToe(Game):
    def __init__(
            self,
            no_players=2,
            size_line_to_win=3,
            player=Player(),
            board=Board(),
            board_checker=BoardChecker(),
            display=Display()
    ):
        self.players = [player for i in range(no_players)]  # non referential
        self.board_gen = board
        self.board_checker = board_checker
        self.displayer = display
        self.size_line_to_win = size_line_to_win

    def play(self):
        board = self.get_board()
        turn = 0
        while not self.is_game_over(board):
            current_player_index = (turn % 2)
            self.display(board)
            move_dict = self.players[current_player_index].move(board)

            symbol = current_player_index + 1
            board[move_dict['x']][move_dict['y']] = symbol
            turn += 1
        return self.get_end_state(board)

    def display(self, board):
        self.displayer.display(board)

    def is_game_over(self, board):
        is_game_over = self.board_checker.is_game_over(board)
        return is_game_over

    def get_end_state(self, board):
        end_state = self.board_checker.get_end_state(board, self.size_line_to_win)
        return end_state

    def get_board(self):
        board = self.board_gen.get_board()
        return board
