from tkinter import *

# creating the window
root = Tk()
root.geometry("900x600")
root.title("Chess game")
root.config(background="#152238")

# start game button
button1 = Button(
    root,
    text="Play",
    width=15,
    font=("Cosmic Sans", 20)
)
button1.place(x=320, y=100)

# change figures button
button2 = Button(
    root,
    text="Figures",
    width=15,
    font=("Cosmic Sans", 20)
)
button2.place(x=320, y=200)

# change board button
button3 = Button(
    root,
    text="Board",
    width=15,
    font=("Cosmic Sans", 20)
)
button3.place(x=320, y=300)

# exit button
button4 = Button(
    root,
    text="Exit",
    width=15,
    font=("Cosmic Sans", 20)
)
button4.place(x=320, y=400)

# mainloop
root.mainloop()
