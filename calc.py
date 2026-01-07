from tkinter import *
from tkinter import ttk


window = Tk()
window.title("My Calculator")
window.geometry("350x500")
window.config(background="#2c3e50")

e = Entry(window,width=18,borderwidth=5,font=("Aptos",16,"bold"),justify="center",bg="#ecf0f1",fg="#2c3e50")
e.place(x=60,y=10,height=40)


def click(num):
    result  = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b = Button(window,text='1',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(1))
b.place(x=10,y=60)

b = Button(window,text='2',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(2))
b.place(x=80,y=60)

b = Button(window,text='3',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(3))
b.place(x=170,y=60)

b = Button(window,text='4',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(4))
b.place(x=10,y=120)

b = Button(window,text='5',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(5))
b.place(x=80,y=120)

b = Button(window,text='6',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(6))
b.place(x=170,y=120)

b = Button(window,text='7',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(7))
b.place(x=10,y=180)

b = Button(window,text='8',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(8))
b.place(x=80,y=180)

b = Button(window,text='9',width=12,height=2,font=("Aptos",10,"bold"),bg="#90e0ef",command=lambda :click(9))
b.place(x=170,y=180)

b = Button(window,text='0',width=12,height=2,font=("Aptos",10,"bold"),command=lambda :click(0))
b.place(x=80,y=240)


def add():
    global math
    math = "addition"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='+',width=12,height=2,font=("Aptos",10,"bold"),bg="#e67e22",command=add)
b.place(x=240,y=240)

def sub():
    global math
    math = "subtraction"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='-',width=12,height=2,font=("Aptos",10,"bold"),bg="#e67e22",command=sub)
b.place(x=240,y=180)

def mul():
    global math
    math = "multiplication"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)

b = Button(window,text='*',width=12,height=2,font=("Aptos",10,"bold"),bg="#e67e22",command=mul)
b.place(x=240,y=120)

def div():
    global math
    math = "division"
    n1 = e.get()
    global i
    i = int(n1)
    e.delete(0,END)


b = Button(window,text='/',width=12,height=2,font=("Aptos",10,"bold"),bg="#e67e22",command=div)
b.place(x=240,y=60)

def equal():
    n2 = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))


b = Button(window,text='=',width=10,height=2,font=("Aptos",10,"bold"),bg="#27ae60",command=equal)
b.place(x=170,y=240)

def clear():
    e.delete(0,END)


b = Button(window,text='Clear',width=10,height=2,font=("Aptos",10,"bold"),bg="#c0392b",command=clear)
b.place(x=10,y=240)



quit_bnt = Button( window,text="Quit", width=10,height=2,font=("Arial", 14, "bold"),bg="red",fg="white", command=window.destroy)

quit_bnt.place(x=110, y=300)

window.mainloop()