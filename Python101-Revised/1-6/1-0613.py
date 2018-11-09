#Example 6.13
#Python3.6.5

def example_613():
    x = [1,2,3]
    try:
        print (x[2])
    except:
        print ("Ha Ha Ha")
        
    try:
        print (x[6])
    except:
        print ("Error x is out of range")
        
example_613()

'''
try:
except

ใช้ดักจับ error เมื่อเกิด error ใน try คำสั่งใน except จะทำงานโดยไม่เกิด error

แสดงผล
3
Error x is out of range
'''
