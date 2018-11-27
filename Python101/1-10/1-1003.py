#Example 10.03
#Python 3.7.1

from turtle import *

def box(x,y,size,c):
    penup()
    setposition(x,y)
    pendown()
    pencolor(c)
    for i in range(4):
        forward(size)
        left(90)

box(0,0,20,"PURPLE")
box(100,100,40,"#FF0000")
box(-100,100,60,"#00FF00")
box(-100,-100,80,"#0000FF")
box(100,-100,100,"#000000")

'''

แสดงผล
'''
