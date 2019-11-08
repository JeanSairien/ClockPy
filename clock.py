#!/bin/python
import datetime
import tkinter as tk 
from tkinter import *



def main():
	
	window = Tk()
 
	window.title("Welcome to LikeGeeks app")
	 
	window.geometry('350x200')
	 
	lbl = Label(window, text="Hello")
	 
	lbl.grid(column=0, row=0)
	 
	txt = Entry(window,width=10)
	 
	txt.grid(column=1, row=0)
	 
	def clicked():
	 
	    res = "Text is " + txt.get()
	 
	    lbl.configure(text= res)
	 
	btn = Button(window, text="Click Me", command=clicked)
	 
	btn.grid(column=2, row=0)
	 
	window.mainloop()


if __name__ == '__main__':
    main()



    
    