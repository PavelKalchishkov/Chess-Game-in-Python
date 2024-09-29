import ctypes
import tkinter
import customtkinter
from PIL import Image
from chess_project.board import c_board
from chess_project.game import game1
from chess_project.chess_piece import ChessPiece

ctypes.windll.shcore.SetProcessDpiAwareness(0)

piece_click = ''
board_click = ''
# set the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# creating the window
width = 900
height = 600
root = customtkinter.CTk()
root.geometry(f"{width}x{height}")
root.title("Chess game")

# declaring the checkbox variables for board
check_box_one_variable_board = tkinter.IntVar()
check_box_one_variable_board.set(1)
check_box_two_variable_board = tkinter.IntVar()
check_box_two_variable_board.set(0)
check_box_three_variable_board = tkinter.IntVar()
check_box_three_variable_board.set(0)

check_box_one_variable_figures = tkinter.IntVar()
check_box_one_variable_figures.set(1)
check_box_two_variable_figures = tkinter.IntVar()
check_box_two_variable_figures.set(0)
check_box_three_variable_figures = tkinter.IntVar()
check_box_three_variable_figures.set(0)

# we set the board to be the first one
current_board_image = customtkinter.CTkImage(light_image=Image.open("board_images/board_one.png"),
                                             dark_image=Image.open("board_images/board_one.png"),
                                             size=(480, 480))

dot_image = customtkinter.CTkImage(light_image=Image.open("board_images/red_square.png"),
                                   dark_image=Image.open("board_images/red_square.png"),
                                   size=(10, 10))

# creating variable for the piece images
current_white_pawn_image = None
current_white_rook_image = None
current_white_bishop_image = None
current_white_knight_image = None
current_white_queen_image = None
current_white_king_image = None
current_black_pawn_image = None
current_black_rook_image = None
current_black_bishop_image = None
current_black_knight_image = None
current_black_queen_image = None
current_black_king_image = None

# variables for the color background on the pieces
current_first_color = "#8D4D2A"
current_second_color = "#E0BA97"


text_chat_text = ""


# function for changing the images of the pieces
def change_pieces(set_number):
    global piece_images_dict
    global current_white_pawn_image
    global current_white_rook_image
    global current_white_bishop_image
    global current_white_knight_image
    global current_white_queen_image
    global current_white_king_image
    global current_black_pawn_image
    global current_black_rook_image
    global current_black_bishop_image
    global current_black_knight_image
    global current_black_queen_image
    global current_black_king_image

    current_white_pawn_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/white pawn.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/white pawn.png"),
                                                      size=(60, 60))

    current_white_rook_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/white rook.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/white rook.png"),
                                                      size=(60, 60))

    current_white_bishop_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/white bishop.png"),
        dark_image=Image.open(f"set_{set_number}_images/white bishop.png"),
        size=(60, 60))

    current_white_knight_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/white knight.png"),
        dark_image=Image.open(f"set_{set_number}_images/white knight.png"),
        size=(60, 60))

    current_white_queen_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/white queen.png"),
        dark_image=Image.open(f"set_{set_number}_images/white queen.png"),
        size=(60, 60))

    current_white_king_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/white king.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/white king.png"),
                                                      size=(60, 60))
    # black pieces
    current_black_pawn_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/black pawn.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/black pawn.png"),
                                                      size=(60, 60))

    current_black_rook_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/black rook.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/black rook.png"),
                                                      size=(60, 60))

    current_black_bishop_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/black bishop.png"),
        dark_image=Image.open(f"set_{set_number}_images/black bishop.png"),
        size=(60, 60))

    current_black_knight_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/black knight.png"),
        dark_image=Image.open(f"set_{set_number}_images/black knight.png"),
        size=(60, 60))

    current_black_queen_image = customtkinter.CTkImage(
        light_image=Image.open(f"set_{set_number}_images/black queen.png"),
        dark_image=Image.open(f"set_{set_number}_images/black queen.png"),
        size=(60, 60))

    current_black_king_image = customtkinter.CTkImage(light_image=Image.open(f"set_{set_number}_images/black king.png"),
                                                      dark_image=Image.open(f"set_{set_number}_images/black king.png"),
                                                      size=(60, 60))

    piece_images_dict = {
        'P': current_white_pawn_image,
        'N': current_white_knight_image,
        'B': current_white_bishop_image,
        'R': current_white_rook_image,
        'Q': current_white_queen_image,
        'K': current_white_king_image,
        'p': current_black_pawn_image,
        'n': current_black_knight_image,
        'b': current_black_bishop_image,
        'r': current_black_rook_image,
        'q': current_black_queen_image,
        'k': current_black_king_image,
    }


