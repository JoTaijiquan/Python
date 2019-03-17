#Example 1.7.13
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_713(a=1,b=2,*x):
    for i in x:
        print (i)
    print (a,b,x)
    print ("******")

example_713()
example_713(10)
example_713(11,12)
example_713(10,20,30)
example_713(10,20,30,40,50)

'''
ส่งค่าต้วแปรเข้าไปใน function แบบให้ค่าเริ่มต้นสองตัวแรก และไม่จำกัดจำนวนค่าที่เหลือ

แสดงผล
1 2 ()
******
10 2 ()
******
11 12 ()
******
30
10 20 (30,)
******
30
40
50
10 20 (30, 40, 50)
******
'''
