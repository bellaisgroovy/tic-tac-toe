from src.tic_tac_toe.game.tic_tac_toe.tic_tac_toe import TicTacToe
from src.tic_tac_toe.player.normal_human_player import NormalHumanPlayer
from src.tic_tac_toe.board.normal_board import NormalBoard
from src.tic_tac_toe.board_checker.normal_board_checker import NormalBoardChecker
from src.tic_tac_toe.display.normal_display import NormalDisplay


class NormalTicTacToe(TicTacToe):
    def __init__(
            self,
            no_players=2,
            size_line_to_win=3,
            player=NormalHumanPlayer(),
            board=NormalBoard(),
            board_checker=NormalBoardChecker(),
            display=NormalDisplay()
    ):
        super().__init__(no_players,size_line_to_win, player, board, board_checker, display)
