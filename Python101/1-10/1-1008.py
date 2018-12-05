#Example 10.08
#Python 3.7.1

import turtle

def example_1008(x,y):
    t = turtle
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("MAGENTA","GREY")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
example_1008(100,100)
example_1008(-100,-100)
example_1008(-100,100)
example_1008(100,-100)

'''

แสดงผล
'''
