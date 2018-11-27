#Example 10.07
#Python 3.7.1

import random
import turtle

def box(color,length):
    t=turtle
    t.pencolor(color) 
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
        
def example_1007(x=100,y=100):
    color = ("#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff" )

    random.seed()

    t=turtle
    t.pu() #penup()
    t.setpos(x,y) #setposition
    t.pd() #pendown()
    for i in range(0,36):
        box(color[random.randint(0,6)],100)
        t.right(10)

example_1007()
'''

แสดงผล
'''
