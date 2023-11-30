from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class Knight(ChessPiece):
    moves_available = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    def __str__(self):
        if self.color == "white":
            return "N"
        elif self.color == "black":
            return "n"

    def check_valid_moves(self):
        for r, c in Knight.moves_available:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))




