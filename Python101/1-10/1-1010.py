#Example 10.10
#Python 3.7.1

import turtle
import random

color=("RED","GREEN","BLUE","BLACK","GRAY","PINK","LIGHTGREEN",\
       "LIGHTBLUE","PURPLE","VIOLET","BROWN","ORANGE","MAGENTA","CYAN")

def gotoxy (x,y):
    t = turtle
    t.pu()
    t.goto(x,y)
    t.pd()

def star(x,y,size):
    t = turtle
    gotoxy(x,y)
    for i in range(5):
        t.fd(size)
        t.rt(144)
        
def example_1010():
        t = turtle
        ts = t.Screen()
        t.setup(800,600)
        t.speed(0)
        random.seed()
    
        for i in range(0,50):
                rx = random.randint(-350,350)
                ry = random.randint(-250,250)
                rs = random.randint(10,100)
                rc = color[random.randint(0,13)]
                t.color(rc)
                star(rx,ry,rs)
        ts.mainloop()

example_1010()
'''

แสดงผล
'''
