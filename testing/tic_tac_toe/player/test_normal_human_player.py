import unittest
from unittest.mock import patch
from src.tic_tac_toe.player.normal_human_player import NormalHumanPlayer


class TestNormalHumanPlayer(unittest.TestCase):
    @patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', return_value="7")
    def test_move_validInput_returnDict(self, mock_input):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        move_dict = player.move(board)

        expected_dict = {'x': 0, 'y': 0}
        self.assertEqual(move_dict, expected_dict)

    @patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["pizza", "5"])
    def test_move_wrongTypeInput_askAgain(self, mock_input):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        move_dict = player.move(board)

        expected_dict = {'x': 1, 'y': 1}
        self.assertEqual(move_dict, expected_dict)

    @patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["10", "1"])
    def test_move_highInput_askAgain(self, mock_input):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        move_dict = player.move(board)

        expected_dict = {'x': 2, 'y': 0}
        self.assertEqual(move_dict, expected_dict)

    @patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["0", "3"])
    def test_move_lowInput_askAgain(self, mock_input):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        move_dict = player.move(board)

        expected_dict = {'x': 2, 'y': 2}
        self.assertEqual(move_dict, expected_dict)