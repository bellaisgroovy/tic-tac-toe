from unittest import TestCase
from unittest.mock import patch, call
from testing.tic_tac_toe.game.stub_game import StubWinGame, StubDrawGame, StubLoseGame, FakeWinLoseWin
from src.login_menu import LoginMenu
from testing.login.stub_login import StubLogin


class TestLoginMenu(TestCase):
    @patch('builtins.print')
    def test_play_StubWinLoggedOut_XWon(self, mocked_print):
        menu = LoginMenu(StubWinGame(), StubLogin())

        menu.play()

        expected_calls = [call('X won!')]
        self.assertEqual(expected_calls, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_play_StubWinLoggedIn_bella123Won(self, mocked_print):
        menu = LoginMenu(StubWinGame(), StubLogin())

        menu.login()
        menu.play()

        expected_calls = [call('bella123 won!')]
        self.assertEqual(expected_calls, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_play_StubDrawLoggedOut_Draw(self, mocked_print):
        menu = LoginMenu(StubDrawGame(), StubLogin())

        menu.play()

        expected_calls = [call('It was a draw.')]
        self.assertEqual(expected_calls, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_play_StubLoseLoggedOut_Loss(self, mocked_print):
        menu = LoginMenu(StubLoseGame(), StubLogin())

        menu.play()

        expected_calls = [call('O won!')]
        self.assertEqual(expected_calls, mocked_print.mock_calls)

    @patch('builtins.print')
    def test_play_fakeMultipleCalls_winLossWin(self, mocked_print):
        menu = LoginMenu(FakeWinLoseWin(), StubLogin)

        menu.play()
        menu.play()
        menu.play()

        expected_calls = [
            call('X won!'),
            call('O won!'),
            call('X won!'),
        ]
        self.assertEqual(expected_calls, mocked_print.mock_calls)


