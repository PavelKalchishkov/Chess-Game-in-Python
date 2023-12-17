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
        moves_from_rook = []
        moves_from_bishop = []

        if moves_from_rook:
            for move in Rook.check_valid_moves(self):
                moves_from_rook.append(move)

        if moves_from_bishop:
            for move in Bishop.check_valid_moves(self):
                moves_from_bishop.append(move)

        self.valid_moves = moves_from_rook + moves_from_bishop

        return self.valid_moves






