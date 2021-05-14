#Python 3.9.5
#Example 1-7-6

def func_1_7_6(x):
    'คืนค่าออกจากฟังก์ชันด้วย return'

    x+=10
    return(x)

if __name__ == "__main__":
    y=0
    y=func_1_7_6(10)
    print(y)
    print (func_1_7_6(20))