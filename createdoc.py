import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=9, width=200)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)



description = """The CREATE TABLE statement is used to create a table in SQL. We know that a table comprises of rows and columns. So while creating tables we have to provide all the information to SQL about the names of the columns, type of data to be stored in columns, size of the data etc.
"""


T.insert(tk.END, description)



syntax1="""create table "tablename"
("column1" "data type",
"column2" "data type",
"column3" "data type",
...
"columnN" "data type");
"""

T.insert(tk.END,syntax1)

tk.mainloop()
