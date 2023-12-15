from abc import ABC, abstractmethod

from chess_project.board import c_board


class ChessPiece(ABC):
    white_turn = True

    white_pieces = []
    black_pieces = []

    row_names = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    column_names = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    possible_white_enpassant = ()
    possible_black_enpassant = ()

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.valid_moves = []

    @staticmethod
    def check_range(r, c):
        if r > 7 or r < 0 or c > 7 or c < 0:
            return False
        else:
            return True

    def get_coordinates(self):
        return self.row, self.column

    def update_coordinates(self, updated_row, updated_column):
        c_board.board[self.row][self.column] = "."
        self.row = updated_row
        self.column = updated_column
        c_board.board[self.row][self.column] = self

    @abstractmethod
    def check_valid_moves(self):
        pass

    def move(self, new_row, new_col):

        if not self.check_valid_moves():
            print("This piece has no legal moves!")
            return False

        if (new_row, new_col) in self.check_valid_moves():

            if c_board.board[new_row][new_col] == ".":
                pass
            elif c_board.board[new_row][new_col] in ChessPiece.white_pieces:
                ChessPiece.white_pieces.remove(c_board.board[new_row][new_col])
            elif c_board.board[new_row][new_col] in ChessPiece.black_pieces:
                ChessPiece.black_pieces.remove(c_board.board[new_row][new_col])

            self.update_coordinates(new_row, new_col)

        else:
            print("This move is not legal!")
            return False

        return True



