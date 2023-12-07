from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class King(ChessPiece):
    moves_available = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

    def __str__(self):
        if self.color == "white":
            return "K"
        elif self.color == "black":
            return "k"

    def check_attacked_squares(self):
        attacked_squares = []
        if self.color == "white":
            for piece in ChessPiece.black_pieces:
                coordinates = piece.get_coordinates()
                cur_row = coordinates[0]
                cur_column = coordinates[1]
                if str(piece) == "p":
                    attacked_squares.append((cur_row + 1, cur_column + 1))
                    attacked_squares.append((cur_row + 1, cur_column - 1))
                elif str(piece) == "k":
                    for move in King.moves_available:
                        attacked_squares.append((cur_row + move[0], cur_column + move[1]))
                else:
                    piece.check_valid_moves()
                    if piece.valid_moves:
                        for move in piece.valid_moves:
                            attacked_squares.append((cur_row + move[0], cur_column + move[1]))

        elif self.color == "black":
            for piece in ChessPiece.white_pieces:
                coordinates = piece.get_coordinates()
                cur_row = coordinates[0]
                cur_column = coordinates[1]
                if str(piece) == "P":
                    attacked_squares.append((cur_row - 1, cur_column - 1))
                    attacked_squares.append((cur_row - 1, cur_column + 1))
                elif str(piece) == "K":
                    for move in King.moves_available:
                        attacked_squares.append((cur_row + move[0], cur_column + move[1]))
                else:
                    piece.check_valid_moves()
                    if piece.valid_moves:
                        for move in piece.valid_moves:
                            attacked_squares.append((cur_row + move[0], cur_column + move[1]))

        valid_attacked_squares = []
        for square in attacked_squares:
            if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                valid_attacked_squares.append(square)
        return list(set(valid_attacked_squares))

    def check_valid_moves(self):
        for r, c in King.moves_available:
            if self.check_range(self.row + r, self.column + c):
                if (c_board.board[self.row + r][self.column + c] == "."
                        or c_board.board[self.row + r][self.column + c].color != self.color):
                    old_row, old_col = self.row, self.column
                    new_row, new_col = self.row + r, self.column + c
                    c_board.board[old_row][old_col] = "."
                    c_board.board[new_row][new_col] = self

                    for attacked_square in self.check_attacked_squares():
                        attacked_row = attacked_square[0]
                        attacked_col = attacked_square[1]

                        if new_row == attacked_row and new_col == attacked_col:
                            break
                    else:
                        self.valid_moves.append((r, c))

                    c_board.board[new_row][new_col] = "."
                    c_board.board[old_row][old_col] = self


