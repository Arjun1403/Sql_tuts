from tkinter import *
import os
from PIL import Image,ImageTk

master = Tk()
root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master.geometry("1900x700")
master.configure(bg='#dddddd')
i1 = Image.open(os.path.join(root_path, "f2g.jpg"))
f2g = ImageTk.PhotoImage(i1)
l2 = Label(master, image=f2g, width=1900, height=700)
l2.place(x=1, y=2)



def file():
    os.system('python crud1.py')


f=Button(master, text="Update", font=('Verdana', 16, 'bold'),bd=7,command=file)
f.place(x=850,y=350)

mainloop()
