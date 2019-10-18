from tkinter import *
import os
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import re

def connect():
    global cur,con
    con = pymysql.connect("localhost","root","hussain@1","dbone")
    cur = con.cursor()
    
def regdest():
    register_screen.destroy()
    
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1000x700+150+5")
    Label(register_screen,text="Enter Your Details", bg="white", width="300", height="2", font=("Calibri", 15,"bold")).pack()
    register_screen.resizable(width=False,height=False)

    global username
    global password
    global urentry
    global prentry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    urentry = Entry(register_screen, textvariable=username)
    urentry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    prentry = Entry(register_screen, textvariable=password, show='*')
    prentry.pack()
    Label(register_screen, text="").pack()
    backbtn=Button(register_screen,text="< Back",command=regdest,font=("Calibri",15),compound="left")
    backbtn.place(x=10,y=70)
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()
    urentry.focus_set()
    nikgames=PhotoImage(file="nikgames.png")
    Label(register_screen,image=nikgames).place(x=2,y=500)


def logdest():
    login_screen.destroy()
    

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1000x700+150+5")
    Label(login_screen,text="Enter Your Details", bg="blue", width="300", height="2", font=("Calibri", 15,"bold")).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global uentry
    global pentry

    Label(login_screen, text="Username * ").pack()
    uentry = Entry(login_screen, textvariable=username_verify)
    uentry.pack()
    Label(login_screen, text="").pack()
++    Label(login_screen, text="Password * ").pack()
    pentry = Entry(login_screen, textvariable=password_verify, show='*')
    pentry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    backbtn=Button(login_screen,text="< Back",command=logdest,font=("Calibri",15),compound="left")
    backbtn.place(x=10,y=70)
    uentry.focus_set()


def register_user():
    connect()
    urname = urentry.get()
    prname = prentry.get()
    if urname==" " or prname=="":
        messagebox.showerror("Error","Fields cannot be empty!")
    else:
        cur.execute("SELECT * FROM `login` WHERE `uname` = (%s) ", urname)
        if cur.fetchone() is not None:
             label=Label(register_screen,text="Username already exists").pack()
             
        else:
            password=prname
            flag=1
            while True:
                if len(urname)<2:
                    label=Label(register_screen,text="User name can not be less than 2 letters").pack()
                    flag=0
                    urentry.focus_set()
                    break
                elif len(urname)>12:
                    label=Label(register_screen,text="User name can not be greater than 12").pack()
                    flag=0
                    urentry.focus_set()
                    break
                elif len(password) < 8:
                    label=Label(register_screen,text="Make sure your Password is greater than 8").pack()
                    flag=0
                    prentry.focus_set()
                    break
                elif len(password) > 12:
                    label=Label(register_screen,text="Make sure your Password is less than 16").pack()
                    flag=0
                    prentry.focus_set()
                    break
                elif re.search('[0-9]',password) is None:
                    label=Label(register_screen,text="Make sure your password has a number in it").pack()
                    flag=0
                    prentry.focus_set()
                    break
                elif re.search('[A-Z]',password) is None:
                    label=Label(register_screen,text="Make sure your password has a Upper case letter in it").pack()
                    flag=0
                    prentry.focus_set()
                    break
                else:
                    label=Label(register_screen,text="Your Password is good enough").pack()
                    break
            if flag==1:
                cur.execute("INSERT INTO `login` (uname, pword) VALUES (%s,%s)", (str(urname), str(prname)))
                con.commit()
                urentry.\et=""
                prentry.set=""
                messagebox.showinfo("Success","User Created Successfully")
                Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    connect()
    uname = uentry.get()
    pword = pentry.get()
    cur.execute("select uname,pword from login")
    var = cur.fetchall()
    
    if (uname=='' or pword==''):
        messagebox.showerror("Error","Fields cannot be empty!")
    else:
        if (uname,pword) in var:
            connect()
            cur.execute("update c_log set uname=(%s)",str(uname))
            con.commit()
            login_sucess()
        else:
            messagebox.showerror("Oops","Invalid Password!")
            


def login_sucess():
    main_screen.destroy()
    os.system('python gamepg.py')

def dest():
    MsgBox =messagebox.askquestion ('Exit Application','Are you sure you want to exit the NiK Games?',icon = 'warning')
    if MsgBox == 'yes':
       main_screen.destroy()
       

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x700+150+5")
    main_screen.resizable(width=False,height=False)
    main_screen.title("NiK Games")
    logimg=PhotoImage(file="login.png")
    registerimg=PhotoImage(file="register.png")
    backimg=PhotoImage(file="back.png")
    backbtn=Button(main_screen,text="Back",image=backimg,command=dest,font=("Calibri",15),compound="left")
    Label(text="Welcome to NiK Games", bg="white", width="300", height="2", font=("Calibri", 15,"bold")).pack()
    log=Button(text="Login",width=100,height=50,image=logimg,compound=LEFT,command=login,bg="#b1bce3")
    reg=Button(text="Register", height=50, width=100,image=registerimg,compound=LEFT, command=register,bg="#b1bce3")
    canvas = Canvas(main_screen, width=600, height=600)
    canvas.pack()
    img = ImageTk.PhotoImage(file="nik logo.png")
    canvas.create_image(10,10, anchor=NW, image=img)
    log.place(x=850, y=70)
    reg.place(x=850, y=130)
    backbtn.place(x=10,y=70)
    main_screen.iconphoto(False,img)
    main_screen.mainloop()


main_account_screen()
