'''
Create By Joompot Sriyapan
Date 16/4/2019

Name 
    Example 1.5.3
Description 
    list
Note
    กำหนดค่าภายในลิสต์ได้โดยระบุตำแหน่งในลิสต์
    a[0] = 7 กำหนดค่าให้ a[0] = 7
    a[2]=['a','b',"c,d,e",8,9+2] กำหนดค่าให้ a[2] เป็นอีกลิสต์หนึ่งซ้อนเข้าไปได้
Display
    1) a =  [1, 2, 3, 4, 5]
    2) a =  [7, 2, ['a', 'b', 'c,d,e', 8, 11], 4, 5]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.3
#Python 3.7.3

def example_503():
    a = [1,2,3,4,5]

    print ("1) a = ",a)
    a[0]=7
    a[2]=['a','b',"c,d,e",8,9+2]
    print ("2) a = ",a)

example_503()
