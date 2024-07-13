class Board:
    # the board is a matrix with string, '.' meaning the space is empty and everything else is a class instance,
    # represented in a string
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    # this is a function for printing the board on the console, it is not used in the UI version
    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col], end=" ")
            else:
                print()
        print()


# creating the game board
c_board = Board()


