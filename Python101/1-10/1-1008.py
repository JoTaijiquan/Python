#Example 10.08
#Python 3.7.1

import random
import turtle




def box(t,color,size):
    t.pencolor(color) 
    for i in range(4):
        t.fd(size)
        t.lt(90)
    
t = turtle
r = random
r.seed()
t.colormode(255)
t.speed(50)

for i in range(10,120):
    box(t, (r.randint(0,255),r.randint(0,255),r.randint(0,255) ),i*3)
    t.rt(4)
'''

แสดงผล
'''
