#Example 10.06
#Python 3.7.1

import turtle

def example_1006(size=100):
    t = turtle
    ts = turtle.Screen()
    t.color("RED","GREEN")
    t.begin_fill()
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.bk(size)
    t.rt(90)
    t.fd(size)
    t.end_fill()
    ts.mainloop()
    
example_1006(200)    

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
