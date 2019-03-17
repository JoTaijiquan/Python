#Example 1.5.16
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_516():
    x = ['a','x','a','c,','z','a']
    
    y = x
    print ("1) x=",x)
    print ("2) y=",y)
    x = sorted(x)
    print ("3) x=sorted(x), x=",x)
    print ("4) y=",y)

example_516()

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
