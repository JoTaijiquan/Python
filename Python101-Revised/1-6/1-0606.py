#Example 1.6.6
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_606():
    x = [1,3,5,7,9]
    for i in x:
        print (i)
        if i==5:
            x.extend([10,11,12,13])
    print (x)

example_606()

'''
ตรวจสอบ ถ้า i==5 ให้เพิ่มค่าใน list x ด้วย [10,11,12,13]
ซึ่งทำให้จำนวนครั้งของวงรอบเพิ่มขึ้นจากเดิมได้

แสดงผล
1
3
5
7
9
10
11
12
13
[1, 3, 5, 7, 9, 10, 11, 12, 13]
'''
