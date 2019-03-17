#Example 1.5.19
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_519():
    x = [2,3,4]
    y = x

    print ("1) y is x",y is x)
    print ("2) y == x",y == x)

    y = x[:]
    print ("3) y is x",y is x)
    print ("4) y == x",y ==x)

example_519()

'''
เมื่อ
x = [2,3,4]
y = x

print ("1) y is x",y is x)  แสดงผลเป็น True (จริง)
print ("2) y == x",y == x)  แสดงผลเป็น True (จริง)

เมื่อให้ y= ค่าของ x
y = x[:x]

print ("3) y is x",y is x)  แสดงผลเป็น False (เท็จ) เนื่องจาก y ไม่ได้เป็นตัวเดียวกับ x
print ("4) y == x",y ==x)   แสดงผลเป็น True (จริง) เนื่องจากค่าใน y เท่ากับค่าใน x

แสดงผล
1) y is x True
2) y == x True
3) y is x False
4) y == x True
'''
