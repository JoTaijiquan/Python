#Python 3.7.3
#Example 3-1-1
import tkinter as tk

class View(tk.Tk):
    'Initializer หรือ Constructor'

    def __init__(self,width=600,height=400,title=""):
        tk.Tk.__init__(self)
        self.title (title)
        self.canvas = tk.Canvas(self,width=width,height=height)
        self.canvas.pack()

    def main_window(self):
        w = self.master.Label(text="test")
        w.pack()

        #w = tk.Label(self.canvas,text="test")
        #w.place(x=100,y=100)
        #w.pack()

if __name__ == "__main__":
    app = View(title="HELLO")
    app.main_window()
    app.mainloop()
    