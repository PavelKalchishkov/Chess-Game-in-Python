from chess_project.board import c_board
from chess_project.game import game1
import pygame

pygame.init()

board_size = (600, 600)
screen = pygame.display.set_mode(board_size)
pygame.display.set_caption('Chess Board')

board_image = pygame.image.load('images/board.png')
board_image = pygame.transform.scale(board_image, board_size)

piece_images = {
    'P': 'images/white_pawn.png',
    'N': 'images/white_knight.png',
    'B': 'images/white_bishop.png',
    'R': 'images/white_rook.png',
    'Q': 'images/white_queen.png',
    'K': 'images/white_king.png',
    'p': 'images/black_pawn.png',
    'n': 'images/black_knight.png',
    'b': 'images/black_bishop.png',
    'r': 'images/black_rook.png',
    'q': 'images/black_queen.png',
    'k': 'images/black_king.png',
}

num_squares = 8
square_size_width = board_size[0] // num_squares
square_size_height = board_size[1] // num_squares

current_click = 1
square_name_one = ''
square_name_two = ''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the square indices
            square_col = mouse_x // square_size_width
            square_row = mouse_y // square_size_height

            file_letters = 'abcdefgh'
            rank_numbers = '87654321'
            chess_file = file_letters[square_col]
            chess_rank = rank_numbers[square_row]
            square_name = chess_file + chess_rank

            if current_click == 1:
                square_name_one = square_name
                if c_board.board[square_row][square_col] == ".":
                    print("Empty square!")
                    pass
                elif not game1.white_turn and c_board.board[square_row][square_col].color == "white":
                    print("It's black's turn!")
                    pass
                elif game1.white_turn and c_board.board[square_row][square_col].color == "black":
                    print("It's white's turn!")
                    pass
                else:
                    valid_moves = c_board.board[square_row][square_col].check_valid_moves()
                    if valid_moves:
                        for move in valid_moves:
                            row = move[0]
                            col = move[1]

                            dot_col = col * square_size_width + square_size_width // 2
                            dor_row = row * square_size_height + square_size_height // 2

                            # Load and scale the dot image
                            dot_image = pygame.image.load('images/grey_dot.png')
                            dot_image = pygame.transform.scale(dot_image, (10, 10))  # Adjust the size as needed

                            # Blit the dot onto the screen at the calculated position
                            screen.blit(dot_image, (dot_col - 5, dor_row - 5))  # Offset to center the dot

                    current_click = 2

            elif current_click == 2:
                square_name_two = square_name
                game1.take_move(square_name_one, square_name_two)

                current_click = 1

    screen.blit(board_image, (0, 0))

    for r in range(len(c_board.board)):
        for c in range(len(c_board.board[r])):
            piece = c_board.board[r][c]
            if piece != '.':
                piece_image = pygame.image.load(piece_images[str(piece)])
                piece_image = pygame.transform.scale(piece_image, (square_size_width, square_size_height))
                screen.blit(piece_image, (c * square_size_width, r * square_size_height))

    pygame.display.update()

pygame.quit()
