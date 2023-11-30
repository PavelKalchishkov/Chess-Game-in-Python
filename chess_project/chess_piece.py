from chess_project.board import c_board


class ChessPiece:
    row_names = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    column_names = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

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

    def check_valid_moves(self):
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
                c_board.board[self.row][self.column] = self
                break
        else:
            return print("Invalid move")
        self.valid_moves = []



