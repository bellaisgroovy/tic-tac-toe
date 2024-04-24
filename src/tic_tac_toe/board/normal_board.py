from src.tic_tac_toe.board.board import Board


class NormalBoard(Board):
    def get_board(self):
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 0 = empty, no enum so no players can be dynamic
