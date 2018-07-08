#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import *
import sys

def show():
	print(entry.get())
	
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

entry=Entry(root,width=40)
entry.grid(row=0,column=0)

b=Button(root,text='click',width=10,command=show)
b.grid(row=1,column=0)

root.mainloop()