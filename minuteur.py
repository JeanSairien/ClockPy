#!/bin/python
import time
import datetime
import tkinter as tk 
from tkinter import *
from clock import *


# def main():
# 	while True: 
# 		hour = datetime.datetime.now() 
# 		print(hour)
# 		l = [17,55,00]
# 		if datetime.datetime.now().hour == l[0] and datetime.datetime.now().minute == l[1] and datetime.datetime.now().second == l[2]:	
# 			print(hour)

# 			time.sleep(10)
# 			r = tk.Tk() 
# 			r.title('Counting Seconds') 
# 			button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
# 			label = tk.Label(r, text= hour  )
# 			label.pack()
# 			button.pack() 
# 			r.mainloop() 

# if __name__ == '__main__':
#     main()		


def main(h, m, s):
    print(h, m, s)
    liste = [h, m, s]
    print(liste)
    while True:
        hour = datetime.datetime.now()
        print(hour)
        #l = [17,55,00]
        l = liste
        if datetime.datetime.now().hour == int(l[0]) and datetime.datetime.now().minute == int(l[1]) and datetime.datetime.now().second == int(l[2]):
            print(hour)

            time.sleep(10)
            r = tk.Tk()
            r.title('Counting Seconds')
            button = tk.Button(r, text='Stop', width=25, command=r.destroy)
            label = tk.Label(r, text= hour  )
            label.pack()
            button.pack()
            r.mainloop()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])