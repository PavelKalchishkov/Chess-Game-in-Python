from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class Rook(ChessPiece):
    moves_available = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                       (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                       (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]

    def __str__(self):
        if self.color == "white":
            return "R"
        elif self.color == "black":
            return "r"

    def check_valid_moves(self):
        self.valid_moves = []

        for r, c in Rook.moves_available[0:7]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[7:14]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[14:21]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[21:28]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((self.row + r, self.column + c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((self.row + r, self.column + c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        return self.valid_moves
