#Example 10.05
#Python 3.7.1

from turtle import *

def example_1005(x=100,y=100,color="black",length=100):
    setposition (x,y)
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)

example_1005(100,100)
example_1005(-100,100,"red",80)
example_1005(-100,-100,"green",50)
example_1005(100,-100,"blue",30)

'''

แสดงผล
'''
