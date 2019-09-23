#Python 3.7.3
#Example t1-1-1

import turtle


def t1_1_1():
    t = turtle
    View = t.Screen()

    t.pu()
    t.goto(0,0)

    t.pd()
    t.goto(100,0)

    t.pu()
    t.goto(0,0)

    t.pd()
    t.goto(0,100)


    View.mainloop()


if __name__=="__main__":
    t1_1_1()