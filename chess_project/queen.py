from chess_project.chess_piece import ChessPiece
from chess_project.rook import Rook
from chess_project.bishop import Bishop
from chess_project.board import c_board


class Queen(Rook, Bishop):
    moves_available = Rook.moves_available + Bishop.moves_available

    def __str__(self):
        if self.color == "white":
            return "Q"
        elif self.color == "black":
            return "q"

    def check_valid_moves(self):
        Rook.check_valid_moves(self)
        Bishop.check_valid_moves(self)






