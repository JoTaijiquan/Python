#Example 10.05
#Python 3.7.1

from turtle import *
import random

color=("RED","GREEN","BLUE","BLACK","GRAY","PINK","LIGHTGREEN",\
       "LIGHTBLUE","PURPLE","VIOLET","BROWN","ORANGE","MAGENTA","CYAN")


def go(x,y,c):
    penup()
    setpos(x,y)
    pendown()
    pencolor(c)
    
def star(x,y,size,c):
    go(x,y,c)
    for i in range(5):
        fd(size)
        rt(144)

rd = random
rd.seed()

speed(0)
for i in range (0,100):
    star(rd.randint(-300,300),rd.randint(-300,300),rd.randint(10,50),color[rd.randint(0,13)])
    

'''

แสดงผล
'''
