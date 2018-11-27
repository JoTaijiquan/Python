#Example 10.02
#Python 3.7.1

import turtle

def ex_1():
    turtle.pencolor("RED")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.back(200)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)

def ex_2():
    turtle.pencolor("GREEN")
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.bk(100)
    turtle.rt(90)

def ex_3():
    turtle.penup()
    turtle.fd(100)
    turtle.lt(90)
    turtle.pendown()

def ex_4():
    turtle.pencolor("BLUE")
    turtle.pensize(5)
    turtle.fillcolor("VIOLET")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(100)
        turtle.rt(90)
    turtle.end_fill()
    
ex_1()
ex_2()
ex_3()
ex_4()
'''

แสดงผล
'''
