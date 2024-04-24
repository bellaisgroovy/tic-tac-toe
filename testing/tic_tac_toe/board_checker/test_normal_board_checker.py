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

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_verticalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_diagonalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_otherDiagonalWin_win(self):
        board_checker = NormalBoardChecker()
        board = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.WIN
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_diagonalLoss_loss(self):
        board_checker = NormalBoardChecker()
        board = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = GameState.LOSS
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_ongoingL_none(self):
        board_checker = NormalBoardChecker()
        board = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

    def test_isWinOrLoss_twoRow_none(self):
        board_checker = NormalBoardChecker()
        board = [[2, 2, 0], [0, 1, 1], [0, 0, 0]]

        size_line_to_win = 3
        is_win_loss_or_ongoing = board_checker.win_or_loss(board)

        expected = None
        self.assertEqual(expected, is_win_loss_or_ongoing)

