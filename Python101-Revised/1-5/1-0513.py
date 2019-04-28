'''
Create By Joompot Sriyapan
Date 20/4/2019

Name 
    Example 1.5.13
Description 
    list
Note

Display

Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.13
#Python 3.7.3

def example_513():
    print ("1) 4 is 4:",4 is 4)
    print ("2) 4 is (4,3):",4 is (4,3))
    print ("3) 4 in (4,3):",4 in (4,3))
    print ("4) (3,4) in (2,3,4):",(3,4) in (2,3,4))
    print ("5) (3,4) in (2,(3,4),4):",(3,4) in (2,(3,4),4))
    print ("6) (3,4) is (2,3,4):",(3,4) is (2,3,4))
    print ("7) (3,4) is (3,4):",(3,4) is (3,4))
    print ("8) (3,4) in (3,4):",(3,4) in (3,4))
    print ("9) (3,4) == (3,4):",(3,4)==(3,4))

example_513()

'''
ตัวอย่างการใช้ is (คือ) in (อยู่ใน) และ == (เท่ากับ)
คำตอบเป็นสถานะ True (จริง) หรือ False (เท็จ)

แสดงผล
1) 4 is 4: True
2) 4 is (4,3): False
3) 4 in (4,3): True
4) (3,4) in (2,3,4): False
5) (3,4) in (2,(3,4),4): True
6) (3,4) is (2,3,4): False
7) (3,4) is (3,4): False
8) (3,4) in (3,4): False
9) (3,4) == (3,4): True
'''
