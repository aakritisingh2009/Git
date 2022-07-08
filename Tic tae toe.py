# imports statements
from tkinter import *
import random
import tkinter.messagebox as tmsg

# gui window setup
root = Tk()
root.geometry("350x350")
root.title("Tic Tac Toe")
root.configure(background="pink")
Label(text=f"Score", font=('Brush Script MT', 28, 'bold')).grid(row=0, column=0)
count = 0


def chance():
    global count
    list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    if count != 9:

        if (count % 2 == 1):
            try:
                a = random.choice(list)
                if a["text"] == "":
                    chval(a, "O")
                elif a["text"] != "":

                    while True:

                        a = random.choice(list)
                        if a["text"] == "":
                            chval(a, "O")
                            break

            except:
                print("something went wrong")


# to change the value of button
def chval(button, text):
    global count

    if button['text'] == "":
        button['text'] = text
        count = count + 1
    else:
        tmsg.showinfo("already",f"{button['text']} is already written")


def winner():
    a = b1["text"]
    b = b2["text"]
    c = b3["text"]
    d = b4["text"]
    e = b5["text"]
    f = b6["text"]
    g = b7["text"]
    h = b8["text"]
    i = b9["text"]
    if a == b == c !="":
        tmsg.showinfo("winner", f"{a} is the winner of this game")
        quit()
    elif a == d == g !="":
        tmsg.showinfo("winner", f"{a} is the winner of this game")
        quit()
    elif a == e == i !="":
        tmsg.showinfo("winner", f"{a} is the winner of this game")
        quit()
    elif b == e == h !="":
        tmsg.showinfo("winner", f"{b} is the winner of this game")
        quit()
    elif c == f == i !="":
        tmsg.showinfo("winner", f"{c} is the winner of this game")
        quit()
    elif c == e == g != "":
        tmsg.showinfo("winner", f"{c} is the winner of this game")
        quit()
    elif d == e == f!="":
        tmsg.showinfo("winner", f"{d} is the winner of this game")
        quit()
    elif g==h==i!="":
        tmsg.showinfo("winner", f"{g} is the winner of this game")
        quit()
    else:
        if count==9:
            tmsg.showinfo("Tie","This is a Draw")
            quit()


# buttons tic tac toe
b1 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b1, "X"), chance(),winner()],
            fg="white")
b2 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b2, "X"), chance(),winner()],
            fg="white")
b3 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b3, "X"), chance(),winner()],
            fg="white")
b4 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b4, "X"), chance(),winner()],
            fg="white")
b5 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b5, "X"), chance(),winner()],
            fg="white")
b6 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b6, "X"), chance(),winner()],
            fg="white")
b7 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b7, "X"), chance(),winner()],
            fg="white")
b8 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b8, "X"), chance(),winner()],
            fg="white")
b9 = Button(root, text="", height=5, width=15, background="black", activebackground="white",
            command=lambda: [chval(b9, "X"), chance(),winner()],
            fg="white")

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=4, column=0)
b8.grid(row=4, column=1)
b9.grid(row=4, column=2)


# Quit button
def quit():
    root.destroy()


exitButton = Button(root, text="Quit", command=quit, font=("Algerian", 20, "bold"))
exitButton.grid(row=0, column=2)

root.mainloop()

