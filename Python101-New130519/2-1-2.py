#Python 3.7.3
#Example 2-1-2

import turtle

def func_2_1_1():
    'Python Turtle'

    t = turtle
    ts = t.Screen()
    t.pencolor("VIOLET")
    t.fillcolor("YELLOW")

    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.end_fill()
    ts.mainloop()
    
if __name__ == "__main__":
    func_2_1_1()