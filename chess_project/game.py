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

    def take_move(self, start_position, end_position):
        start_row = ChessPiece.row_names[start_position[1]]
        start_col = ChessPiece.column_names[start_position[0]]
        try:
            end_row = ChessPiece.row_names[end_position[1]]
            end_col = ChessPiece.column_names[end_position[0]]
        except KeyError:
            return print("Invalid move")

        try:
            if self.white_turn and c_board.board[start_row][start_col].color == "white":
                c_board.board[start_row][start_col].move((end_row, end_col))
                self.white_turn = False
            elif not self.white_turn and c_board.board[start_row][start_col].color == "black":
                c_board.board[start_row][start_col].move((end_row, end_col))
                self.white_turn = True
            else:
                return print("Invalid move")
        except AttributeError:
            return print("Invalid move")


for row in range(8):
    for col in range(8):
        if c_board.board[row][col] == "p":
            c_board.board[row][col] = BlackPawn(row, col, "black")
        elif c_board.board[row][col] == "P":
            c_board.board[row][col] = WhitePawn(row, col, "white")
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
        elif c_board.board[row][col] == "K":
            c_board.board[row][col] = King(row, col, "white")


game1 = Game()


game1.take_move("a2", "a4")
c_board.print_board()

game1.take_move("a4", "a5")
c_board.print_board()