# we set the default to be one
change_pieces("one")

piece_images_dict = {
    'P': current_white_pawn_image,
    'N': current_white_knight_image,
    'B': current_white_bishop_image,
    'R': current_white_rook_image,
    'Q': current_white_queen_image,
    'K': current_white_king_image,
    'p': current_black_pawn_image,
    'n': current_black_knight_image,
    'b': current_black_bishop_image,
    'r': current_black_rook_image,
    'q': current_black_queen_image,
    'k': current_black_king_image,
}

# creating the frames
play_menu = customtkinter.CTkFrame(master=root,
                                   width=width,
                                   height=height
                                   )
play_menu.grid(row=0, column=0)

frame_menu = customtkinter.CTkFrame(master=root,
                                    width=width,
                                    height=height
                                    )
frame_menu.grid(row=0, column=0)

frame_figures = customtkinter.CTkFrame(master=root,
                                       width=width,
                                       height=height
                                       )
frame_figures.grid(row=0, column=0)

frame_board = customtkinter.CTkFrame(master=root,
                                     width=width,
                                     height=height
                                     )
frame_board.grid(row=0, column=0)


def play_menu_frame():
    global text_chat_text
    piece_labels = {}
    dots = []

    # button for going back to the menu
    button1_play = customtkinter.CTkButton(
        play_menu,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_play.place(x=20, y=20)

    label_play_board_image = customtkinter.CTkLabel(play_menu, text="", image=current_board_image)
    label_play_board_image.place(x=90, y=100)

    text_chat = customtkinter.CTkTextbox(play_menu, state='disabled', height=420, width=235, font=("Cosmic Sans", 16))
    text_chat.place(x=610, y=100)

    input_box = customtkinter.CTkEntry(play_menu)
    input_box.place(x=610, y=530)

    def send_message():
        global text_chat_text
        message = input_box.get()
        if message:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, f'Player: {message}\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
            input_box.delete(0, tkinter.END)

            text_chat_text = text_chat.get("1.0", tkinter.END)

    send_button = customtkinter.CTkButton(play_menu, height=27, width=50, text="Send", command=send_message)
    send_button.place(x=760, y=530)

    def check_game_messages(result):
        global text_chat_text
        if result == 1:
            pass
        elif result == 2:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: Checkmate, White wins!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 7:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: Checkmate, Black wins!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 3:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: Draw!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 4:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: This move is not legal!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 5:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: Black is in check!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 6:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: Game is over...\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)
        elif result == 8:
            text_chat.configure(state='normal')
            text_chat.insert(tkinter.END, 'Game: White is in check!\n')
            text_chat.configure(state='disabled')
            text_chat.yview(tkinter.END)

        text_chat_text = text_chat.get("1.0", tkinter.END)

    # function that calculates x,y coordinates
    def calculate_x_y_coordinates(x, y):
        board_width = label_play_board_image.winfo_width()
        square_width = board_width // 8
        print(square_width)
        current_square = ""
        # calculate x coordinates
        if x < square_width:
            current_square += "a"
        elif square_width < x < square_width * 2:
            current_square += "b"
        elif square_width * 2 < x < square_width * 3:
            current_square += "c"
        elif square_width * 3 < x < square_width * 4:
            current_square += "d"
        elif square_width * 4 < x < square_width * 5:
            current_square += "e"
        elif square_width * 5 < x < square_width * 6:
            current_square += "f"
        elif square_width * 6 < x < square_width * 7:
            current_square += "g"
        elif square_width * 7 < x < square_width * 8:
            current_square += "h"

        # calculate y coordinates
        if y < square_width:
            current_square += "8"
        elif square_width < y < square_width * 2:
            current_square += "7"
        elif square_width * 2 < y < square_width * 3:
            current_square += "6"
        elif square_width * 3 < y < square_width * 4:
            current_square += "5"
        elif square_width * 4 < y < square_width * 5:
            current_square += "4"
        elif square_width * 5 < y < square_width * 6:
            current_square += "3"
        elif square_width * 6 < y < square_width * 7:
            current_square += "2"
        elif square_width * 7 < y < square_width * 8:
            current_square += "1"

        return current_square

    def draw_dots_on_board(coordinates_to_draw):
        for coordinates in coordinates_to_draw:
            row = coordinates[0]
            col = coordinates[1]

            current_width = row * 60 + 25
            current_height = col * 60 + 26

            current_dot = customtkinter.CTkLabel(label_play_board_image,
                                                 text="",
                                                 image=dot_image,
                                                 height=10,
                                                 width=10)
            current_dot.place(y=current_width, x=current_height)
            dots.append(current_dot)
            current_dot.bind("<Button-1>", on_dot_click)

    def destroy_dots(dots_list):
        for label in dots_list:
            label.destroy()

    def on_dot_click(event):
        global board_click
        global piece_click
        board_x, board_y = label_play_board_image.winfo_rootx(), label_play_board_image.winfo_rooty()
        # Get the absolute position of the click event
        event_x, event_y = event.x_root, event.y_root
        # Calculate the relative position of the click event on the board
        relative_x, relative_y = event_x - board_x, event_y - board_y

        board_click = calculate_x_y_coordinates(relative_x, relative_y)
        if piece_click != '':
            game_result = game1.take_move(piece_click, board_click)
            check_game_messages(game_result)
            board_click, piece_click = '', ''
            play_menu.after(60, update_pieces_on_board)
        else:
            board_click = ''

    def update_pieces_on_board():
        pieces_to_remove = []

        for piece_label, values in piece_labels.items():
            row = values[0]
            col = values[1]
            piece = values[2]
            board_piece = c_board.board[row][col]

            if str(board_piece) != piece:
                piece_label.destroy()
                pieces_to_remove.append(piece_label)

        for piece in pieces_to_remove:
            del piece_labels[piece]

        destroy_dots(dots)

        draw_pieces_on_board()

    def on_board_click(event):
        global board_click
        global piece_click
        x, y = event.x, event.y
        board_click = calculate_x_y_coordinates(x, y)

        if piece_click != '':
            game_result = game1.take_move(piece_click, board_click)
            check_game_messages(game_result)
            board_click, piece_click = '', ''
            play_menu.after(60, update_pieces_on_board)
        else:
            board_click = ''

    def on_piece_click(event):
        global piece_click
        global board_click
        # Get the absolute position of the board
        board_x, board_y = label_play_board_image.winfo_rootx(), label_play_board_image.winfo_rooty()

        # Get the absolute position of the click event
        event_x, event_y = event.x_root, event.y_root

        # Calculate the relative position of the click event on the board
        relative_x, relative_y = event_x - board_x, event_y - board_y
        if piece_click:
            first_click = piece_click
            piece_click = calculate_x_y_coordinates(relative_x, relative_y)
            if first_click == piece_click:
                board_click, piece_click, first_click = '', '', ''
                play_menu.after(60, update_pieces_on_board)
            else:
                game_result = game1.take_move(first_click, piece_click)
                check_game_messages(game_result)
                board_click, piece_click, first_click = '', '', ''
                play_menu.after(60, update_pieces_on_board)
        else:
            piece_click = calculate_x_y_coordinates(relative_x, relative_y)

            row = int(relative_y / 60)
            col = int(relative_x / 60)

            piece = c_board.board[row][col]
            valid_moves = c_board.board[row][col].check_valid_moves()
            piece_color = c_board.board[row][col].color
            white_turn = game1.white_turn
            white_king_row, white_king_col = game1.white_king_coordinates
            black_king_row, black_king_col = game1.black_king_coordinates

            if white_turn and piece_color == 'black' or not white_turn and piece_color == 'white':
                piece_click = ''

            elif white_turn and piece_color == 'white' and str(piece) == 'K':
                valid_moves = piece.check_white_king_valid_moves(row, col)
                if piece.check_white_castling(white_king_row, white_king_col, 7, 6):
                    valid_moves.append((7, 6))
                if piece.check_white_castling(white_king_row, white_king_col, 7, 2):
                    valid_moves.append((7, 2))
                draw_dots_on_board(valid_moves)

            elif not white_turn and piece_color == 'black' and str(piece) == 'k':
                valid_moves = piece.check_black_king_valid_moves(row, col)
                if piece.check_black_castling(black_king_row, black_king_col, 0, 6):
                    valid_moves.append((0, 6))
                if piece.check_black_castling(black_king_row, black_king_col, 0, 2):
                    valid_moves.append((0, 2))
                draw_dots_on_board(valid_moves)

            elif white_turn and piece_color == 'white' and piece.check_if_white_in_check(white_king_row,
                                                                                         white_king_col):
                valid_moves = piece.get_white_piece_moves_that_stop_check(row, col, white_king_row, white_king_col)
                draw_dots_on_board(valid_moves)

            elif not white_turn and piece_color == 'black' and piece.check_if_black_in_check(black_king_row,
                                                                                             black_king_col):
                valid_moves = piece.get_black_piece_moves_that_stop_check(row, col, black_king_row, black_king_col)
                draw_dots_on_board(valid_moves)

            elif white_turn and piece_color == 'white':
                valid_moves = piece.check_if_white_king_in_check_after_piece_move(piece, white_king_row, white_king_col,
                                                                                  valid_moves)
                if not valid_moves:
                    piece_click = ''
                else:
                    draw_dots_on_board(valid_moves)

            elif not white_turn and piece_color == 'black':
                valid_moves = piece.check_if_black_king_in_check_after_piece_move(piece, black_king_row, black_king_col,
                                                                                  valid_moves)
                if not valid_moves:
                    piece_click = ''
                else:
                    draw_dots_on_board(valid_moves)

    def draw_pieces_on_board():
        global piece_images_dict

        current_width = 0
        current_height = 0
        current_color_counter = 1
        for row in range(8):
            for col in range(8):
                if current_color_counter % 2 != 0:
                    current_color = current_first_color
                else:
                    current_color = current_second_color

                piece = c_board.board[row][col]

                if piece != ".":
                    current_label = customtkinter.CTkLabel(label_play_board_image,
                                                           text="",
                                                           image=piece_images_dict[str(piece)],
                                                           bg_color=current_color)
                    current_label.place(x=current_width, y=current_height)
                    current_label.bind("<Button-1>", on_piece_click)
                    piece_labels[current_label] = [row, col, str(piece)]

                current_color_counter += 1
                current_width += 60

            current_height += 60
            current_width = 0
            current_color_counter -= 1

    # Bind the click event to the label_play_board_image
    label_play_board_image.bind("<Button-1>", on_board_click)
    draw_pieces_on_board()

    if text_chat_text:
        text_chat.configure(state='normal')
        text_chat.insert(tkinter.END, f'{text_chat_text.strip()}\n')
        text_chat.configure(state='disabled')

    play_menu.after(100, play_menu.tkraise)


