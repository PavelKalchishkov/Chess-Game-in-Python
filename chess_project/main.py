import customtkinter

# set the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# creating the window
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Chess game")


# functions for the buttons
def play():
    print("Play")


def change_figures():
    print("Change figures")


def change_board():
    print("Change board")


# start game button
button1 = customtkinter.CTkButton(
    root,
    text="Play",
    corner_radius=8,
    height=45,
    width=250,
    font=("Cosmic Sans", 23),
    command=play
)
button1.place(x=320, y=100)

# change figures button
button2 = customtkinter.CTkButton(
    root,
    text="Figures",
    corner_radius=8,
    height=45,
    width=250,
    font=("Cosmic Sans", 23),
    command=change_figures
)
button2.place(x=320, y=200)

# change board button
button3 = customtkinter.CTkButton(
    root,
    text="Board",
    corner_radius=8,
    height=45,
    width=250,
    font=("Cosmic Sans", 23),
    command=change_board
)
button3.place(x=320, y=300)

# exit button
button4 = customtkinter.CTkButton(
    root,
    text="Exit",
    corner_radius=8,
    height=45,
    width=250,
    font=("Aerial", 23),
    command=root.quit
)
button4.place(x=320, y=400)


# mainloop
root.mainloop()
