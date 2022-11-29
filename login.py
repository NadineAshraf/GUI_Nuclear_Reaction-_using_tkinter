from tkinter import *
from tkinter import messagebox
from nuclear import *

 
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Nadine" and password == "123"):
 
        messagebox.showinfo("","Login Success")
        root.destroy()
        Welcome()
 
    else :
        messagebox.showinfo("","Incorrent username and password")
 
 
root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2
 
Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Ok ,height = 2, width = 13).place(x=10, y=100)
 
root.mainloop()