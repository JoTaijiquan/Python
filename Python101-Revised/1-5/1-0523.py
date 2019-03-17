#Example 1.5.23
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_523():
    a = 1,2,3
    b = 2,3,4
    c = a+b
    print ("1)",c)
    print ("2)",b*3)

example_523()

'''
ค่าใน tuple เปลี่ยนแปลงไม่ได้ แต่นำมา print ต่อกันได้

แสดงผล
1) (1, 2, 3, 2, 3, 4)
2) (2, 3, 4, 2, 3, 4, 2, 3, 4)
'''
