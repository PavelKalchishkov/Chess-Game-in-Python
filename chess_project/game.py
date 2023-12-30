import copy

from chess_project.chess_piece import ChessPiece
from chess_project.pawn import Pawn
from chess_project.rook import Rook
from chess_project.bishop import Bishop
from chess_project.knight import Knight
from chess_project.queen import Queen
from chess_project.king import King
from chess_project.board import c_board


class Game:
    def __init__(self):
        self.white_turn = True
        self.white_king_coordinates = []
        self.black_king_coordinates = []

    @staticmethod
    def check_if_pawn(start_row, start_col):
        if str(c_board.board[start_row][start_col]) == "p" or str(c_board.board[start_row][start_col]) == "P":
            return True
        else:
            return False

    @staticmethod
    def check_if_king(start_row, start_col):
        if str(c_board.board[start_row][start_col]) == "k" or str(c_board.board[start_row][start_col]) == "K":
            return True
        else:
            return False

    def take_move(self, start_position, new_position):
        old_piece = None
        try:
            start_row = ChessPiece.row_names[start_position[1]]
            start_col = ChessPiece.column_names[start_position[0]]

            new_row = ChessPiece.row_names[new_position[1]]
            new_col = ChessPiece.column_names[new_position[0]]
        except KeyError:
            return print("Invalid square!")

        if c_board.board[start_row][start_col] == ".":
            return print("Invalid move - starting square empty!")

        if c_board.board[new_row][new_col] != ".":
            old_piece = c_board.board[new_row][new_col]

        if self.white_turn and c_board.board[start_row][start_col].color == "white":
            old_board = copy.deepcopy(c_board.board)
            if c_board.board[start_row][start_col].move(new_row, new_col):

                if self.check_if_king(new_row, new_col):
                    self.white_king_coordinates = [new_row, new_col]

                white_king_row, white_king_col = self.white_king_coordinates
                if ChessPiece.check_if_white_in_check(white_king_row, white_king_col):
                    if self.check_if_king(new_row, new_col):
                        self.white_king_coordinates = [start_row, start_col]
                    c_board.board[new_row][new_col].update_coordinates(start_row, start_col)
                    if old_piece:
                        c_board.board[new_row][new_col] = old_piece
                    c_board.board = old_board
                    return print("White king is in check, this move is illegal!")

                if self.check_if_pawn(new_row, new_col):
                    c_board.board[new_row][new_col].update_pawn_attributes(start_row, start_col, new_row, new_col)
                self.white_turn = not self.white_turn
                ChessPiece.possible_white_enpassant = ()

            black_king_row, black_king_col = self.black_king_coordinates
            if ChessPiece.check_if_black_in_check(black_king_row, black_king_col):
                print("Black is in check!")

        elif not self.white_turn and c_board.board[start_row][start_col].color == "black":
            old_board = copy.deepcopy(c_board.board)
            if c_board.board[start_row][start_col].move(new_row, new_col):

                if self.check_if_king(new_row, new_col):
                    self.black_king_coordinates = [new_row, new_col]

                black_king_row, black_king_col = self.black_king_coordinates
                if ChessPiece.check_if_black_in_check(black_king_row, black_king_col):
                    if self.check_if_king(new_row, new_col):
                        self.black_king_coordinates = [start_row, start_col]
                    c_board.board[new_row][new_col].update_coordinates(start_row, start_col)
                    if old_piece:
                        c_board.board[new_row][new_col] = old_piece
                    c_board.board = old_board
                    return print("Black king is in check, this move is illegal!")

                if self.check_if_pawn(new_row, new_col):
                    c_board.board[new_row][new_col].update_pawn_attributes(start_row, start_col, new_row, new_col)
                self.white_turn = not self.white_turn
                ChessPiece.possible_black_enpassant = ()

            white_king_row, white_king_col = self.white_king_coordinates
            if ChessPiece.check_if_white_in_check(white_king_row, white_king_col):
                print("White is in check!")

        else:
            return print(f"Invalid move, it's {'white' if self.white_turn else 'black'}'s turn!")


game1 = Game()

for row in range(8):
    for col in range(8):
        if c_board.board[row][col] == "p":
            c_board.board[row][col] = Pawn(row, col, "black")
        elif c_board.board[row][col] == "P":
            c_board.board[row][col] = Pawn(row, col, "white")
        elif c_board.board[row][col] == "r":
            c_board.board[row][col] = Rook(row, col, "black")
        elif c_board.board[row][col] == "R":
            c_board.board[row][col] = Rook(row, col, "white")
        elif c_board.board[row][col] == "b":
            c_board.board[row][col] = Bishop(row, col, "black")
        elif c_board.board[row][col] == "B":
            c_board.board[row][col] = Bishop(row, col, "white")
        elif c_board.board[row][col] == "n":
            c_board.board[row][col] = Knight(row, col, "black")
        elif c_board.board[row][col] == "N":
            c_board.board[row][col] = Knight(row, col, "white")
        elif c_board.board[row][col] == "q":
            c_board.board[row][col] = Queen(row, col, "black")
        elif c_board.board[row][col] == "Q":
            c_board.board[row][col] = Queen(row, col, "white")
        elif c_board.board[row][col] == "k":
            c_board.board[row][col] = King(row, col, "black")
            game1.black_king_coordinates = [row, col]
        elif c_board.board[row][col] == "K":
            c_board.board[row][col] = King(row, col, "white")
            game1.white_king_coordinates = [row, col]

c_board.print_board()

game1.take_move("h8", "h7")
c_board.print_board()

game1.take_move("g5", "g6")
c_board.print_board()

game1.take_move("h7", "g6")
c_board.print_board()

game1.take_move("h7", "h8")
c_board.print_board()

game1.take_move("g6", "g7")
c_board.print_board()

white_king_row, white_king_col = game1.white_king_coordinates
ChessPiece.check_white_checkmate(white_king_row, white_king_col)







