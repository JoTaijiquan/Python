#Example 10.06
#Python 3.7.1

from turtle import *

def example_1006(x=100,y=100,color="black",length=100):
    penup()
    setposition (x,y)
    pendown()
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)


example_1006(100,100)
example_1006(-100,100,"red",80)
example_1006(-100,-100,"green",50)
example_1006(100,-100,"blue",30)

'''

แสดงผล
'''
