import os
from tkinter import *

from PIL import Image, ImageTk

image_root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
docs_root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'open_docs')
master = Tk()
v = IntVar



master.geometry("1480x700")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(image_root_path, "q1.jpg"))
q1 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=q1, width=1480, height=700)
l2.place(x=1, y=2)


def read():
    os.system(f'python {os.path.join(docs_root_path, "read11.py")}')


def update():
    os.system(f'python {os.path.join(docs_root_path, "update11.py")}')


def create():
    os.system(f'python {os.path.join(docs_root_path, "create11.py")}')


def keyword():
    os.system(f'python {os.path.join(docs_root_path, "keyword_doc.py")}')


def func():
    os.system(f'python {os.path.join(docs_root_path, "fun_doc.py")}')


def delete():
    os.system(f'python {os.path.join(docs_root_path, "delete11.py")}')


def submit1():
    master.destroy()
    create()


def submit2():
    master.destroy()
    read()


def submit3():
    master.destroy()
    update()


def submit4():
    master.destroy()
    delete()


def submit5():
    master.destroy()
    keyword()

def submit6():
    master.destroy()
    func()



i1=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit1,bd=8)

i2=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit2,bd=8)

i3=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit3,bd=8)

i4=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit4,bd=8)

i5=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit5,bd=8)

i6=Button(master,text="DOCUMENTATION",font=("times",14,"bold"),command=submit6,bd=8)


i1.place(x=550,y=240)

i2.place(x=550,y=330)

i3.place(x=550,y=420)

i4.place(x=550,y=500)

i5.place(x=1140,y=230)

i6.place(x=1140,y=310)
master.mainloop()
