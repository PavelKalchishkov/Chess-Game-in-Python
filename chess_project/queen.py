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

    def move(self, new_position):
        self.check_valid_moves()

        if not self.valid_moves:
            return print("Invalid move!")

        new_row = new_position[0]
        new_col = new_position[1]

        diff = new_row - self.row
        diff2 = new_col - self.column

        for r, c in self.valid_moves:
            if r == diff and c == diff2:
                c_board.board[self.row][self.column] = "."
                self.row = new_row
                self.column = new_col
                c_board.board[self.row][self.column] = self
                break
        else:
            return print("Invalid move")
        self.valid_moves = []





