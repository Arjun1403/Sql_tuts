from tkinter import *
from tkinter.messagebox import askyesnocancel

from Sql.execute import execute_sql


def register():
    print("inside register")


def check():
    def try_it_out():
        query = c.get()
        output_result = execute_sql.func_run(query=query)
        print("inside login")
        b.grid(row=1, column=2)
        d = Label(f, height=25, width=100, text=output_result)
        d.grid(row=20, column=2)
        value = askyesnocancel(title="query", message="wanna execute in new window?")
        if value:
            check()
        elif value is False:
            master.destroy()

    master = Tk()
    master.geometry("3000x1000")
    # master.configure(bg='#4db4f0')
    f = Frame(master, padx=12, pady=14)
    ff = Frame(master)
    f.configure(bg='#E7EFF3')
    a = Label(f, text='Enter query :', font=('Verdana', 14, 'bold'), bg='#E8F1F2')
    b = Label(f, text='Results', font=('Verdana', 14, 'bold'), bg='#E8F1F2')
    c = Entry(f, width=70, bd=10, bg='#faf5e6')

    # d.pack()
    # d.insert(END,"hellow results")
    e = Button(f, text="Try it out", font=('Verdana', 12, 'bold'), command=try_it_out, bd=2, bg='#E7EFF3')
    ff.place(anchor="s", relx=0.5, rely=1)
    f.place(anchor="c", relx=0.5, rely=0.5)
    a.grid(row=0, column=1)

    c.grid(row=0, column=2)

    e.grid(row=0, column=3)

    master.mainloop()


check()

