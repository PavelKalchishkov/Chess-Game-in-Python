import copy
from abc import ABC, abstractmethod
from copy import deepcopy

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

    @staticmethod
    def check_if_white_in_check(row, column):
        attacked_squares = []

        for piece in ChessPiece.black_pieces:
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "p":
                attacked_squares.append((cur_row + 1, cur_col + 1))
                attacked_squares.append((cur_row + 1, cur_col - 1))
            else:
                valid_moves = piece.check_valid_moves()
                for move in valid_moves:
                    attacked_squares.append(move)

        if (row, column) in attacked_squares:
            return True
        else:
            return False

    @staticmethod
    def check_if_black_in_check(row, column):
        attacked_squares = []

        for piece in ChessPiece.white_pieces:
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "P":
                attacked_squares.append((cur_row - 1, cur_col - 1))
                attacked_squares.append((cur_row - 1, cur_col + 1))
            else:
                valid_moves = piece.check_valid_moves()
                if valid_moves:
                    for move in valid_moves:
                        attacked_squares.append(move)

        if (row, column) in attacked_squares:
            return True
        else:
            return False

    def updated_king_legal_moves(self, row, col, legal_moves):
        updated_valid_moves = []

        cur_row = row
        cur_col = col

        for move in legal_moves:
            new_row = move[0]
            new_col = move[1]

            old_board = copy.deepcopy(c_board.board)
            self.update_coordinates(new_row, new_col)

            if self.color == "white":
                if not ChessPiece.check_if_white_in_check(new_row, new_col):
                    updated_valid_moves.append(move)
                    self.update_coordinates(cur_row, cur_col)
                    c_board.board = old_board
                else:
                    self.update_coordinates(cur_row, cur_col)
                    c_board.board = old_board

            elif self.color == "black":
                if not ChessPiece.check_if_black_in_check(new_row, new_col):
                    updated_valid_moves.append(move)
                    self.update_coordinates(cur_row, cur_col)
                    c_board.board = old_board
                else:
                    self.update_coordinates(cur_row, cur_col)
                    c_board.board = old_board

        return updated_valid_moves

    @abstractmethod
    def check_valid_moves(self):
        pass

    def move(self, new_row, new_col):

        legal_moves = self.check_valid_moves()

        if not legal_moves:
            print("This piece has no legal moves!")
            return False

        if str(self) == "k" or str(self) == "K":
            legal_moves = self.updated_king_legal_moves(self.row, self.column, legal_moves)
            if not legal_moves:
                print("This piece has no legal moves!")
                return False

        if (new_row, new_col) in legal_moves:

            if c_board.board[new_row][new_col] == ".":
                pass
            elif c_board.board[new_row][new_col] in ChessPiece.white_pieces:
                ChessPiece.white_pieces.remove(c_board.board[new_row][new_col])
            elif c_board.board[new_row][new_col] in ChessPiece.black_pieces:
                ChessPiece.black_pieces.remove(c_board.board[new_row][new_col])

            self.update_coordinates(new_row, new_col)
            print(self.get_coordinates())

        else:
            print("This move is not legal!")
            return False

        return True



