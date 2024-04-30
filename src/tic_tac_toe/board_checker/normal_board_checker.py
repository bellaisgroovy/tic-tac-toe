from src.tic_tac_toe.board_checker.board_checker import BoardChecker
from src.tic_tac_toe.data.game_state import GameState


class NormalBoardChecker(BoardChecker):
    def is_game_over(self, board, size_line_to_win=3):
        if self.get_end_state(board, size_line_to_win) != GameState.ONGOING:
            return True
        return False

    def get_end_state(self, board, size_line_to_win):
        win_or_loss = NormalBoardChecker.win_or_loss(board)
        if win_or_loss is not None:
            return win_or_loss
        elif NormalBoardChecker.is_full(board):
            return GameState.DRAW
        else:
            return GameState.ONGOING

    @staticmethod
    def win_or_loss(board):
        # for each cell
        for x in range(len(board)):
            print('x',x)
            for y in range(len(board)):
                print('y',y)
                coord = {'x': x, 'y': y}
                symbol = board[x][y]

                is_match = NormalBoardChecker.is_match(board, coord)

                if is_match:
                    if symbol == 1:
                        return GameState.WIN
                    elif symbol == 2:
                        return GameState.LOSS
        return None

    @staticmethod
    def is_full(board):
        is_draw = True
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 0:
                    is_draw = False
        return is_draw

    @staticmethod
    def is_match(board, coord):
        print('coord', coord)
        matches = 1
        is_match = (  # loop was more verbose so minor duplication
                NormalBoardChecker.is_dir_match(board, coord, matches, NormalBoardChecker.get_next_coord_x) or
                NormalBoardChecker.is_dir_match(board, coord, matches, NormalBoardChecker.get_next_coord_y) or
                NormalBoardChecker.is_dir_match(board, coord, matches, NormalBoardChecker.get_next_coord_xy) or
                NormalBoardChecker.is_dir_match(board, coord, matches, NormalBoardChecker.get_next_coord_other_xy)
        )
        return is_match

    @staticmethod
    def is_dir_match(board, coord, matches, get_next_coord):
        if matches == len(board):
            return True

        next_coord = get_next_coord(coord)

        in_range = 0 <= next_coord['x'] < len(board) and 0 <= next_coord['y'] < len(board)
        is_match = False
        if in_range:
            is_match = board[coord['x']][coord['y']] == board[next_coord['x']][next_coord['y']]

        if in_range and is_match:
            matches += 1
            has_won = NormalBoardChecker.is_dir_match(board, next_coord, matches, get_next_coord)
            if has_won:
                return True
        return False

    @staticmethod
    def get_next_coord_y(coord):
        return {'x': coord['x'], 'y': coord['y'] + 1}

    @staticmethod
    def get_next_coord_x(coord):
        return {'x': coord['x'] + 1, 'y': coord['y']}

    @staticmethod
    def get_next_coord_xy(coord):
        return {'x': coord['x'] + 1, 'y': coord['y'] + 1}

    @staticmethod
    def get_next_coord_other_xy(coord):
        return {'x': coord['x'] + 1, 'y': coord['y'] - 1}
