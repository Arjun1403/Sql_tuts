from tkinter import *
import os
from PIL import Image,ImageTk


master = Tk()
root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master.geometry("1900x700")
master.configure(bg='#dddddd')
i1 = Image.open(os.path.join(root_path, "f2g.jpg"))
f2g = ImageTk.PhotoImage(i1)
l2 = Label(master, image=f2g, width=1480, height=700)
l2.place(x=1, y=2)



def adques():
    os.system('python adques.py')
def crud1():
    os.system('python crud1.py')

f=Button(master, text="Add", font=('Verdana', 16, 'bold'),bd=7,command=adques)
f1=Button(master, text="Update", font=('Verdana', 16, 'bold'),bd=7,command=crud1)
f.place(x=935,y=200)
f1.place(x=930,y=400)

mainloop()
