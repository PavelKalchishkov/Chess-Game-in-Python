import copy
from abc import ABC, abstractmethod


from chess_project.board import c_board


class ChessPiece(ABC):
    white_turn = True

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

    @staticmethod
    def find_all_white_pieces():
        white_pieces = []
        for row in range(8):
            for col in range(8):
                if c_board.board[row][col] == ".":
                    pass
                elif c_board.board[row][col].color == "white":
                    white_pieces.append(c_board.board[row][col])

        return white_pieces

    @staticmethod
    def find_all_black_pieces():
        black_pieces = []
        for row in range(8):
            for col in range(8):
                if c_board.board[row][col] == ".":
                    pass
                elif c_board.board[row][col].color == "black":
                    black_pieces.append(c_board.board[row][col])

        return black_pieces

    @classmethod
    def get_white_attacked_squares(cls):
        attacked_squares = []
        for piece in cls.find_all_white_pieces():
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "P":
                attacked_squares.append((cur_row - 1, cur_col - 1))
                attacked_squares.append((cur_row - 1, cur_col + 1))
            else:
                valid_moves = piece.check_valid_moves()
                for move in valid_moves:
                    attacked_squares.append(move)

        return attacked_squares

    @classmethod
    def get_black_attacked_squares(cls):
        attacked_squares = []
        for piece in cls.find_all_black_pieces():
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "p":
                attacked_squares.append((cur_row + 1, cur_col + 1))
                attacked_squares.append((cur_row + 1, cur_col - 1))
            else:
                valid_moves = piece.check_valid_moves()
                for move in valid_moves:
                    attacked_squares.append(move)

        return attacked_squares

    @classmethod
    def check_if_white_in_check(cls, row, col):
        black_attacked_squares = cls.get_black_attacked_squares()
        if (row, col) in black_attacked_squares:
            return True
        else:
            return False

    @classmethod
    def check_if_black_in_check(cls, row, col):
        white_attacked_squares = cls.get_white_attacked_squares()
        if (row, col) in white_attacked_squares:
            return True
        else:
            return False

    @staticmethod
    def check_white_king_valid_moves(king_row, king_col):
        old_board = copy.deepcopy(c_board.board)
        king_moves = c_board.board[king_row][king_col].check_valid_moves()
        king_valid_moves = []

        if king_moves:
            for move in king_moves:
                old_piece = None
                row, col = move

                if c_board.board[row][col] != ".":
                    old_piece = c_board.board[row][col]

                c_board.board[king_row][king_col].update_coordinates(row, col)

                if not ChessPiece.check_if_white_in_check(row, col):
                    king_valid_moves.append(move)

                c_board.board[row][col].update_coordinates(king_row, king_col)
                if old_piece:
                    c_board.board[row][col] = old_piece
                c_board.board = old_board

        return king_valid_moves

    @staticmethod
    def check_if_white_pieces_can_stop_check(king_row, king_col):
        old_board = copy.deepcopy(c_board.board)
        pieces = ChessPiece.find_all_white_pieces()
        correct_moves = []

        for piece in pieces:
            if str(piece) == "K":
                pass
            else:
                piece_row, piece_col = piece.get_coordinates()
                for move in piece.check_valid_moves():
                    old_piece = None
                    row, col = move

                    if c_board.board[row][col] != ".":
                        old_piece = c_board.board[row][col]

                    c_board.board[piece_row][piece_col].update_coordinates(row, col)

                    if not ChessPiece.check_if_white_in_check(king_row, king_col):
                        correct_moves.append(move)

                    c_board.board[row][col].update_coordinates(piece_row, piece_col)
                    if old_piece:
                        c_board.board[row][col] = old_piece
                    c_board.board = old_board

        return correct_moves

    @staticmethod
    def check_white_checkmate(king_row, king_col):
        if ChessPiece.check_if_white_in_check(king_row, king_col):
            if not ChessPiece.check_white_king_valid_moves(king_row, king_col):
                if not ChessPiece.check_if_white_pieces_can_stop_check(king_row, king_col):
                    return print("Checkmate! Black wins!")

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
        legal_moves = self.check_valid_moves()

        if not legal_moves:
            print("This piece has no legal moves!")
            return False

        if (new_row, new_col) in legal_moves:
            self.update_coordinates(new_row, new_col)
            return True

        else:
            print("This move is not legal!")
            return False





