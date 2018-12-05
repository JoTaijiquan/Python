#Example 10.04
#Python 3.7.1

from turtle import *

def go(x,y,c):
    penup()
    setpos(x,y)
    pendown()
    pencolor(c)
    
def star(x,y,size,c):
    go(x,y,c)
    for i in range(5):
        fd(size)
        rt(144)

def box(x,y,size,c):
    go(x,y,c)
    for i in range(4):
        fd(size)
        rt(90)

def circlexy(x,y,size,c):
    go(x,y,c)
    circle(size)

speed(100)
bgcolor("lightblue")
star(0,0,100,"RED")
star(100,100,50,"BLUE")
box (200,100,30,"GREEN")
circlexy(-100,100,50,"PURPLE")
'''

แสดงผล
'''
