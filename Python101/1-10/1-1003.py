#Example 10.03
#Python 3.7.1

import turtle as t

def example_1003():
    ts = t.Screen()
    t.pencolor("GREEN")  
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.back(100)

    ts.mainloop()
example_1003()    

'''
t.pencolor("GREN")  เปลีี่ยนปากกาเป็นสีเขียว
t.forward(100)      เดินหน้า 100 หน่วย
t.left(90)          หันซ้าย 90 องศา
t.forward(100)      เดินหน้า 100 หน่วย
t.right(90)         หันขวา 90 องศา
t.back(100)         ถอยหลัง 100 หน่วย
แสดงผล
'''