# menu frame
def create_menu_frame():
    frame_menu.tkraise()

    button1_menu = customtkinter.CTkButton(
        frame_menu,
        text="Play",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=play_menu_frame
    )
    button1_menu.place(x=320, y=100)

    # change figures button
    button2_menu = customtkinter.CTkButton(
        frame_menu,
        text="Figures",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=create_figures_frame
    )
    button2_menu.place(x=320, y=200)

    # change board button
    button3_menu = customtkinter.CTkButton(
        frame_menu,
        text="Board",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=create_board_frame
    )
    button3_menu.place(x=320, y=300)

    # exit button
    button4_menu = customtkinter.CTkButton(
        frame_menu,
        text="Exit",
        corner_radius=8,
        height=45,
        width=250,
        font=("Aerial", 23),
        command=root.quit
    )
    button4_menu.place(x=320, y=400)


# figure frame
def create_figures_frame():
    global piece_images_dict

    # functions for the different figures

    def change_figures_to_one():
        change_pieces("one")

        check_box_two_variable_figures.set(0)
        check_box_three_variable_figures.set(0)
        check_box_figures_one.configure(state="disable")
        check_box_figures_two.configure(state="normal")
        check_box_figures_three.configure(state="normal")

    def change_figures_to_two():
        change_pieces("two")

        check_box_one_variable_figures.set(0)
        check_box_three_variable_figures.set(0)
        check_box_figures_two.configure(state="disable")
        check_box_figures_one.configure(state="normal")
        check_box_figures_three.configure(state="normal")

    def change_figures_to_three():
        change_pieces("three")

        check_box_one_variable_figures.set(0)
        check_box_two_variable_figures.set(0)
        check_box_figures_three.configure(state="disable")
        check_box_figures_one.configure(state="normal")
        check_box_figures_two.configure(state="normal")

    # we set this window to be the main window
    frame_figures.tkraise()

    # button for going back to the main menu
    button1_figures = customtkinter.CTkButton(
        frame_figures,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_figures.place(x=20, y=20)

    # label/heading 'Select a figure type'
    label_heading_figures = customtkinter.CTkLabel(frame_figures,
                                                   text="Select a figure type",
                                                   font=("Cosmic Sans", 60))
    label_heading_figures.place(x=205, y=140)

    # making the 'go back to menu' button
    button1_board = customtkinter.CTkButton(
        frame_figures,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_board.place(x=20, y=20)

    # adding all the images
    # adding the first image
    image_one = customtkinter.CTkImage(light_image=Image.open("set_one_images/black knight.png"),
                                       dark_image=Image.open("set_one_images/black knight.png"),
                                       size=(80, 80))
    label_one = customtkinter.CTkLabel(frame_figures, text="", image=image_one)
    label_one.place(x=210, y=250)

    # adding the second image
    image_two = customtkinter.CTkImage(light_image=Image.open("set_two_images/black knight.png"),
                                       dark_image=Image.open("set_two_images/black knight.png"),
                                       size=(80, 80))
    label_two = customtkinter.CTkLabel(frame_figures, text="", image=image_two)
    label_two.place(x=420, y=250)

    # adding the third image
    image_three = customtkinter.CTkImage(light_image=Image.open("set_three_images/black knight.png"),
                                         dark_image=Image.open("set_three_images/black knight.png"),
                                         size=(80, 80))
    label_three = customtkinter.CTkLabel(frame_figures, text="", image=image_three)
    label_three.place(x=630, y=250)

    # adding all the checkboxes for the images
    check_box_figures_one = customtkinter.CTkCheckBox(frame_figures,
                                                      text="",
                                                      variable=check_box_one_variable_figures,
                                                      onvalue=1,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_figures_to_one
                                                      )
    check_box_figures_one.place(x=243, y=355)

    check_box_figures_two = customtkinter.CTkCheckBox(frame_figures,
                                                      text="",
                                                      variable=check_box_two_variable_figures,
                                                      onvalue=2,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_figures_to_two
                                                      )
    check_box_figures_two.place(x=453, y=355)

    check_box_figures_three = customtkinter.CTkCheckBox(frame_figures,
                                                        text="",
                                                        variable=check_box_three_variable_figures,
                                                        onvalue=3,
                                                        offvalue=0,
                                                        corner_radius=40,
                                                        command=change_figures_to_three
                                                        )
    check_box_figures_three.place(x=663, y=355)

    # we check what is the current figure type, so we call its function
    if check_box_one_variable_figures.get() == 1:
        change_figures_to_one()
    elif check_box_two_variable_figures.get() == 2:
        change_figures_to_two()
    elif check_box_three_variable_figures.get() == 3:
        change_figures_to_three()


# board frame
def create_board_frame():
    # function for changing the board
    def change_board_to_one():
        global current_board_image
        global current_first_color
        global current_second_color
        current_board_image = customtkinter.CTkImage(light_image=Image.open("board_images/board_one.png"),
                                                     dark_image=Image.open("board_images/board_one.png"),
                                                     size=(480, 480))

        check_box_two_variable_board.set(0)
        check_box_three_variable_board.set(0)
        check_box_board_one.configure(state="disable")
        check_box_board_two.configure(state="normal")
        check_box_board_three.configure(state="normal")

        current_first_color = "#8D4D2A"
        current_second_color = "#E0BA97"

    def change_board_to_two():
        global current_board_image
        global current_first_color
        global current_second_color
        current_board_image = customtkinter.CTkImage(light_image=Image.open("board_images/board_two.png"),
                                                     dark_image=Image.open("board_images/board_two.png"),
                                                     size=(480, 480))

        check_box_one_variable_board.set(0)
        check_box_three_variable_board.set(0)
        check_box_board_two.configure(state="disable")
        check_box_board_one.configure(state="normal")
        check_box_board_three.configure(state="normal")

        current_first_color = "#EEEED2"
        current_second_color = "#769656"

    def change_board_to_three():
        global current_board_image
        global current_first_color
        global current_second_color
        current_board_image = customtkinter.CTkImage(light_image=Image.open("board_images/board_three.png"),
                                                     dark_image=Image.open("board_images/board_three.png"),
                                                     size=(480, 480))

        check_box_one_variable_board.set(0)
        check_box_two_variable_board.set(0)
        check_box_board_three.configure(state="disable")
        check_box_board_one.configure(state="normal")
        check_box_board_two.configure(state="normal")

        current_first_color = "#FFFFFF"
        current_second_color = "#3B9AD9"

    # making the main window
    frame_board.tkraise()

    # making the label/heading
    label_heading = customtkinter.CTkLabel(frame_board,
                                           text="Select a board",
                                           font=("Cosmic Sans", 60))
    label_heading.place(x=260, y=140)

    # making the 'go back to menu' button
    button1_board = customtkinter.CTkButton(
        frame_board,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button1_board.place(x=20, y=20)

    # adding all the images
    # adding the first image
    image_one = customtkinter.CTkImage(light_image=Image.open("board_images/board_one_icon.png"),
                                       dark_image=Image.open("board_images/board_one_icon.png"),
                                       size=(90, 90))
    label_one = customtkinter.CTkLabel(frame_board, text="", image=image_one)
    label_one.place(x=210, y=250)

    # adding the second image
    image_two = customtkinter.CTkImage(light_image=Image.open("board_images/board_two_icon.png"),
                                       dark_image=Image.open("board_images/board_two_icon.png"),
                                       size=(90, 90))
    label_two = customtkinter.CTkLabel(frame_board, text="", image=image_two)
    label_two.place(x=420, y=250)

    # adding the third image
    image_three = customtkinter.CTkImage(light_image=Image.open("board_images/board_three_icon.png"),
                                         dark_image=Image.open("board_images/board_three_icon.png"),
                                         size=(90, 90))
    label_three = customtkinter.CTkLabel(frame_board, text="", image=image_three)
    label_three.place(x=630, y=250)

    # adding all the checkboxes for the images
    check_box_board_one = customtkinter.CTkCheckBox(frame_board,
                                                    text="",
                                                    variable=check_box_one_variable_board,
                                                    onvalue=1,
                                                    offvalue=0,
                                                    corner_radius=40,
                                                    command=change_board_to_one
                                                    )
    check_box_board_one.place(x=243, y=355)

    check_box_board_two = customtkinter.CTkCheckBox(frame_board,
                                                    text="",
                                                    variable=check_box_two_variable_board,
                                                    onvalue=2,
                                                    offvalue=0,
                                                    corner_radius=40,
                                                    command=change_board_to_two
                                                    )
    check_box_board_two.place(x=453, y=355)

    check_box_board_three = customtkinter.CTkCheckBox(frame_board,
                                                      text="",
                                                      variable=check_box_three_variable_board,
                                                      onvalue=3,
                                                      offvalue=0,
                                                      corner_radius=40,
                                                      command=change_board_to_three
                                                      )
    check_box_board_three.place(x=663, y=355)

    if check_box_one_variable_board.get() == 1:
        change_board_to_one()
    elif check_box_two_variable_board.get() == 2:
        change_board_to_two()
    elif check_box_three_variable_board.get() == 3:
        change_board_to_three()


create_menu_frame()

# mainloop
root.mainloop()
