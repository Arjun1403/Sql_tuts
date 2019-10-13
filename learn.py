import os
from tkinter import *

from PIL import Image, ImageTk

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')

master = Tk()
v = IntVar
master.geometry("1480x700")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(root_path, "fi1.jpg"))
fi1 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=fi1, width=1420, height=700)
l2.place(x=1, y=2)


def crud1():
    os.system('python crud1.py')

def test():
    os.system('python test11.py')


def execute():
    os.system('python execute.py')


f = Frame(master, padx=25, pady=20)
f.configure(bg="#A9A9A9")
f1 = Frame(master, padx=25, pady=20)
f1.configure(bg="#A9A9A9")
f2 = Frame(master, padx=25, pady=20)
f2.configure(bg="#A9A9A9")

i4 = Image.open(os.path.join(root_path, "l1.jpg"))
img = ImageTk.PhotoImage(i4)
i2 = Image.open(os.path.join(root_path, "exec.jpg"))
img1 = ImageTk.PhotoImage(i2)
i3 = Image.open(os.path.join(root_path, "t1.jpg"))
img2 = ImageTk.PhotoImage(i3)

l = Button(f, text="LEARN", image=img, font=('Verdana', 30, 'bold'), command=crud1,bd=15)
e = Button(f1, text="EXECUTE", font=('Verdana', 30, 'bold'), image=img1, command=execute,bd=15)
t = Button(f2, text="TEST", font=('Verdana', 30, 'bold'), image=img2, command=test,bd=15)

f.place(anchor="c", relx=0.2, rely=0.5)
f1.place(anchor="c", relx=0.5, rely=0.5)
f2.place(anchor="c", relx=0.8, rely=0.5)
l.grid(row=1, column=2)
e.grid(row=2, column=2)
t.grid(row=3, column=2)
mainloop()
