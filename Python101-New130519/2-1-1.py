#Python 3.7.3
#Example 2-1-1

import turtle

def func_2_1_1():
    'Python Turtle'

    t = turtle
    ts = t.Screen()
    t.pencolor("RED")
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    ts.mainloop()
    
if __name__ == "__main__":
    func_2_1_1()