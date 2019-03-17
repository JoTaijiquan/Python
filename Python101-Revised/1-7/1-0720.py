#Example 1.7.20
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_720(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return "x=y"

print (example_720(10,20))
print (example_720(9,1))
print (example_720(100,100))

'''
return ตามเงื่อนไขที่แตกต่างกันได้

อาจเปลี่ยน code เป็น
def example_720(x,y):
    if x>y:
        r=x
    elif x<y:
        r=y
    else:
        r= "x=y"
    return r

ก็ได้ผลเหมือนกัน

แสดงผล
20
9
x=y
'''
