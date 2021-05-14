#Python 3.9.5
#Example 1-4-3

def func_1_4_3():
    'กำหนดค่าใน range ให้ข้ามทีละ 2'

    for i in range(1,20,2):
        print (i)
        if i>10:
            break
if __name__ == "__main__":
    func_1_4_3()