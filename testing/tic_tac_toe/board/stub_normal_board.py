from src.tic_tac_toe.board.normal_board import NormalBoard


class WinStubNormalBoard(NormalBoard):
    def get_board(self):
        return [[1, 1, 1],
                [0, 0, 0],
                [0, 0, 0]]


class LoseStubNormalBoard(NormalBoard):
    def get_board(self):
        return [[2, 2, 2],
                [0, 0, 0],
                [0, 0, 0]]


class DrawStubNormalBoard(NormalBoard):
    def get_board(self):
        return [[2, 1, 2],
                [1, 2, 2],
                [1, 2, 1]]
