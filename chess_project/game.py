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
        self.game_over = False
        self.white_turn = True
        self.white_king_coordinates = []
        self.black_king_coordinates = []
        self.counter = 0
        self.board_state = {}

    def add_board_state_to_dictionary(self):
        board_str = ""
        if self.white_turn:
            board_str += "W"
        else:
            board_str += "B"

        for r in range(8):
            for c in range(8):
                board_str += str(c_board.board[r][c])

        if board_str not in self.board_state:
            self.board_state[board_str] = 0
        self.board_state[board_str] += 1

    def check_for_threefold_repetition_draw(self):
        for key, value in self.board_state.items():
            if value == 3:
                print()
                print("Draw by threefold repetition!")
                self.game_over = True

    @staticmethod
    def check_count_of_pieces_on_board():
        count_pieces = len(ChessPiece.find_all_white_pieces()) + len(ChessPiece.find_all_black_pieces())
        return count_pieces

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

    @staticmethod
    def check_if_rook(start_row, start_col):
        if str(c_board.board[start_row][start_col]) == "r" or str(c_board.board[start_row][start_col]) == "R":
            return True
        else:
            return False

    def take_move(self, start_position, new_position):
        old_piece = None
        count_pieces = Game.check_count_of_pieces_on_board()

        if self.game_over:
            print('Game is over.')
            return 6

        try:
            start_row = ChessPiece.row_names[start_position[1]]
            start_col = ChessPiece.column_names[start_position[0]]

            new_row = ChessPiece.row_names[new_position[1]]
            new_col = ChessPiece.column_names[new_position[0]]
        except (KeyError, IndexError):
            print("Invalid square!")
            return 4

        if c_board.board[start_row][start_col] == ".":
            print("Invalid move - starting square empty!")
            return 4

        if c_board.board[new_row][new_col] != ".":
            old_piece = c_board.board[new_row][new_col]

        if self.white_turn and c_board.board[start_row][start_col].color == "white":
            old_board = copy.deepcopy(c_board.board)
            if c_board.board[start_row][start_col].move(new_row, new_col):

                if self.check_if_king(new_row, new_col):
                    c_board.board[new_row][new_col].has_moved = True
                    self.white_king_coordinates = [new_row, new_col]

                if self.check_if_rook(new_row, new_col):
                    c_board.board[new_row][new_col].has_moved = True

                white_king_row, white_king_col = self.white_king_coordinates
                if ChessPiece.check_if_white_in_check(white_king_row, white_king_col):
                    if self.check_if_king(new_row, new_col):
                        self.white_king_coordinates = [start_row, start_col]
                    c_board.board[new_row][new_col].update_coordinates(start_row, start_col)
                    if old_piece:
                        c_board.board[new_row][new_col] = old_piece
                    c_board.board = old_board
                    print("White king is in check there, this move is illegal!")
                    return 4

                if self.check_if_pawn(new_row, new_col):
                    c_board.board[new_row][new_col].update_pawn_attributes(start_row, start_col, new_row, new_col)
                    self.counter = 0

                if count_pieces != Game.check_count_of_pieces_on_board():
                    self.counter = 0

                self.add_board_state_to_dictionary()
                self.check_for_threefold_repetition_draw()

                self.white_turn = not self.white_turn
                ChessPiece.possible_white_enpassant = ()
                self.counter += 1

                print('Successful move')
                return 1

            black_king_row, black_king_col = self.black_king_coordinates
            if ChessPiece.check_if_black_in_check(black_king_row, black_king_col):
                if ChessPiece.check_black_checkmate(black_king_row, black_king_col):
                    self.game_over = True
                    print("Checkmate! White wins!")
                    return 2
                else:
                    print("Black is in check!")
                    return 5

            if ChessPiece.check_black_stalemate():
                self.game_over = True
                print("Stalemate! Black has no legal moves!")
                return 3

            if ChessPiece.check_insufficient_material():
                self.game_over = True
                print("Draw by insufficient material!")
                return 3

            if self.counter == 100:
                self.game_over = True
                print("Draw by 50 move rule!")
                return 3

            print('Successful move')
            return 1

        elif not self.white_turn and c_board.board[start_row][start_col].color == "black":
            old_board = copy.deepcopy(c_board.board)
            if c_board.board[start_row][start_col].move(new_row, new_col):

                if self.check_if_king(new_row, new_col):
                    c_board.board[new_row][new_col].has_moved = True
                    self.black_king_coordinates = [new_row, new_col]

                if self.check_if_rook(new_row, new_col):
                    c_board.board[new_row][new_col].has_moved = True

                black_king_row, black_king_col = self.black_king_coordinates
                if ChessPiece.check_if_black_in_check(black_king_row, black_king_col):
                    if self.check_if_king(new_row, new_col):
                        self.black_king_coordinates = [start_row, start_col]
                    c_board.board[new_row][new_col].update_coordinates(start_row, start_col)
                    if old_piece:
                        c_board.board[new_row][new_col] = old_piece
                    c_board.board = old_board
                    print("Black king is in check there, this move is illegal!")
                    return 4

                if self.check_if_pawn(new_row, new_col):
                    c_board.board[new_row][new_col].update_pawn_attributes(start_row, start_col, new_row, new_col)
                    self.counter = 0

                if count_pieces != Game.check_count_of_pieces_on_board():
                    self.counter = 0

                self.add_board_state_to_dictionary()
                self.check_for_threefold_repetition_draw()

                self.white_turn = not self.white_turn
                ChessPiece.possible_black_enpassant = ()
                self.counter += 1

            white_king_row, white_king_col = self.white_king_coordinates
            if ChessPiece.check_if_white_in_check(white_king_row, white_king_col):
                if ChessPiece.check_white_checkmate(white_king_row, white_king_col):
                    self.game_over = True
                    print("Checkmate! Black wins!")
                    return 7
                else:
                    print("White is in check!")
                    return 5

            if ChessPiece.check_white_stalemate():
                self.game_over = True
                print("Stalemate! White has no legal moves!")
                return 3

            if ChessPiece.check_insufficient_material():
                self.game_over = True
                print("Draw by insufficient material!")
                return 3

            if self.counter == 100:
                self.game_over = True
                print("Draw by 50 move rule!")
                return 3

            print('Successful move')
            return 1

        else:
            print(f"Invalid move, it's {'white' if self.white_turn else 'black'}'s turn!")
            return 4


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

# c_board.print_board()
# while not game1.game_over:
#     game1.take_move(input("Starting square: "), input("End square: "))
#     print()
#     c_board.print_board()
