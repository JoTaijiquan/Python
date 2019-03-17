#Example 1.4.12
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_412():
    y=2
    while y<10000:
        print ("y=",y)
        y*=2

example_412()

'''
while y<10000 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ y<10000
    print ("y =",y) แสดงค่า y
    y*=2  เหมือน y=y*2 
    
แสดงผล
y= 2
y= 4
y= 8
y= 16
y= 32
y= 64
y= 128
y= 256
y= 512
y= 1024
y= 2048
y= 4096
y= 8192
'''
