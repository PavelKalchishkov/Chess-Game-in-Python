from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class King(ChessPiece):
    moves_available = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.has_moved = False

    # representing the king as a string
    def __str__(self):
        if self.color == "white":
            return "K"
        elif self.color == "black":
            return "k"

    # we check the squares around the king, if they are empty or with enemy figures, we can move there
    def check_valid_moves(self):
        self.valid_moves = []

        for r, c in King.moves_available:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))

        return self.valid_moves




