#Example 1.7.6
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_706(x):
    x[0] +=10
    print ("Now x=",x,x[0])

x = [10]
print (x,x[0])
print()

example_706(x)
print (x,x[0])
print()

example_706(x)
print (x,x[0])


'''
ส่งตัวแปร list เข้าไปใน function
เมื่อมีการเปลี่ยนค่าใน list ภายใน function
ค่าใน list นอก function ก็ถูกเปลี่ยนไปด้วย

แสดงผล
[10] 10

Now x= [20] 20
[20] 20

Now x= [30] 30
[30] 30
'''
