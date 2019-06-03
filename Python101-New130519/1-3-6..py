#Python 3.7.3
#Example 1-3-6

import random

def func_1_3_6():
    'การสร้างตัวเลขสุ่ม คำสั่ง random.seed() จะใช้ค่าตั้งต้นจากนาฬิกาของระบบ'

    random.seed()
    x = random.randint(1,10)
    print (x)

if __name__ == "__main__":
    func_1_3_6()