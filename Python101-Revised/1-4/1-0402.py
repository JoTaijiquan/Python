'''
Create By Joompot Sriyapan
Date 13/4/2019

Name 
    Example 1.4.2
Description 
    for loop
Note
    for i in range(2,10): 
        ทำคำสั่งในบล็อควนรอบใน range(2,10) 
        นับตั้งแต่ 2 ถึงน้อยกว่า 10 (9) แล้วนำค่าในแต่ละรอบมาใส่ใน i
        print (i,i+1)       แสดงค่าของ i แต่ละรอบ
Display
    1 2
    2 3
    3 4
    4 5
    5 6
    6 7
    7 8
    8 9
    9 10
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.4.2
#Python 3.7.3

def example_402():
    for i in range(2,10):
        print (i,i+1)

example_402()
