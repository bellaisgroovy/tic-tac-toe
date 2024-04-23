import unittest
from unittest.mock import patch
from src.tic_tac_toe.player.normal_human_player import NormalHumanPlayer


class TestNormalHumanPlayer(unittest.TestCase):
    def test_move_validInput_returnDict(self):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        with patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', return_value="7"):
            move_dict = player.move(board)

        expected_dict = {'x': 0, 'y': 0}
        self.assertEqual(move_dict, expected_dict)

    def test_move_wrongTypeInput_askAgain(self):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        with patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["pizza", "5"]):
            move_dict = player.move(board)

        expected_dict = {'x': 1, 'y': 1}
        self.assertEqual(move_dict, expected_dict)

    def test_move_highInput_askAgain(self):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        with patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["10", "1"]):
            move_dict = player.move(board)

        expected_dict = {'x': 0, 'y': 2}
        self.assertEqual(move_dict, expected_dict)

    def test_move_lowInput_askAgain(self):
        player = NormalHumanPlayer()
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        with patch('src.tic_tac_toe.player.normal_human_player.NormalHumanPlayer.input_wrap', side_effect=["0", "3"]):
            move_dict = player.move(board)

        expected_dict = {'x': 2, 'y': 2}
        self.assertEqual(move_dict, expected_dict)