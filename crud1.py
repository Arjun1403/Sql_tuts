import os
from tkinter import *

from PIL import Image, ImageTk

image_root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
docs_root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'open_docs')
master = Tk()
v = IntVar



master.geometry("1480x700")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(image_root_path, "q.jpg"))
q = ImageTk.PhotoImage(i1)
l2 = Label(master, image=q, width=1480, height=700)
l2.place(x=1, y=2)
f = Frame(master, padx=10, pady=10)
ff = Frame(master)
f.configure(bg="#f2c496")


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

f = Frame(master, padx=12, pady=14)
ff = Frame(master)
f.configure(bg='#E7EFF3')
a1=Label(master,text="CREATE TABLE",font=("times",13,"bold"),bg="#ffFFFF")
i1=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit1,bd=3)
b1=Label (master,text="READ TABLE",font=("times",13,"bold"),bg="#ffFFFF")
i2=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit2,bd=3)
c1=Label (master,text="UPDATE TABLE",font=("times",13,"bold"),bg="#ffFFFF")
i3=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit3,bd=3)
d1=Label (master,text="DELETE TABLE",font=("times",13,"bold"),bg="#ffFFFF")
i4=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit4,bd=3)
e1=Label (master,text="SQL KEYWORDS",font=("times",13,"bold"),bg="#ffFFFF")
i5=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit5,bd=3)
f1=Label (master,text="SQL FUNCTIONS",font=("times",13,"bold"),bg="#ffFFFF")
i6=Button(master,text="DOCUMENTATION",font=("times",11,"bold"),command=submit6,bd=3)

a1.place(x=300,y=300)
i1.place(x=450,y=300)
b1.place(x=300,y=400)
i2.place(x=450,y=400)
c1.place(x=300,y=500)
i3.place(x=450,y=500)
d1.place(x=300,y=600)
i4.place(x=450,y=600)
e1.place(x=700,y=300)
i5.place(x=850,y=300)
f1.place(x=700,y=400)
i6.place(x=850,y=400)
mainloop()
