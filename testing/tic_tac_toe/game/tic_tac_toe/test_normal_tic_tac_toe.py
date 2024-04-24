from unittest import TestCase
from src.tic_tac_toe.game.tic_tac_toe.normal_tic_tac_toe import NormalTicTacToe
from testing.tic_tac_toe.board.stub_normal_board import WinStubNormalBoard, LoseStubNormalBoard, DrawStubNormalBoard
from src.tic_tac_toe.data.game_state import GameState


class TestNormalTicTacToe(TestCase):
    def test_play_winningBoard_win(self):
        tic_tac_toe = NormalTicTacToe(board=WinStubNormalBoard())

        end_state = tic_tac_toe.play()

        self.assertEqual(GameState.WIN, end_state)

    def test_play_losingBoard_lose(self):
        tic_tac_toe = NormalTicTacToe(board=LoseStubNormalBoard())

        end_state = tic_tac_toe.play()

        self.assertEqual(GameState.LOSS, end_state)

    def test_play_drawingBoard_draw(self):
        tic_tac_toe = NormalTicTacToe(board=DrawStubNormalBoard())

        end_state = tic_tac_toe.play()

        self.assertEqual(GameState.LOSS, end_state)