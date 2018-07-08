#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

import tkinter
from tkinter import *
import sys

def exit():
	sys.exit()
	
def edit():
	label.config(text="Chai Piloo!")
	
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

label=Label(root,text='Hello Fraand!')
label.pack()

f=Frame(root)
f.pack(side=TOP)

b1=Button(f,text="exit",bg='orange',width=25,command=exit)
b1.pack()

b2=Button(f,text="change",bg='green',width=25,command=edit)
b2.pack()



root.mainloop()
