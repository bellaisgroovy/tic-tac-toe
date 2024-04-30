from src.tic_tac_toe.display.normal_display import NormalDisplay
from unittest import TestCase
from unittest.mock import call, patch


class TestNormalDisplay(TestCase):
    @patch('builtins.print')
    def test_display_normalBoard_prints(self, mocked_print):
        display = NormalDisplay()
        board = [[0, 2, 0], [0, 2, 1], [1, 2, 0], ]

        display.display(board)

        expected_calls = [call('|', end=''),
         call(' ', end='|'),
         call('O', end='|'),
         call(' ', end='|'),
         call(),
         call('|', end=''),
         call(' ', end='|'),
         call('O', end='|'),
         call('X', end='|'),
         call(),
         call('|', end=''),
         call('X', end='|'),
         call('O', end='|'),
         call(' ', end='|'),
         call()]
        self.assertEqual(expected_calls, mocked_print.mock_calls, )
