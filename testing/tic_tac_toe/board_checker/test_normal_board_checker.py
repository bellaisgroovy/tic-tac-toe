from unittest import TestCase
from src.tic_tac_toe.board_checker.normal_board_checker import NormalBoardChecker
from src.tic_tac_toe.data.game_state import GameState


class TestNormalBoardChecker(TestCase):
    def test_isGameOver_draw_true(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [2, 1, 1], [1, 2, 1]]

        is_game_over = board_checker.is_game_over(board)

        self.assertTrue(is_game_over)

    def test_isGameOver_win_true(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [1, 1, 1], [1, 2, 1]]

        is_game_over = board_checker.is_game_over(board)

        self.assertTrue(is_game_over)

    def test_isGameOver_loss_true(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [2, 1, 1], [2, 2, 1]]

        is_game_over = board_checker.is_game_over(board)

        self.assertTrue(is_game_over)

    def test_isGameOver_ongoing_false(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [2, 0, 1], [0, 2, 1]]

        is_game_over = board_checker.is_game_over(board)

        self.assertFalse(is_game_over)

    def test_isFull_oneSpace_false(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [2, 1, 1], [0, 2, 1]]

        is_full = board_checker.is_full(board)

        self.assertFalse(is_full)

    def test_isFull_full_false(self):
        board_checker = NormalBoardChecker()
        board = [[2, 1, 2], [2, 1, 1], [1, 2, 1]]

        is_full = board_checker.is_full(board)

        self.assertTrue(is_full)

    def test_isWinOrLoss_horizontalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_verticalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_diagonalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_otherDiagonalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isDirMatch_otherDiagonalMatch_True(self):
        board_checker = NormalBoardChecker()
        board = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

        is_match = board_checker.is_dir_match(
            board, coord={'x': 0, 'y': 2},
            matches=1,
            get_next_coord=board_checker.get_next_coord_other_xy
        )

        self.assertTrue(is_match)

    def test_isMatch_otherDiagonalMatch_True(self):
        board_checker = NormalBoardChecker()
        board = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

        is_match = board_checker.is_match(board, coord={'x': 0, 'y': 2})

        self.assertTrue(is_match)

    def test_isWinOrLoss_diagonalLoss_loss(self):
        board_checker = NormalBoardChecker()
        board = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.LOSS
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_ongoingL_none(self):
        board_checker = NormalBoardChecker()
        board = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_twoRow_none(self):
        board_checker = NormalBoardChecker()
        board = [[2, 2, 0], [0, 1, 1], [0, 0, 0]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_5173286_none(self):
        board_checker = NormalBoardChecker()
        board = [[1, 2, 0], [0, 1, 1], [2, 1, 2]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_5173286Mirror_none(self):
        board_checker = NormalBoardChecker()
        board = [[0, 2, 1], [1, 1, 0], [2, 1, 2]]

        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isMatchX_matchX_true(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0]
        ]
        inc_x = board_checker.get_next_coord_x
        coord = {'x': 0, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertTrue(is_match)

    def test_isMatchX_noMatchX_false(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        inc_x = board_checker.get_next_coord_y
        coord = {'x': 0, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertFalse(is_match)

    def test_isMatchY_matchY_true(self):
        board_checker = NormalBoardChecker()
        board = [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ]
        inc_x = board_checker.get_next_coord_y
        coord = {'x': 2, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertTrue(is_match)

    def test_isMatchY_noMatchY_false(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        inc_x = board_checker.get_next_coord_y
        coord = {'x': 0, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertFalse(is_match)

    def test_isMatchXY_matchXY_true(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        inc_x = board_checker.get_next_coord_xy
        coord = {'x': 0, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertTrue(is_match)

    def test_isMatchXY_noMatchXY_false(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        inc_x = board_checker.get_next_coord_xy
        coord = {'x': 0, 'y': 0}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertFalse(is_match)

    def test_isMatchOtherXY_matchOtherXY_true(self):
        board_checker = NormalBoardChecker()
        board = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
        inc_x = board_checker.get_next_coord_other_xy
        coord = {'x': 0, 'y': 2}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertTrue(is_match)

    def test_isMatchOtherXY_noMatchOtherXY_false(self):
        board_checker = NormalBoardChecker()
        board = [
            [1, 0, 1],
            [0, 0, 0],
            [0, 0, 1]
        ]
        inc_x = board_checker.get_next_coord_other_xy
        coord = {'x': 0, 'y': 2}
        matches = 1

        is_match = board_checker.is_dir_match(board, coord, matches, inc_x)

        self.assertFalse(is_match)
