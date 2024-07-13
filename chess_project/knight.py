from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class Knight(ChessPiece):
    moves_available = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    # representing the knight as a string
    def __str__(self):
        if self.color == "white":
            return "N"
        elif self.color == "black":
            return "n"

    # we check the if the knight has legal moves in those specific location, since the knight jumps over the pieces,
    # there is no need to check if the path is blocked
    def check_valid_moves(self):
        self.valid_moves = []
        for r, c in Knight.moves_available:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))

        return self.valid_moves




