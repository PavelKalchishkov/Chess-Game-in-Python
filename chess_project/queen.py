from chess_project.rook import Rook
from chess_project.bishop import Bishop


class Queen(Rook, Bishop):
    moves_available = Rook.moves_available + Bishop.moves_available

    def __str__(self):
        if self.color == "white":
            return "Q"
        elif self.color == "black":
            return "q"

    def check_valid_moves(self):
        self.valid_moves = []

        for move in Rook.check_valid_moves(self):
            self.valid_moves.append(move)
        for move in Bishop.check_valid_moves(self):
            self.valid_moves.append(move)

        return self.valid_moves






