#Example 10.04
#Python 3.7.1

from turtle import *

def go(x,y):
    penup()
    setpos(x,y)
    pendown()
    
def star(x,y,size,c):
    go(x,y)
    pencolor(c)
 
    for i in range(5):
        fd(size)
        rt(144)

def example_1004(length=100):
    for i in range(4):
        forward(length)
        left(90)

star(0,0,100,"RED")
star(100,100,50,"BLUE")

'''

แสดงผล
'''
