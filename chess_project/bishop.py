from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class Bishop(ChessPiece):
    moves_available = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                       (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                       (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                       (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]

    # representing the bishop class as a string
    def __str__(self):
        if self.color == "white":
            return "B"
        elif self.color == "black":
            return "b"

    # the bishop checks the same way the rook does, but diagonally
    def check_valid_moves(self):
        self.valid_moves = []

        for r, c in Bishop.moves_available[0:7]:
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

        for r, c in Bishop.moves_available[7:14]:
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

        for r, c in Bishop.moves_available[14:21]:
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

        for r, c in Bishop.moves_available[21:28]:
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
