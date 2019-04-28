'''
Create By Joompot Sriyapan
Date 13/4/2019

Name 
    Example 1.3.1
Description 
    input
Note
    ค่าที่ป้อนผ่านคำสั่ง input จะเป็น string หรือตัวอักษร
    ถ้าจะให้กลายเป็นค่าตัวเลขต้องแปลงด้วยคำสั่ง int() หรือ float()
Display
1. x= 10
2. x= 10 <class 'str'>
3. int(x) = 10 <class 'int'>
4. float(x) = 10.0 <class 'float'>
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.3.1
#Python 3.7.3

def example_301():
    x = input ("Input x ")
    print ("1. x=",x)
    print ("2. x=",x,type(x))
    x = int(x)
    print ("3. int(x) =",x,type(x))
    x = float(x)
    print ("4. float(x) =",x,type(x))

example_301()
