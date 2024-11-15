#Aaron Beneditt

import tkinter as tk
#from tkinter.simpledialog import askinteger
from tkinter import *
#from tkinter import messagebox

top = Tk()


top.geometry("500x500")
answer = Text(width=47, height=2)
answer.place(x=50, y=100)
def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)

        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)



B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=50, y=150)

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=150, y=150)

B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=250, y=150)

B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=50, y=250)

B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=150, y=250)

B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=250, y=250)

B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=50, y=350)

B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=150, y=350)

B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=250, y=350)

B10 = Button(top, text="C", width=10, height=2, bg="red", command=lambda: show("C"))
B10.place(x=350, y=150)

B11 = Button(top, text="+", width=10, height=2, command=lambda: show("+"))
B11.place(x=350, y=200)

B12 = Button(top, text="-", width=10, height=2, command=lambda: show("-"))
B12.place(x=350, y=250)

B13 = Button(top, text="*", width=10, height=2, command=lambda: show("*"))
B13.place(x=350, y=300)

B13 = Button(top, text="/", width=10, height=2, command=lambda: show("/"))
B13.place(x=350, y=350)

B14 = Button(top, text="=", width=10, height=2, command=lambda: show("="))
B14.place(x=350, y=400)
top.mainloop()

















#top.mainloop() #keep it funning until you close it

# "eval" calcula las expresiones

