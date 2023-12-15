from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board
from chess_project.queen import Queen


class Pawn(ChessPiece):
    white_pawn_moves_available = [(-2, 0), (-1, 0), (-1, -1), (-1, 1)]
    black_pawn_moves_available = [(2, 0), (1, 0), (1, 1), (1, -1)]

    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.squares_traveled = 0

    def __str__(self):
        if self.color == "white":
            return "P"
        elif self.color == "black":
            return "p"

    def update_pawn_attributes(self, start_row, start_col, new_row, new_col):
        pawn_row_move = new_row - start_row
        pawn_col_move = new_col - start_col

        if self.color == "white":
            if pawn_row_move == -2:
                self.squares_traveled += 1
                ChessPiece.possible_black_enpassant = (self.row + 1, self.column)

            self.squares_traveled += 1

            if ChessPiece.possible_white_enpassant:
                if self.row == ChessPiece.possible_white_enpassant[0] and self.column == ChessPiece.possible_white_enpassant[1]:
                    ChessPiece.black_pieces.remove(c_board.board[self.row + 1][self.column])
                    c_board.board[self.row + 1][self.column] = "."

            if self.squares_traveled == 6:
                c_board.board[self.row][self.column] = Queen(self.row, self.column, self.color)

        elif self.color == "black":
            if pawn_row_move == 2:
                self.squares_traveled += 1
                ChessPiece.possible_white_enpassant = (self.row - 1, self.column)

            self.squares_traveled += 1

            if ChessPiece.possible_black_enpassant:
                if self.row == ChessPiece.possible_black_enpassant[0] and self.column == ChessPiece.possible_black_enpassant[1]:
                    ChessPiece.white_pieces.remove(c_board.board[self.row - 1][self.column])
                    c_board.board[self.row - 1][self.column] = "."

            if self.squares_traveled == 6:
                c_board.board[self.row][self.column] = Queen(self.row, self.column, self.color)

    def check_valid_moves(self):
        self.valid_moves = []

        if self.color == "white":

            if self.squares_traveled == 0:
                if c_board.board[self.row - 1][self.column] == "." and c_board.board[self.row - 2][self.column] == ".":
                    self.valid_moves.append((self.row - 2, self.column))

            if c_board.board[self.row - 1][self.column] == ".":
                self.valid_moves.append((self.row - 1, self.column))

            if self.check_range(self.row - 1, self.column - 1):
                if ChessPiece.possible_white_enpassant:
                    if (self.row - 1) == ChessPiece.possible_white_enpassant[0] and (self.column - 1) == ChessPiece.possible_white_enpassant[1]:
                        self.valid_moves.append((self.row - 1, self.column - 1))
                elif c_board.board[self.row - 1][self.column - 1] == ".":
                    pass
                elif c_board.board[self.row - 1][self.column - 1].color == "black":
                    self.valid_moves.append((self.row - 1, self.column - 1))

            if self.check_range(self.row - 1, self.column + 1):
                if ChessPiece.possible_white_enpassant:
                    if (self.row - 1) == ChessPiece.possible_white_enpassant[0] and (self.column + 1) == ChessPiece.possible_white_enpassant[1]:
                        self.valid_moves.append((self.row - 1, self.column + 1))
                elif c_board.board[self.row - 1][self.column + 1] == ".":
                    pass
                elif c_board.board[self.row - 1][self.column + 1].color == "black":
                    self.valid_moves.append((self.row - 1, self.column + 1))

        elif self.color == "black":

            if self.squares_traveled == 0:
                if c_board.board[self.row + 1][self.column] == "." and c_board.board[self.row + 2][self.column] == ".":
                    self.valid_moves.append((self.row + 2, self.column))

            if c_board.board[self.row + 1][self.column] == ".":
                self.valid_moves.append((self.row + 1, self.column))

            if self.check_range(self.row + 1, self.column + 1):
                if ChessPiece.possible_black_enpassant:
                    if (self.row + 1) == ChessPiece.possible_black_enpassant[0] and (self.column + 1) == ChessPiece.possible_black_enpassant[1]:
                        self.valid_moves.append((self.row + 1, self.column + 1))
                elif c_board.board[self.row + 1][self.column + 1] == ".":
                    pass
                elif c_board.board[self.row + 1][self.column + 1].color == "black":
                    self.valid_moves.append((self.row + 1, self.column + 1))

            if self.check_range(self.row + 1, self.column - 1):
                if ChessPiece.possible_black_enpassant:
                    if (self.row + 1) == ChessPiece.possible_black_enpassant[0] and (self.column - 1) == ChessPiece.possible_black_enpassant[1]:
                        self.valid_moves.append((self.row + 1, self.column - 1))
                elif c_board.board[self.row + 1][self.column - 1] == ".":
                    pass
                elif c_board.board[self.row + 1][self.column - 1].color == "black":
                    self.valid_moves.append((self.row + 1, self.column - 1))

        return self.valid_moves




