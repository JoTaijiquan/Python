'''
Create By Joompot Sriyapan
Date 14/4/2019

Name 
    Example 1.4.7
Description 
    for loop
Note
while x<5 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ x<10
    print ("x =",x) แสดงค่า x
    x+=2 บวกค่า x  ทีละ 2 เหมือน x=x+2 
Display
x= 1
x= 3
x= 5
x= 7
x= 9
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.4.7
#Python 3.7.3
#Created By Jooompot Sriyapan

def example_407():
    x=1
    while x<10:
        print ("x=",x)
        x+=2
        
example_407()
