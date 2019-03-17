#Example 1.7.14
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_714(**x):
    for i,j in x.items():
        print (i,j)
    print ("********")

example_714()
example_714(a=123)
example_714(x=456)
example_714(a=123,b=456,c="Hello",d=[7,8,9],e=(11,12,13),f=(),x=[])

'''
อันนี้พิสดารหนอ่ย คือให้ส่งค่าตัวแปรพร้อมค่าตั้งต้นเข้าไป ต้องลองดูเองหลายๆ แบบแล้วจะเข้าใจ

แสดงผล
********
a 123
********
x 456
********
a 123
b 456
c Hello
d [7, 8, 9]
e (11, 12, 13)
f ()
x []
********
'''
