#Example 1.7.21
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_721(a=0,b=0,c=0):
    return a,b,c

print (example_721())
print (example_721(b=10))
print (example_721(100,101,102)[1])
print (example_721(100,101,102)[2])

'''
return a,b,c ก็คือ return เป็น tuple นั่นเอง ไม่ต้องใส่ () ก็ได้

แสดงผล
(0, 0, 0)
(0, 10, 0)
101
102
'''
