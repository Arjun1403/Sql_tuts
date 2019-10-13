import os
from tkinter import *
from tkinter import messagebox

# from PIL import Image, ImageTk
import pymysql
from PIL import Image, ImageTk

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master = Tk()
master.geometry("3000x1000")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(root_path, "DONE1.png"))
DONE1 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=DONE1, width=3000, height=1000)
l2.place(x=1, y=2)

f = Frame(master, padx=12, pady=14)
ff = Frame(master)
f.configure(bg='#E7EFF3')


def connect():
    global cur
    con = pymysql.connect("localhost", "root", "root123", "dbone")
    cur = con.cursor()


a = Label(f, text='Username:', font=('Verdana', 14, 'bold'), bg='#E8F1F2')
b = Label(f, text='Password:', font=('Verdana', 14, 'bold'), bg='#E8F1F2')
c = Entry(f, width=20, bd=4, bg='#faf5e6')
d = Entry(f, width=20, bd=4, bg='#faf5e6', show='*')


def login():
    connect()
    username = c.get()
    password = d.get()
    cur.execute("select username,password from register")
    var = cur.fetchall()

    if username == '' or password == '':
        messagebox.showerror("Error", "Fields cannot be empty!")
    elif (username, password) in var:
        master.destroy()
        second = Tk()
        print("user")
        learn()
        second.mainloop()
    else:
        cur.execute("select uname,pword from login")
        var = cur.fetchall()
        if username == '' or password == '':
            messagebox.showerror("Error", "Fields cannot be empty!")
        else:
            if (username, password) in var:
                master.destroy()
                second = Tk()
                print("admin")
                learn()
                second.mainloop()
            else:
                messagebox.showerror("Error", "login invaild!")


def register():
    os.system('python register.py')


def learn():
    os.system('python learn.py')


img = Image.open(os.path.join(root_path, "ico.png"))
img = img.resize((112, 123), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
x = Label(f, image=img)

e = Button(f, text="Login", font=('Verdana', 12, 'bold'), command=login, bd=2, bg='#E7EFF3')
v = Button(f, text="register", font=('Verdana', 12, 'bold'), bd=2, command=register, bg='#E7EFF3')
g = Label(ff, text='@suranacollege.edu.in', font=('Times', 10, 'bold'), bg='#4db4f0', fg='#f5f4f2')
ff.place(anchor="s", relx=0.5, rely=1)
f.place(anchor="c", relx=0.5, rely=0.5)
a.grid(row=0, column=1)
b.grid(row=1, column=1)
c.grid(row=0, column=2)
d.grid(row=1, column=2)
e.grid(row=2, column=2)
x.grid(row=0, column=0, rowspan=3)
v.grid(row=2, column=1)
g.grid()

mainloop()
