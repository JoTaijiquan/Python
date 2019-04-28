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
    a = [11,12,13,14,21,22]
    print ("1)",a[2:2])
    a = [11,12,['xx','yy'],14,21,22]
    print ("2)",a[2:4])

example_513()

'''
a = [11,12,13,14,21,22,23,24]           กำหนดค่า list a=[11,12,13,14,21,22] 
print ("1)",a[2:2])                     แสดงผล list a ตั้งแต่ตัวที่ 2 ไม่เกินตัวที่ 2 ได้ []

a = [11,12,['xx','yy'],14,21,22,23,24]  กำหนดค่า list a=[11,12,['xx','yy'],14,21,22]
print ("2)",a[2:4])                     แสดงผล list a ตั้งแต่ตัวที่ 2 ไม่เกินตัวที่ 4 ได้[['xx', 'yy'], 14]

แสดงผล
1) []
2) [['xx', 'yy'], 14]
'''
