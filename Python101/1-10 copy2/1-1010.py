#Example 10.10
#Python 3.7.1

import random
import turtle


t=turtle
r=random

r.seed()

t.setup(800,600)
t.title("Random Line")
t.speed(100)
t.colormode(255)

for i in range(100):
    rx=r.randint(-400,400)
    ry=r.randint(-290,290)
    c=r.randint(0,255),r.randint(0,255),r.randint(0,255)
    t.pencolor(c)
    t.goto(rx,ry)
    t.pensize(i%10)

'''

แสดงผล
'''
