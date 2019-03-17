#Example 1.4.10
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_410():
    x=1
    while x<10:
        print ("x=",x)
        x+=2
example_410()

'''
while x<5 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ x<10
    print ("x =",x) แสดงค่า x
    x+=2 บวกค่า x  ทีละ 2 เหมือน x=x+2 
    
แสดงผล
x= 1
x= 3
x= 5
x= 7
x= 9
'''
