#Example 6.10
#Python3.6.5

def example_610():
    i=8
    for i in 3,"Superman",False,[1,2,3],(3,4),[],(),i,None,i:
        print (i)

example_610()

'''
tuple ไม่จำเป็นต้องอยู่ใน () ก็ได้

แสดงผล
3
Superman
False
[1, 2, 3]
(3, 4)
[]
()
8
None
8
'''
