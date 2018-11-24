#Example 10.08
#Python 3.7.1

import random
import turtle

def star(color,size):
    t=turtle
    t.pencolor(color) 
    for i in range(5):
        t.fd(size)
        t.rt(144)
    
        
def example_1008(x=100,y=100):
    color = ("#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff" )

    random.seed()

    t=turtle
    t.speed(0)
    for i in range(0,100):
        t.pu() #penup()
        t.setpos(random.randint(-300,300),random.randint(-300,300)) #setposition
        t.pd() #pendown()
        star(color[random.randint(0,6)],random.randint(10,50))

example_1008()
#star("red",100)
'''

แสดงผล
'''
