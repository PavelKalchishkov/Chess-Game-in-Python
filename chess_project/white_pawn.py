from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class WhitePawn(ChessPiece):
    moves_available = [(-2, 0), (-1, 0), (-1, -1), (-1, 1)]

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = "white"
        self.valid_moves = []
        self.squares_traveled = 0

    def __str__(self):
        return "P"

    def check_valid_moves(self):
        if self.check_range(self.row - 1, self.column) and self.check_range(self.row - 2, self.column):
            if self.squares_traveled == 0:
                if c_board.board[self.row - 1][self.column] == "." and c_board.board[self.row - 2][self.column]:
                    self.valid_moves.append(WhitePawn.moves_available[0])

        if self.check_range(self.row - 1, self.column):
            if c_board.board[self.row - 1][self.column] == ".":
                self.valid_moves.append(WhitePawn.moves_available[1])

        if self.check_range(self.row - 1, self.column - 1):
            try:
                if c_board.board[self.row - 1][self.column - 1].color == "black":
                    self.valid_moves.append(WhitePawn.moves_available[2])
            except AttributeError:
                pass

        if self.check_range(self.row - 1, self.column + 1):
            try:
                if c_board.board[self.row - 1][self.column + 1].color == "black":
                    self.valid_moves.append(WhitePawn.moves_available[3])
            except AttributeError:
                pass

        # TODO: add en passant check

    def move(self, new_position):
        self.check_valid_moves()

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

                if diff == -2:
                    self.squares_traveled += 1
                self.squares_traveled += 1

                if self.squares_traveled == 6:
                    print("Choose promotion: 1: Queen, 2: Knight, 3: Bishop, 4: Rook")
                    # promotion = int(input())
                    # TODO: finish when other classes are finished
                break
        else:
            return print("Invalid move")
        self.valid_moves = []



