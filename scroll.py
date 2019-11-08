#!/bin/python
import datetime
import tkinter as tk 
from tkinter import *
from tkinter import scrolledtext

def main():
	window = Tk()
 
	window.title("Welcome to LikeGeeks app")
 
	window.geometry('350x200')
 
	txt = scrolledtext.ScrolledText(window,width=40,height=10)
 
	txt.grid(column=0,row=0)
 
	window.mainloop()
if __name__ == '__main__':
    main()		



