from chess_project.chess_piece import ChessPiece
from chess_project.white_pawn import WhitePawn
from chess_project.black_pawn import BlackPawn
from chess_project.rook import Rook
from chess_project.bishop import Bishop
from chess_project.knight import Knight
from chess_project.queen import Queen
from chess_project.king import King
from chess_project.board import c_board


class Game:

    def __init__(self):
        self.white_turn = True

    def check_for_checks(self):
        is_in_check = False
        if self.white_turn:
            for piece in ChessPiece.white_pieces:
                if str(piece) == "K":
                    king_row, king_col = piece.get_coordinates()
                    for square in piece.check_attacked_squares():
                        attacked_row = square[0]
                        attacked_col = square[1]
                        if attacked_row == king_row and attacked_col == king_col:
                            is_in_check = True
        elif not self.white_turn:
            for piece in ChessPiece.black_pieces:
                if str(piece) == "k":
                    king_row, king_col = piece.get_coordinates()
                    for square in piece.check_attacked_squares():
                        attacked_row = square[0]
                        attacked_col = square[1]
                        if attacked_row == king_row and attacked_col == king_col:
                            is_in_check = True
        return is_in_check

    def take_move(self, start_position, end_position):
        try:
            start_row = ChessPiece.row_names[start_position[1]]
            start_col = ChessPiece.column_names[start_position[0]]

            end_row = ChessPiece.row_names[end_position[1]]
            end_col = ChessPiece.column_names[end_position[0]]
        except KeyError:
            return print("Invalid move")

        if self.check_for_checks():
            if self.white_turn and str(c_board.board[start_row][start_col]) != "K":
                return print("Invalid move, move the king!")

            elif not self.white_turn and str(c_board.board[start_row][start_col]) != "k":
                return print("Invalid move, move the king!")

        if c_board.board[start_row][start_col] == ".":
            return print("Invalid move!")
        if self.white_turn and c_board.board[start_row][start_col].color == "white":
            if c_board.board[start_row][start_col].move((end_row, end_col)):
                self.white_turn = not self.white_turn
                ChessPiece.possible_white_enpassant = ()
        elif not self.white_turn and c_board.board[start_row][start_col].color == "black":
            if c_board.board[start_row][start_col].move((end_row, end_col)):
                self.white_turn = not self.white_turn
                ChessPiece.possible_black_enpassant = ()
        else:
            return print("Invalid move!")


for row in range(8):
    for col in range(8):
        if c_board.board[row][col] == "p":
            c_board.board[row][col] = BlackPawn(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "P":
            c_board.board[row][col] = WhitePawn(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "r":
            c_board.board[row][col] = Rook(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "R":
            c_board.board[row][col] = Rook(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "b":
            c_board.board[row][col] = Bishop(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "B":
            c_board.board[row][col] = Bishop(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "n":
            c_board.board[row][col] = Knight(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "N":
            c_board.board[row][col] = Knight(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "q":
            c_board.board[row][col] = Queen(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "Q":
            c_board.board[row][col] = Queen(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "k":
            c_board.board[row][col] = King(row, col, "black")
            ChessPiece.black_pieces.append(c_board.board[row][col])
        elif c_board.board[row][col] == "K":
            c_board.board[row][col] = King(row, col, "white")
            ChessPiece.white_pieces.append(c_board.board[row][col])

game1 = Game()

c_board.print_board()

game1.take_move("b1", "h1")
c_board.print_board()

game1.take_move("h8", "h7")
c_board.print_board()

game1.take_move("h8", "g7")
c_board.print_board()

game1.take_move("h1", "h2")
c_board.print_board()

game1.take_move("g8", "a8")
c_board.print_board()

game1.take_move("a1", "b2")
c_board.print_board()

game1.take_move("a1", "b1")
c_board.print_board()