#Python 3.7.3
#Example 2-1-2
import tkinter as tk
import time
import math

class View(tk.Tk):
    'Initializer หรือ Constructor'

    def __init__(self,width=800,height=400,title=""):
        tk.Tk.__init__(self)
        self.title (title)
        self.canvas = tk.Canvas(self,width=width,height=height)
        self.canvas.pack()

    def shoot(self,angle=45.0,v0=10.0, g=-9.8):
        angle = math.radians(angle)
        vx = v0*math.cos(angle)
        vy = v0*math.sin(angle)

        ball = self.canvas.create_oval(10,300,40,330,fill="RED")
        sx,sy = 10,300

        for i in range(100):
            sx = int(vx*i/10)-sx
            sy = int(vy*i + 0.5*a*i**2/10)-sy
            sy = 0
            self.canvas.move (ball,sx,sy)
            self.update()
            time.sleep(0.1)
    
if __name__ == "__main__":
    app = View(title="test")
    app.shoot()

    app.mainloop()