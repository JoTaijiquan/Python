#Example 10.05
#Python 3.7.1

from turtle import *

def example_1005():
    pencolor("VIOLET")
    fillcolor("YELLOW")
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    right(90)
    back(100)
    right(90)
    forward(100)
    end_fill()
    
example_1005()    

'''
from turtle import * ทำให้เรียกใช้ฟังก์ชันใน turtle ได้โดยตรง

pencolor("VIOLET")      เปลีี่ยนปากกาเป็นสีม่วง
fillcolor("YELLOW")     เปลี่ยนสีสำหรับระบายเป็นสีเหลือง
begin_fill()            เริ่มต้นระบายสีี
forward(100)            เดินหน้า 100 หน่วย
left(90)                หันซ้าย 90 องศา
forward(100)            เดินหน้า 100 หน่วย
right(90)               หันขวา 90 องศา
back(100)               ถอยหลัง 100 หน่วย
right(90)               หันขวา 90 องศา
forward(100)            เดินหน้า 100 หน่วย
end_fill()              จบการระบายสี
แสดงผล
'''
