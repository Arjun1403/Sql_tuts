import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from main_connection import connect
import os
import re

connection, cur = connect()
master = Tk()
v = IntVar
root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master.geometry("1900x700")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(root_path, "fi3.jpg"))
fi3 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=fi3, width=1900, height=700)
l2.place(x=1, y=2)

f = Frame(master, padx=50, pady=50)
ff = Frame(master)
f.configure(bg="#E7EFF3")


def learn():
    os.system('python learn.py')


def fun():
    username = a2.get()
    password = b2.get()
    fname = c2.get()
    lname = d2.get()
    phoneno = e2.get()
    email = f2.get()
    course = g2.get()
    dob = h2.get()


a = Label(ff, text="REGISTER_FORM", font=("times", 20, "bold"), bg="#E7EFF3")
a1 = Label(f, text="USERNAME", font=("verdana", 14, "bold"), bg="#E7EFF3")
a2 = Entry(f, width=24, bd=4)
b1 = Label(f, text="PASSWORD", font=("verdana", 14, "bold"), bg="#E7EFF3")
b2 = Entry(f, width=24, bd=4)
c1 = Label(f, text="FIRST_NAME", font=("verdana", 14, "bold"), bg="#E7EFF3")
c2 = Entry(f, width=24, bd=4)
d1 = Label(f, text="LAST_NAME", font=("verdana", 14, "bold"), bg="#E7EFF3")
d2 = Entry(f, width=24, bd=4)
e1 = Label(f, text="PHONE_NUMBER", font=("verdana", 14, "bold"), bg="#E7EFF3")
e2 = Entry(f, width=24, bd=4)
f1 = Label(f, text="EMAIL", font=("verdana", 14, "bold"), bg="#E7EFF3")
f2 = Entry(f, width=24, bd=4)
g1 = Label(f, text="COURSE", font=("verdana", 14, "bold"), bg="#E7EFF3")
g2 = Entry(f, width=24, bd=4)
h1 = Label(f, text="DOB", font=("verdana", 14, "bold"), bg="#E7EFF3")
h2 = Entry(f, width=24, bd=4)
ff.place(anchor="s", relx=0.5, rely=0.35)
f.place(anchor="c", relx=0.7, rely=1)
a.grid(row=0, column=0, rowspan=1)
a1.grid(row=1, column=0)
a2.grid(row=1, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
c1.grid(row=4, column=0)
c2.grid(row=4, column=1)
d1.grid(row=6, column=0)
d2.grid(row=6, column=1)
e1.grid(row=8, column=0)
e2.grid(row=8, column=1)
f1.grid(row=10, column=0)
f2.grid(row=10, column=1)
g1.grid(row=12, column=0)
g2.grid(row=12, column=1)
h1.grid(row=14, column=0)
h2.grid(row=14, column=1)


def submit():
    cur.execute(
        'INSERT INTO `register` (`username`, `password`, `fname`, `lname`, `phoneno`, `email`, `course`, `dob`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
        (a2.get(), b2.get(), c2.get(), d2.get(), e2.get(), f2.get(), g2.get(), h2.get()))
    connection.commit()
    messagebox.showinfo("success", "login success!!!!")
    learn()


i1 = Button(f, text="SUBMIT", font=("times", 15, "bold"), command=submit, bg="#FF0000", bd=8)
i1.grid(row=15, column=1)
f.place(anchor="c", relx=0.5, rely=0.6)
master.mainloop()
