#Example 4.11
#Python3.6.5

def example_411():
    z=10
    while z>1:
        print ("z=",z)
        z-=2

example_411()

'''
while z>1 ให้วนรอบ ตราบที่เงื่อนไขยังเป็นจริง ในกรณีนี้คือวนรอบตราบที่ z>1
    print ("z =",z) แสดงค่า z
    z-=2 ลบค่า z  ทีละ 2 เหมือน z=z-2 
    
แสดงผล
z= 10
z= 8
z= 6
z= 4
z= 2
'''
