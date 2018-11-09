#Example 7.10
#Python3.6.5

def example_710(x=10,y=20):
    print (x,y)

example_710()
example_710(1)
example_710(y=100)
example_710(100,200)
example_710(y=100,x=10)

'''
กำหนดค่าให้กับตัวแปรที่จะส่งค่าเข้าไปใน function ทั้งสองตัว

แสดงผล
10 20
1 20
10 100
100 200
10 100
'''
