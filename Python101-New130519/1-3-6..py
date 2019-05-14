#Python 3.7.3

import random

def func_1_3_6():
    'random คำสั่ง random.seed() จะใช้ค่าตั้งต้นจากนาฬิการของระบบ'

    random.seed()
    x = random.randint(1,10)
    print (x)

if __name__ == "__main__":
    func_1_3_6()