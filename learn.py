import pymysql
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
master=Tk()
v=IntVar
master.geometry("1000x500")
master.configure(bg='#4db4f0')
master.geometry("3000x1000")
master.configure(bg='#4db4f0')
i1 = Image.open("C:\\Users\\Dell\\PycharmProjects\\untitled\\d.png")
d= ImageTk.PhotoImage(i1)
l2 = Label(master, image=d, width=3000, height=1000)
l2.place(x=1, y=2)

def crud1():
    os.system('python crud1.py')

f = Frame(master, padx=20, pady=20)
ff = Frame(master)

f.configure(bg="#f2c496")
f1 = Frame(master, padx=20, pady=20)
f1.configure(bg="#f2c496")
f2 = Frame(master, padx=20, pady=20)
f2.configure(bg="#f2c496")



i4=Image.open("l1.jpg")
img=ImageTk.PhotoImage(i4)
i2=Image.open("exec.jpg")
img1=ImageTk.PhotoImage(i2)
i3=Image.open("t1.jpg")
img2=ImageTk.PhotoImage(i3)

l=Button(f,text="LEARN",image=img, font=('Verdana', 30, 'bold'),command=crud1)
e=Button(f1,text="EXECUTE",font=('Verdana', 30, 'bold'),image=img1)
t=Button(f2,text="TEST",font=('Verdana', 30, 'bold'),image=img2)

f.place(anchor="c", relx=0.2, rely=0.5)
f1.place(anchor="c", relx=0.5, rely=0.5)
f2.place(anchor="c", relx=0.8, rely=0.5)
l.grid(row=1,column=2)
e.grid(row=2,column=2)
t.grid(row=3,column=2)
mainloop()