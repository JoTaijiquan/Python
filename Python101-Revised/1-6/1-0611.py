#Example 6.11
#Python3.6.5

def example_611():
    for i in range(10):
        if i==5:
            pass
        else:
            print (i)

example_611()

'''
ตรวจสอบ i==5
ไม่สั่ง print(i) แต่ให้ pass ไปเฉยๆ
คำสั่ง pass คือให้ผ่านรอบนี้ไปโดยไม่ทำอะไร

แสดงผล
0
1
2
3
4
6
7
8
9
'''
