from tkinter import *
top = Tk()

C = Canvas(top, bg="blue", height=300, width=300)
sql = PhotoImage(file = "C:\\Users\Dell\.PyCharmCE2019.1\config\scratches\sql.png")
background_label = Label(top, image=sql)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop

