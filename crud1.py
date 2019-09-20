from tkinter import *
import os
master=Tk()
v=IntVar
master.geometry("1000x500")
master.coe1=Label (master,text="phonenumber:",font=("verdana",10,"bold"),bg="#00FFFF")
master.configure(bg='#4db4f0')
f = Frame(master, padx=10, pady=10)
ff = Frame(master)
f.configure(bg="#f2c496")
def createdoc():
    os.system('python createdoc.py')


def submit1():
    master.destroy()
    fourth= Tk()
    print("create")
    createdoc()
    fourth.mainloop()

def submit2():
    master.destroy()
    fifth= Tk()
    print("read")
    fifth.mainloop()
def submit3():
    master.destroy()
    sixth= Tk()
    print("update")
    sixth.mainloop()
def submit4():
    master.destroy()
    seven= Tk()
    print("delete")
    seven.mainloop()
x=Label(master,text="DOCUMENTS",font=("verdana",10,"bold"),bg="#00FFFF")
a1=Label(master,text="create table:",font=("verdana",10,"bold"),bg="#00FFFF")
i1=Button(master,text="documentation",command=submit1)
b1=Label (master,text="read table",font=("verdana",10,"bold"),bg="#00FFFF")
i2=Button(master,text="documentation",command=submit2)
c1=Label (master,text="update table",font=("verdana",10,"bold"),bg="#00FFFF")
i3=Button(master,text="documentation",command=submit3)
d1=Label (master,text="delete table:",font=("verdana",10,"bold"),bg="#00FFFF")
i4=Button(master,text="documentation",command=submit4)
x.place(x=200,y=200)
a1.place(x=200,y=300)
i1.place(x=300,y=300)
b1.place(x=400,y=500)
i2.place(x=500,y=500)
c1.place(x=600,y=600)
i3.place(x=700,y=600)
d1.place(x=800,y=700)
i4.place(x=900,y=700)
mainloop()