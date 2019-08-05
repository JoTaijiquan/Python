#Example 10.07
#Python 3.7.1

import turtle

def example_1007(x,y):
    t = turtle
    ts = turtle.Screen()

    t.goto(x,y)
    t.color("CYAN","ORANGE")
    t.begin_fill()
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.end_fill()
    ts.mainloop()
    
example_1007(100,100)
example_1007(-100,-100)
example_1007(-100,100)
example_1007(100,-100)

'''
เพื่อกันงง กลับมาใช้ t=turtle

t = turtle
t.color("RED","GREEN")  กำหนดสีตัวแรกคือสีปากกา ตัวที่สองคือสีระบาย
t.begin_fill()          เริ่มการระบาย
t.fd(size)              t.forward(size)
t.lt(90)                t.left(90)
t.fd(size)              t.forward(size)
t.rt(90)                t.right(90)
t.bk(size)              t.back(size)
t.rt(90)                t.right(90)
t.fd(size)              t.forward(size)
t.end_fill()            t.endfill()
แสดงผล
'''
