'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.6
Description 
    list
Note
    count นับจำนวนข้อมูลใน list
    remove ลบข้อมูลออกจาก list
Display
    1) a= [1, 2, 3, 4, 5, 6, 3, 4, 3, 6]
    2) count 3? = 3
    3) count 6? = 2
    4) remove 3, a= [1, 2, 4, 5, 6, 3, 4, 3, 6]
    5) remove 3, a= [1, 2, 4, 5, 6, 4, 3, 6]
    6) remove 1, a= [2, 4, 5, 6, 4, 3, 6]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.6
#Python 3.7.3

def example_506():
    a = [1,2,3,4,5,6,3,4,3,6]

    print ("1) a=",a)
    print ("2) count 3? =",a.count(3))
    print ("3) count 6? =",a.count(6))
    a.remove (3)
    print ("4) remove 3, a=",a)
    a.remove (3)
    print ("5) remove 3, a=",a)
    a.remove (1)
    print ("6) remove 1, a=",a)
example_506()