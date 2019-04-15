'''
Create By Joompot Sriyapan
Date 14/4/2019

Name 
    Example 1.4.8
Description 
    for loop
Note
while y<10000 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ y<10000
    print ("y =",y) แสดงค่า y
    y*=2  เหมือน y=y*2 
Display
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
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.4.8
#Python 3.7.3

def example_408():
    y=2
    while y<10000:
        print ("y=",y)
        y*=2

example_408()
