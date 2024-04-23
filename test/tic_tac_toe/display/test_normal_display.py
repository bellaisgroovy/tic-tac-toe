from src.tic_tac_toe.display.normal_display import NormalDisplay
from unittest import TestCase
from unittest.mock import call, patch


class TestNormalDisplay(TestCase):
    @patch('builtins.print')
    def test_display_normalBoard_prints(self, mocked_print):
        display = NormalDisplay()
        board = [[1, 2, 0], [0, 2, 1], [0, 2, 0]]

        display.display(board)

        left = call('|', end='')
        space = call(' ', end='|')
        x = call('X', end='|')
        o = call('O', end='|')
        end = call()
        expected_calls = [left, x, o, space, end, left, space, o, x, end, left, space, o, space, end]
        self.assertEqual(expected_calls, mocked_print.mock_calls, )
