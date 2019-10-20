
import os
from tkinter import *
from tkinter import messagebox
from main_connection import connect
from PIL import Image, ImageTk

connection, cur = connect()

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master = Tk()
master.geometry("1900x700")
master.configure(bg='#dddddd')
i1 = Image.open(os.path.join(root_path, "ad2.jpg"))
ad2 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=ad2, width=1480, height=700)
l2.place(x=1, y=2)


ques = Entry(master, width=180, bd=5, bg='#faf5e6')
mark=Entry(master, width=10, bd=5, bg='#faf5e6')
opt = Entry(master, width=100, bd=4, bg='#faf5e6')
ranswer=Entry(master, width=70, bd=5, bg='#faf5e6')

ques.place(x=10,y=200)
mark.place(x=1230,y=200)
opt.place(x=100,y=340)
ranswer.place(x=700,y=610)
mainloop()

