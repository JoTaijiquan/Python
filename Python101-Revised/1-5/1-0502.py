'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.2
Description 
    list
Note
  อ่านค่าในลิสต์โดยใช้ [] ระบุตำแหน่งในลิสต์ โดยตำแหน่งแรก=0
    a[1] = 2
    b[0] = "abc"  
    ถ้าระบุตำแหน่งด้วยเลขลบ จะอ่านจากท้ายลิสต์มา
    a[-1]  = 5 ตำแหน่งสุดท้ายในลิสต์
Display
1) a[1] = 2
2) b[0] = abc
3) a[-2] = 4
4 b[-1] = False
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.2
#Python 3.7.3

def example_502():
    a = [1,2,3,4,5]
    b = ["abc",2,3,False]

    print("1) a[1] =",a[1])
    print("2) b[0] =",b[0])
    print("3) a[-2] =",a[-2])
    print("4 b[-1] =",b[-1])

example_502()
