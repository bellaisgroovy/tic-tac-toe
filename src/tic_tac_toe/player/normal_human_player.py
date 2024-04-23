from src.tic_tac_toe.player.player import Player


class NormalHumanPlayer(Player):
    def move(self, board):
        valid = False
        print("Which square would you like to move in?")
        while not valid:
            square = self.__get_input_square()
            xy_dict = self.__assign_xy_to_square(square)
            valid = self.__is_valid_move(board, xy_dict)
            if not valid:
                self.__print_move_instructions()
        return xy_dict

    def __get_input_square(self):  # not private for mocking
        valid = False
        square = -1
        while not valid:
            try:
                square = int(self.input_wrap("square (use numpad) : "))
                valid = True
            except ValueError:
                valid = False
            if not 0 < square < 10:
                valid = False
            if not valid:
                self.__print_move_instructions()
        return square

    @staticmethod
    def __is_valid_move(board, move_dict):
        x = move_dict["x"]
        y = move_dict["y"]
        if board[x][y] != 0:
            return False
        return True

    @staticmethod
    def __assign_xy_to_square(square):
        match square:
            case 7:
                xy_dict = {"x": 0, "y": 0}
            case 8:
                xy_dict = {"x": 1, "y": 0}
            case 9:
                xy_dict = {"x": 2, "y": 0}
            case 4:
                xy_dict = {"x": 0, "y": 1}
            case 5:
                xy_dict = {"x": 1, "y": 1}
            case 6:
                xy_dict = {"x": 2, "y": 1}
            case 1:
                xy_dict = {"x": 0, "y": 2}
            case 2:
                xy_dict = {"x": 1, "y": 2}
            case 3:
                xy_dict = {"x": 2, "y": 2}
            case _:
                raise ValueError("square must be num 1-9")
        return xy_dict

    @staticmethod
    def __print_move_instructions():
        print("please input a number below corresponding to square")
        print("789")
        print("456")
        print("123")

    @staticmethod
    def input_wrap(msg):  # wrapped and public for mocking
        return input(msg)
