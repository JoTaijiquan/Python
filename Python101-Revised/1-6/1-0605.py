#Example 6.05
#Python3.6.5

def example_605():
    for i in (1,3,5,7,8,9,10):
        print (i)
        if i==5:
            break
        else:
            pass
    print ("end at",i)

example_605()

'''
ตรวจสอบ ถ้า i==5 ให้ออกจากวงรอบด้วยคำสั่ง break

แสดงผล
1
3
5
end at 5
'''
