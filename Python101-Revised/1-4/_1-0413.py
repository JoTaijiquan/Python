#Example 1.4.13
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_413():
    y=2
    while y<1000000:
        print ("y=",y)
        y**=2

example_413()

'''
while y<1000000 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ y<1000000
    print ("y =",y) แสดงค่า y
    y**=2  เหมือน y=y**2 หรือ y = y ยกกำลัง 2 
    
แสดงผล
y= 2
y= 4
y= 16
y= 256
y= 65536
'''