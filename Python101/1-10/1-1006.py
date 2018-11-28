#Example 10.06
#Python 3.7.1

import turtle

color=("RED","GREEN","BLUE","BLACK","GRAY","PINK","LIGHTGREEN",\
       "LIGHTBLUE","PURPLE","VIOLET","BROWN","ORANGE","MAGENTA","CYAN")

color2 = ("#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", \
             "#00ffff", "#ff00ff","#808080","#800000","#008000","#000080",\
             "#808000","#800080","#008080","#c0c0c0","#c00000")

color3 = ((0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),\
          (0,255,255),(0xff,0,0),(0,0xff,0),(0,0,0xff))




def go(t,x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()
    t.setheading(0)

def draw_color(t,c):
    for i in c:
        t.color(i)
        t.fd(100)
        t.write(i,False,"left",("Arial",10,"normal"))
        t.bk(100)
        t.pu()
        t.rt(90)
        t.fd(30)
        t.lt(90)
        t.pd()


t = turtle
t.setup(width=800,height=600,startx=0,starty=0)
t.pensize(10)
t.speed(100)

go(t,-300,200)
draw_color(t,color)             

go(t,-100,200)
draw_color(t,color2)

go(t,100,200)
t.colormode(255)
draw_color(t,color3)
'''

แสดงผล
'''
