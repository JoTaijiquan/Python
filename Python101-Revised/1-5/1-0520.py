#Example 1.5.20
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_520():
    a = (7,8,9)
    
    print ("1) ",a)
    print ("2) ",type(a))
    print ("3) ",a[1])

example_520()

'''
a = (7,8,9)             เป็น tuple คล้ายๆ list แต่เปลี่ยนค่าไม่ได้
print ("1) ",a)         แสดงผล (7, 8, 9)
print ("2) ",type(a))   แสดงประเภทของตัวแปร a เป็น tuple
print ("3) ",a[1])      การอ่านข้อมูลใน tuple ใช้ a[x] เหมือน list a[1] ได้ 8 (เริ่มนับจาก 0)

แสดงผล
1)  (7, 8, 9)
2)  <class 'tuple'>
3)  8
'''
