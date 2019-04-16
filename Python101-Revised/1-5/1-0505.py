'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.5
Description 
    list
Note
    append ใช้ใ่ข้อมูลเข้าไปในลิสต์ โดยข้อมูลที่ใส่เข้าไปจะไปต่อท้ายลิสต์เดิม นอกจากลิสต์นั้นเป็นลิสต์ว่าง ก็จะกลายเป็นข้อมูลแรกไป
    extend เอาลิสต์ใหม่ไปต่อท้ายลิสต์เก่า
    insert แทรกข้อมูลเข้าไปในลิสต์ ในตำแหน่งที่ต้องการ
    index หาตำแหน่งของข้อมูลตัวนั้น โดยนับตำแหน่งแรกเป็น 0
    ข้อสังเกต a.extend([“!”,7,8]) จะนำลิสต์ [“!”,7,8] ไป “ต่อกับ” ลิสต์ a
    ส่วน a.append([0,0,0]) จะนำลิต์ [0,0,0] ไปใส่ไว้ “ใน” ลิสต์ a
Display
    1) a= []
    2) append hello to a= ['hello']
    3) append world to a= ['hello', 'world']
    4) extend !,7,8 to a= ['hello', 'world', '!', 7, 8]
    5) insert สวัสดี at position 2, a= ['hello', 'world', 'สวัสดี', '!', 7, 8]
    6) find position of 7 = 4
    7) find position of สวัสดี = 2
    8) append [1,2,3] to a= ['hello', 'world', 'สวัสดี', '!', 7, 8, [0, 0, 0]]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.5
#Python 3.7.3

def example_505():
    a= []
    print ("1) a=",a)
    a.append("hello")
    print ("2) append hello to a=",a)
    a.append("world")
    print ("3) append world to a=",a)
    a.extend(["!",7,8])
    print ("4) extend !,7,8 to a=",a)
    a.insert (2,"สวัสดี")
    print ("5) insert สวัสดี at position 2, a=",a)
    print ("6) find position of 7 =",a.index(7))
    print ("7) find position of สวัสดี =",a.index("สวัสดี"))
    a.append ([0,0,0])
    print ("8) append [1,2,3] to a=",a)  

example_505()
