import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
master=Tk()
v=IntVar
master.geometry("3000x1000")
master.configure(bg='#4db4f0')
i1 = Image.open("C:\\Users\\Dell\\PycharmProjects\\untitled\\d.png")
d= ImageTk.PhotoImage(i1)
l2 = Label(master, image=d, width=3000, height=1000)
l2.place(x=1, y=2)


from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("960x600")

canvas = Canvas(root, width=500, height=500)
canvas.pack()

crud = PhotoImage(file="crud.png")
canvas.create_image(250, 250, image=crud)

button_qwer = Button(root, text="asdfasdf", image=crud)

root.mainloop()