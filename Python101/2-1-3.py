#Python 3.7.3
#Example 2-1-3

import turtle

def func_2_1_3():
    'forward=fd back=bk left=lt right=rt'

    t = turtle
    ts = t.Screen()
    t.pencolor("BLUE")
    t.pensize(5)

    t.forward(100)
    t.left(90)
    t.back(50)
    t.right(45)
    t.forward(100)
    
    t.left(90)
    t.pencolor("MAGENTA")

    t.fd(100)
    t.rt(45)
    t.bk(50)
    t.lt(90)
    t.fd(100)

    ts.mainloop()
    
if __name__ == "__main__":
    func_2_1_3()