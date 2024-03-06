import customtkinter

# set the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# creating the window
width = 900
height = 600
root = customtkinter.CTk()
root.geometry(f"{width}x{height}")
root.title("Chess game")


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


# functions for the buttons
def play():
    print("Play")


def change_board():
    frame_board.tkraise()

    button5_figures = customtkinter.CTkButton(
        frame_board,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button5_figures.place(x=20, y=20)


# start game button
def create_menu_frame():
    frame_menu.tkraise()

    button1_menu = customtkinter.CTkButton(
        frame_menu,
        text="Play",
        corner_radius=8,
        height=45,
        width=250,
        font=("Cosmic Sans", 23),
        command=play
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
        command=change_board
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


def create_figures_frame():
    frame_figures.tkraise()

    button5_figures = customtkinter.CTkButton(
        frame_figures,
        text="Back to menu",
        corner_radius=8,
        height=45,
        width=200,
        font=("Cosmic Sans", 23),
        command=create_menu_frame
    )
    button5_figures.place(x=20, y=20)


create_menu_frame()

# mainloop
root.mainloop()
