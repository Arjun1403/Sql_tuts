import pymysql
from tkinter import *
from tkinter import messagebox
master=Tk()
v=IntVar
master.geometry("1000x500")
master.configure(bg='#4db4f0')

f = Frame(master, padx=10, pady=10)
ff = Frame(master)
f.configure(bg="#f2c496")
def fun():
    username=a2.get()
    password=b2.get()
    fname=c2.get()
    lname=d2.get()
    phoneno=e2.get()
    email=f2.get()
    course=g2.get()
    dob=h2.get()

a1=Label(master,text="username:",font=("verdana",10,"bold"),bg="#00FFFF")
a2=Entry(master,width=20)
b1=Label (master,text="password:",font=("verdana",10,"bold"),bg="#00FFFF")
b2=Entry(master,width=20)
c1=Label (master,text="firstname:",font=("verdana",10,"bold"),bg="#00FFFF")
c2=Entry(master,width=20)
d1=Label (master,text="lastnamename:",font=("verdana",10,"bold"),bg="#00FFFF")
d2=Entry(master,width=20)
e1=Label (master,text="phonenumber:",font=("verdana",10,"bold"),bg="#00FFFF")
e2=Entry(master,width=20)
f1=Label (master,text="email:",font=("verdana",10,"bold"),bg="#00FFFF")
f2=Entry(master,width=20)
g1=Label (master,text="course:",font=("verdana",10,"bold"),bg="#00FFFF")
g2=Entry(master,width=20)
h1=Label (master,text="dob:",font=("verdana",10,"bold"),bg="#00FFFF")
h2=Entry(master,width=20)

a1.pack()
a2.pack()
b1.pack()
b2.pack()
c1.pack()
c2.pack()
d1.pack()
d2.pack()
e1.pack()
e2.pack()
f1.pack()
f2.pack()
g1.pack()
g2.pack()
h1.pack()
h2.pack()

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

i1=Button(master,text="submit",command=submit)
i1.pack()
master.mainloop()

