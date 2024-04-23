import unittest
from src.tic_tac_toe.board.normal_board import NormalBoard


class TestNormalHumanPlayer(unittest.TestCase):
    def test_getBoard_call_generatesEmptyBoard(self):
        board_gen = NormalBoard()

        board = board_gen.get_board()

        expected_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(expected_board, board)
