#Python 3.7.3
#Example 2-1-4

import tkinter as tk
import time


class Draw(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title ("test")

        self.canvas = tk.Canvas(self,width=800,height=400)
        self.canvas.pack()

        self.img = tk.PhotoImage(file="ball.png")
        self.canvas.create_image(64,42,image=self.img,anchor=tk.NW)
        self.canvas.create_image(164,42,image=self.img,anchor=tk.NW)

        self.ball = self.canvas.create_oval(10,10,30,30,fill="RED")
    def loadImg(self,imgName):
        img = tk.PhotoImage(file=imgName)
        self.canvas.create_image(64,42,image=img,anchor=NW)
    def animate(self):
        for i in range(100):
            self.canvas.move (self.ball,1,0)
            self.update()
            time.sleep(0.01)


a = Draw()
#a.loadImg("ball.png")
a.animate()
a.mainloop()