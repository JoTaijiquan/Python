'''
Create By Joompot Sriyapan
Date 20/4/2019

Name 
    Example 1.5.12
Description 
    list
Note

Display

Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.12
#Python 3.7.3

def example_512():
    x = ['a','x','a','c,','z','a']
    
    y = x
    print ("1) x=",x)
    print ("2) y=",y)
    x = sorted(x)
    print ("3) x=sorted(x), x=",x)
    print ("4) y=",y)

example_512()

'''
เมื่อ y=x
คำสั่ง x=sorted(x) เป็นการกำหนดค่าใหม่ให้ตัวแปร x
ทำให้ x กับ y หลุดออกจากกัน การเปลี่ยนแปลงค่า x ไม่ทำให้ y เปลี่ยน

แสดงผล
1) x= ['a', 'x', 'a', 'c,', 'z', 'a']
2) y= ['a', 'x', 'a', 'c,', 'z', 'a']
3) x=sorted(x), x= ['a', 'a', 'a', 'c,', 'x', 'z']
4) y= ['a', 'x', 'a', 'c,', 'z', 'a']
'''
