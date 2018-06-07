print ("สวัสดี ชาวโลก")
'''
#example 3.0
import tkinter as tk

win = tk.Tk()
win.title ("Hello Wolrd!")
win.mainloop()
'''

'''
#Example 3.1

import tkinter as tk

win = tk.Tk()
win.title ("Hello World!")

win.mainloop()
'''

#Example 3.11

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title = ("Hello World!")
ttk.Label (win, text="Label").grid(column=0,row=0)
win.mainloop
