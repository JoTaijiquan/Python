'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.4
Description 
    list
Note
    print ("1) a = ",a) แสดงค่าใน list ทั้งหมด คือ [1, 2, [11, 12, 13], 4, (21, 22, 23)]
    print ("2) a[2][1] = ",a[2][1]) แสดงค่าของ list ซ้อน list สามารถซ้อนได้หลายชั้น
    print ("3) type of a is",type(a))  a เป็นตัวแปรชนิด list
    print ("4) type of a[1] is",type(a[1])) a[1] มีค่า 2 เป็นตัวแปรชนิด integer
    print ("5) type of a[2] is",type(a[2])) a[2] มีค่า [11,12,13] เป็นตัวแปรชนิด list
    print ("6) type of a[2][1] is",type(a[2][1])) a[2][1] มีค่า  12 เป็นตัวแปรชนิด integer
    print ("7) type of a[4] is",type(a[4])) a[4] มีค่า (21,22,23) เป็นตัวแปรชนิด tuple
    tuple เป็น list ชนิดค่าคงที่
Display
    1) a =  [1, 2, [11, 12, 13], 4, (21, 22, 23)]
    2) a[2][1] =  12
    3) type of a is <class 'list'>
    4) type of a[1] is <class 'int'>
    5) type of a[2] is <class 'list'>
    6) type of a[2][1] is <class 'int'>
    7) type of a[4] is <class 'tuple'>
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.4
#Python 3.7.3

def example_504():
    a = [1,2,[11,12,13],4,(21,22,23)]
    
    print ("1) a = ",a)
    print ("2) a[2][1] = ",a[2][1])
    print ("3) type of a is",type(a))
    print ("4) type of a[1] is",type(a[1]))
    print ("5) type of a[2] is",type(a[2]))
    print ("6) type of a[2][1] is",type(a[2][1]))
    print ("7) type of a[4] is",type(a[4]))

example_504()
