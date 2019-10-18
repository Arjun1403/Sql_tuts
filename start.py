import os
from tkinter import *

from PIL import Image, ImageTk

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')

master = Tk()
v = IntVar
master.geometry("1480x700")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(root_path, "ad.jpg"))
ad = ImageTk.PhotoImage(i1)
l2 = Label(master, image=ad, width=1420, height=700)
l2.place(x=1, y=2)


def admin():
    os.system('python adminlog.py')

def user():
    os.system('python login.py')


l = Button(master, text="ADMIN", font=('Verdana', 35, 'bold'), command=admin,bd=15,bg="#d2a679")
e = Button(master, text="USER", font=('Verdana', 35, 'bold'), command=user,bd=15,bg="#d2a679")

l.place(x=800,y=250)
e.place(x=800,y=450)
mainloop()