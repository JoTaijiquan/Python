#Example 10.04
#Python 3.7.1

import turtle 

def example_1004():
    t = turtle
    ts = t.Screen()
    t.pencolor("BLUE")  
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.back(100)
    t.right(90)
    t.forward(100)
    ts.mainloop()

example_1004()    

'''
t = turtle          กำหนดให้ t แทน turtle
t.pencolor("BLUE")  เปลีี่ยนปากกาเป็นสีน้ำเงิน
t.forward(100)      เดินหน้า 100 หน่วย
t.left(90)          หันซ้าย 90 องศา
t.forward(100)      เดินหน้า 100 หน่วย
t.right(90)         หันขวา 90 องศา
t.back(100)         ถอยหลัง 100 หน่วย
t.right(90)         หันขวา 90 องศา
t.forward(100)      เดินหน้า 100 หน่วย
แสดงผล
'''
