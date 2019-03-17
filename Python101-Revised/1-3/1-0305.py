#Example 1.3.5
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_305():
    x = input ("Input x ")
    print ("1) x=",x)
    print ("2) x=",x,type(x))
    x = int(x)
    print ("3) int(x) =",x,type(x))
    x = float(x)
    print ("4) float(x) =",x,type(x))

example_305()

'''
แสดงผล

Input x

ลองป้อน 10

1) x= 10
2) x= 10 <class 'str'>
3) int(x) = 10 <class 'int'>
4) float(x) = 10.0 <class 'float'>

ค่าที่ป้อนผ่านคำสั่ง input จะเป็น string หรือตัวอักษร
ถ้าจะให้กลายเป็นค่าตัวเลขต้องแปลงด้วยคำสั่ง int() หรือ float()
'''
