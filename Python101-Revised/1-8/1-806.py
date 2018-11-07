#Example 8.06
#Python3.6.5

def example_806():
    x= set([3,5,7,9])
    y= set([1,3,5,7,9,11])

    print ("y is superset of x",y.issuperset(x))
    print ("x is subset of y",x.issubset(y))
    if x < y: print ("x<y is",x<y)

 
example_806()

'''
print ("y is superset of x",y.issuperset(x))
y เป็น superset ของ x เมื่อสมาชิกทุกตัวของ x เป็นสมาชิกของ y

print ("x is subset of y",x.issubset(y))
x เป็น subset ของ y เมื่อสมาชิกทุกตัวของ x เป็นสมาชิกของ y

ข้อสังเกต
ลองตรวจสอบด้วย logic x<y หรือ x>y ดู

แสดงผล
y is superset of x True
x is subset of y True
x<y is True
'''
