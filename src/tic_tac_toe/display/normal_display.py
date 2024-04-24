from src.tic_tac_toe.display.display import Display
from copy import deepcopy

class NormalDisplay(Display):
    def display(self, board):
        nice_board = self.__replace_symbols(board)
        self.__print_board(nice_board)

    @staticmethod
    def __replace_symbols(board):
        nice_board = deepcopy(board)
        for x, row in enumerate(board):
            for y, symbol in enumerate(row):
                match symbol:
                    case 0:
                        nice_board[y][x] = " "
                    case 1:
                        nice_board[y][x] = "X"
                    case 2:
                        nice_board[y][x] = "O"
        return nice_board

    @staticmethod
    def __print_board(board):
        for row in board:
            print("|", end="")
            for symbol in row:
                print(symbol, end="|")
            print()
