import tkinter as tk
import random as r
import time as t
from time import sleep
from PIL import ImageTk,Image
root=tk.Tk()
hatbotimage=Image.open("hatbot.png")
root.geometry("1920x1080")
root.title("Hatbot's Game of Luck")
def roll20():
    res=r.randint(1,20)
    stringver=str(res)
    lbl.config(text=stringver)
def roll6():
    res = r.randint(1,6)
    stringver=str(res)
    lbl.config(text=stringver)
def rollcustom():
    try:
        l1.destroy()
    except NameError:
        pass
    try:
        ent.destroy()
    except NameError:
        pass
    try:
        submit.destroy()
    except NameError:
        pass
    l1=tk.Label(text='Custom number:')
    ent=tk.Entry()
    def submit():
        global num
        global res
        num=int(ent.get())
        res=r.randint(1,num)
        lbl.config(text=str(res))
        l1.destroy()
        ent.destroy()
        submit.destroy()
    submit=tk.Button(text='Submit', command=submit)
    l1.pack()
    ent.pack()
    submit.pack()
def roll100():
    res = r.randint(1,100)
    stringver=str(res)
    lbl.config(text=stringver)
def flipcoin():
    res = r.randint(1,2)
    if res == 1:
        result='Heads!'
    if res == 2:
        result='Tails!'
    lbl.config(text=str(result))
def leave():
    root.destroy()
b1=tk.Button(text='Roll a D20', command=roll20)
b2=tk.Button(text='Roll a custom die',command=rollcustom)
b3=tk.Button(text='Roll a D6', command=roll6)
b4=tk.Button(text='Roll a D100', command=roll100)
b5=tk.Button(text='Flip A Coin', command=flipcoin)
lbl = tk.Label(root, text="Click roll")
exitbutton=tk.Button(text='Exit', command=leave)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
lbl.pack()
exitbutton.place(x=1412,y=0)
hi = ImageTk.PhotoImage(hatbotimage)
labell=tk.Label(image=hi)
labell.image = hi
labell.pack()
root.mainloop()
