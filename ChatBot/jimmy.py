import tkinter
from tkinter import messagebox

frm = tkinter.Tk()
frm.geometry("300x300")
frm.title("Hello SCMT")
frm.configure(bg="white")

frm2 = tkinter.Tk()
frm2.geometry("300x300")
frm2.title("New form")
frm2.configure(bg="light blue")

lb1 = tkinter.Label(frm2, text="Username:")
lb1.place(x=10,y=10)

lb2 = tkinter.Label(frm2, text="Password:")
lb2.place(x=10,y=50)

txt1 = tkinter.Entry(frm2)
txt1.place(x=100,y=10)

txt2 = tkinter.Entry(frm2)
txt2.place(x=100,y=50)
txt2.config(show="*")

frm.withdraw()

def open():
    user ="SIT"
    pw = "12345"

    txtu = txt1.get()
    txtp = txt2.get()

    if (txtu == user) and (txtp == pw):

        frm.deiconify()
        frm2.withdraw()
    else:
        messagebox.showerror("Information", "Username or Password incorect..!!")
        txt1.delete(0,'end')
        txt2.delete(0,'end')
        txt1.focus()
def show():
        txt2.config(show="")
        txt2.focus()

btnopen = tkinter.Button(frm2, text="Login",width=15, command= open)
btnopen.place(x=10, y=150)

btnexit = tkinter.Button(frm2, text="Exit",width=15, command= exit)
btnexit.configure(bg="gray")
btnexit.place(x=150, y=150)

btnshow = tkinter.Checkbutton(frm2, text="Show Passworld",command= show)
btnshow.place(x=100,y=80)

def black():
    frm.configure(bg="black")
def red():
    frm.configure(bg="red")
def green():
    frm.configure(bg="green")
def blue():
    frm.configure(bg="blue")
def pink():
    frm.configure(bg="pink")

bt1 = tkinter.Checkbutton(frm, text="Black", command=black)
bt1.place(x=100, y=10)
bt1.configure(fg="black", font=("Times New Roman", 16))

bt2 = tkinter.Checkbutton(frm, text="Red", command=red)
bt2.place(x=100, y=50)
bt2.configure(fg="red", font=("Times New Roman", 16))

bt2 = tkinter.Checkbutton(frm, text="Green", command=green)
bt2.place(x=100, y=100)
bt2.configure(fg="green", font=("Times New Roman", 16))

bt3 = tkinter.Checkbutton(frm, text="Blue", command=blue)
bt3.place(x=100, y=150)
bt3.configure(fg="blue", font=("Times New Roman", 16))

bt5 = tkinter.Checkbutton(frm, text="Pink", command=pink)
bt5.place(x=100, y=200)
bt5.configure(fg="pink", font=("Times New Roman", 16))


frm.mainloop()