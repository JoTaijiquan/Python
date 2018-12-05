#Example 10.09
#Python 3.7.1

import random
import turtle

def star(t,color,size):
    t.pencolor(color) 
    for i in range(5):
        t.fd(size)
        t.rt(144)

def spiral(t,color,angle,num_of_round):
    t.clearscreen()
    t.speed(100)
    t.hideturtle()
    t.color(color)

    for i in range(num_of_round):
        t.fd(i); t.lt(angle)


t=turtle

spiral(t,"CYAN",59,250)
spiral(t,"RED",89,250)
spiral(t,"BLUE",91,250)
spiral(t,"GREEN",111,250)
spiral(t,"ORANGE",159,250)
'''

แสดงผล
'''
