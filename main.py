import tkinter as tk
import random as r
import time as t
from time import sleep
root=tk.Tk()
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
    l1=tk.Label(text='Custom number:')
    ent=tk.Entry()
    def submit():
        global num
        global res
        num=int(ent.get())
        res=r.randint(1,num)
        lbl.config(text=str(res))
        t.sleep(1)
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
b1=tk.Button(text='Roll a D20', command=roll20)
b2=tk.Button(text='Roll a custom die',command=rollcustom)
b3=tk.Button(text='Roll a D6', command=roll6)
b4=tk.Button(text='Roll a D100', command=roll100)
lbl = tk.Label(root, text="Click roll")
b1.pack()
b2.pack()
b3.pack()
b4.pack()
lbl.pack()
root.mainloop()
