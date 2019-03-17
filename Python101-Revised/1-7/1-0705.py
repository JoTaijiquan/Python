#Example 1.7.5
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_705(x,y):
    x+=1
    y+=2
    print ("x=",x)
    print ("y=",y)
    print()

x=10; y=20
example_705(x,y)
print ("x=",x)
print ("y=",y)


'''
ส่งค่าตัวแปร2 ตัว เข้าไปใน function
ใน function example705(x,7) มีการเพิ่มค่า x และ y
แต่ไม่กระทบ x และ y นอก function

แสดงผล
x= 11
y= 22

x= 10
y= 20
'''
