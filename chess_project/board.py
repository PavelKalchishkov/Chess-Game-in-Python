class Board:
    def __init__(self):
        self.board = [
            ["r", "p", "b", "q", "k", "b", "k", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "P", "B", "Q", "K", "B", "N", "R"]
        ]

    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col], end=" ")
            else:
                print()
        print()


c_board = Board()


