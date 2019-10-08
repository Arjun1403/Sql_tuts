import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
master=Tk()
v=IntVar
root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
master.geometry("3000x1000")
master.configure(bg='#4db4f0')
i1 = Image.open(os.path.join(root_path, "DONE12.png"))
DONE12= ImageTk.PhotoImage(i1)
l2 = Label(master, image=DONE12, width=3000, height=1000)
l2.place(x=1, y=2)

f= Frame(master, padx=70, pady=70)
ff = Frame(master)
f.configure(bg="#E7EFF3 ")
def learn():
    os.system('python learn.py')


def fun():
    username=a2.get()
    password=b2.get()
    fname=c2.get()
    lname=d2.get()
    phoneno=e2.get()
    email=f2.get()
    course=g2.get()
    dob=h2.get()


a1=Label(f,text="USERNAME",font=("verdana",12,"bold"),bg="#E7EFF3 ")
a2=Entry(f,width=20)
b1=Label (f,text="PASSWORD",font=("verdana",12,"bold"),bg="#E7EFF3 ")
b2=Entry(f,width=20)
c1=Label (f,text="FIRST_NAME",font=("verdana",12,"bold"),bg="#E7EFF3 ")
c2=Entry(f,width=20)
d1=Label (f,text="LAST_NAME",font=("verdana",12,"bold"),bg="#E7EFF3 ")
d2=Entry(f,width=20)
e1=Label (f,text="PHONE_NUMBER",font=("verdana",12,"bold"),bg="#E7EFF3 ")
e2=Entry(f,width=20)
f1=Label (f,text="EMAIL",font=("verdana",12,"bold"),bg="#E7EFF3 ")
f2=Entry(f,width=20)
g1=Label (f,text="COURSE",font=("verdana",12,"bold"),bg="#E7EFF3 ")
g2=Entry(f,width=20)
h1=Label (f,text="DOB",font=("verdana",12,"bold"),bg="#E7EFF3 ")
h2=Entry(f,width=20)
ff.place(anchor="s", relx=0.5, rely=1)
f.place(anchor="c", relx=0.5, rely=0.5)

a1.grid(row=0,column=0)
a2.grid(row=0,column=1)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
c1.grid(row=4,column=0)
c2.grid(row=4,column=1)
d1.grid(row=6,column=0)
d2.grid(row=6,column=1)
e1.grid(row=8,column=0)
e2.grid(row=8,column=1)
f1.grid(row=10,column=0)
f2.grid(row=10,column=1)
g1.grid(row=12,column=0)
g2.grid(row=12,column=1)
h1.grid(row=14,column=0)
h2.grid(row=14,column=1)

def conn():
    global con
    con=pymysql.connect("localhost","root","root123","dbone")
    global cur
    cur=con.cursor()
def submit():
    conn()
    cur.execute('INSERT INTO `dbone`.`register` (`username`, `password`, `fname`, `lname`, `phoneno`, `email`, `course`, `dob`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)' ,(a2.get(),b2.get(),c2.get(),d2.get(),e2.get(),f2.get(),g2.get(),h2.get()))
    con.commit()
    messagebox.showinfo( "success","login success!!!!")
    learn()

i1=Button(f,text="SUBMIT",command=submit)
i1.grid(row=15,column=1)
f.place(anchor="c", relx=0.5, rely=0.5)
master.mainloop()
