#Example 10.09
#Python 3.7.1

import random
import turtle

def star(color,size):
    t=turtle
    t.pencolor(color) 
    for i in range(5):
        t.fd(size)
        t.rt(144)
    
        
def example_1009(x=100,y=100):
    color = ("#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff" )

    random.seed()

    t=turtle
    t.speed(100)
    t.ht() #t.hideturtle
    for i in range(0,180):
        t.pencolor(color[random.randint(0,6)])
        t.rt(37)
        t.fd(100)

        t.penup()
        t.setposition(0,0)
        t.pendown()
    t.st() #t.showturtle
    

example_1009()

'''

แสดงผล
'''
