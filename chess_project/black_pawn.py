from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board
from chess_project.queen import Queen


class BlackPawn(ChessPiece):
    moves_available = [(2, 0), (1, 0), (1, 1), (1, -1)]

    def __init__(self, row, column, color):
        super().__init__(row, column, color)
        self.squares_traveled = 0

    def __str__(self):
        return "p"

    def check_valid_moves(self):
        if self.check_range(self.row + 1, self.column) and self.check_range(self.row + 2, self.column):
            if self.squares_traveled == 0:
                if c_board.board[self.row + 1][self.column] == "." and c_board.board[self.row + 2][self.column] == ".":
                    self.valid_moves.append(BlackPawn.moves_available[0])

        if self.check_range(self.row + 1, self.column):
            if c_board.board[self.row + 1][self.column] == ".":
                self.valid_moves.append(BlackPawn.moves_available[1])

        if self.check_range(self.row + 1, self.column + 1):
            try:
                if ChessPiece.possible_black_enpassant:
                    if self.row + 1 == ChessPiece.possible_black_enpassant[0] and self.column + 1 == ChessPiece.possible_black_enpassant[1]:
                        self.valid_moves.append(BlackPawn.moves_available[2])
                if c_board.board[self.row + 1][self.column + 1].color == "white":
                    self.valid_moves.append(BlackPawn.moves_available[2])
            except AttributeError:
                pass

        if self.check_range(self.row + 1, self.column - 1):
            try:
                if ChessPiece.possible_black_enpassant:
                    if self.row + 1 == ChessPiece.possible_black_enpassant[0] and self.column - 1 == ChessPiece.possible_black_enpassant[1]:
                        self.valid_moves.append(BlackPawn.moves_available[3])
                if c_board.board[self.row + 1][self.column - 1].color == "white":
                    self.valid_moves.append(BlackPawn.moves_available[3])
            except AttributeError:
                pass

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
                if c_board.board[self.row][self.column] in ChessPiece.white_pieces:
                    ChessPiece.white_pieces.remove(c_board.board[self.row][self.column])
                elif c_board.board[self.row][self.column] in ChessPiece.black_pieces:
                    ChessPiece.black_pieces.remove(c_board.board[self.row][self.column])
                c_board.board[self.row][self.column] = self

                if diff == 2:
                    self.squares_traveled += 1
                    ChessPiece.possible_white_enpassant = (self.row - 1, self.column)
                self.squares_traveled += 1

                if ChessPiece.possible_black_enpassant:
                    if self.row == ChessPiece.possible_black_enpassant[0] and self.column == ChessPiece.possible_black_enpassant[1]:
                        c_board.board[self.row - 1][self.column] = "."

                if self.squares_traveled == 6:
                    c_board.board[self.row][self.column] = Queen(self.row, self.column, self.color)
                break
        else:
            return print("Invalid move")
        self.valid_moves = []



