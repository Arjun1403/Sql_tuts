import os
from tkinter import *
from tkinter import messagebox
from main_connection import con, cur
from PIL import Image, ImageTk

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master = Tk()
master.geometry("1900x700")
master.configure(bg='#dddddd')
i1 = Image.open(os.path.join(root_path, "ad1.jpg"))
ad1 = ImageTk.PhotoImage(i1)
l2 = Label(master, image=ad1, width=1420, height=700)
l2.place(x=1, y=2)

f = Frame(master, padx=15, pady=15)
ff = Frame(master)
f.configure(bg='#dddddd')

a = Label(f, text='Username:', font=('Verdana', 14, 'bold'), bg='#dddddd')
b = Label(f, text='Password:', font=('Verdana', 14, 'bold'), bg='#dddddd')
c = Entry(f, width=20, bd=4, bg='#faf5e6')
d = Entry(f, width=20, bd=4, bg='#faf5e6', show='*')


def login():
    username = c.get()
    password = d.get()
    cur.execute("select uname,pword from login")
    var = cur.fetchall()

    if username == '' or password == '':
        messagebox.showerror("Error", "Fields cannot be empty!")
    elif (username, password) in var:
        master.destroy()
        adminuser()
    else:
        cur.execute("select uname,pword from login")
        var = cur.fetchall()
        if username == '' or password == '':
            messagebox.showerror("Error", "Fields cannot be empty!")
        else:
            if (username, password) in var:
                master.destroy()

                print("admin")
                adminuser()

            else:
                messagebox.showerror("Error", "login invaild!")





def adminuser():
    os.system('python adminuser.py')


img = Image.open(os.path.join(root_path, "ico.png"))
img = img.resize((112, 123), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
x = Label(f, image=img)

e = Button(f, text="Login", font=('Verdana', 12, 'bold'), command=login, bd=5, bg='#E7EFF3')


f.place(anchor="c", relx=0.55, rely=0.65)

a.grid(row=0, column=1)
b.grid(row=1, column=1)
c.grid(row=0, column=2)
d.grid(row=1, column=2)
e.grid(row=2, column=2)
x.grid(row=0, column=0, rowspan=3)


mainloop()
