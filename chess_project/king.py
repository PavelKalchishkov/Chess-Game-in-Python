from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class King(ChessPiece):
    moves_available = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

    def __str__(self):
        if self.color == "white":
            return "K"
        elif self.color == "black":
            return "k"

    def check_for_check(self):
        pass

    def check_valid_moves(self):
        for r, c in King.moves_available:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))


