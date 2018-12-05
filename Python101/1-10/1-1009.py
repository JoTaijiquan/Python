#Example 10.09
#Python 3.7.1

import turtle


def gotoxy (x,y):
    t = turtle
    t.pu()
    t.goto(x,y)
    t.pd()
    
def example_1009(x,y,size,color):
    t = turtle
    gotoxy(x,y)
    t.color(color)
    for i in range(5):
        t.fd(size)
        t.rt(144)

example_1009(0,0,60,"RED")
example_1009(100,100,50,"GREEN")
example_1009(-100,-100,40,"BLUE")
example_1009(-100,100,30,"BLACK")
example_1009(100,-100,20,"BROWN")

'''

แสดงผล
'''
