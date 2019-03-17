#Example 1.9.2
#Python 3.6.5
#Created By Jooompot Sriyapan

class Cat:
        
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")

tom = Cat()
tom.say()
tom.say()
print()

Cat()
print()

Cat().say()

'''
สมาชิกของ class Cat มีสองตัวละ
__init__(self) เรียกว่า Initializer จะเป็น function ที่ทำงานอัตโนมัตเมื่อ class ถูกสร้างขึ้น
บางตำราอาจเรียกว่า Constructor ไม่ต้องตกใจ เพราะ __init__ ใน python ถูกใช้ในฐานะของ
Constructor เมื่อเทียบกับโปรแกรมอื่นๆ (ถ้าตามตำราแล้ว Constructor จะเป็น __new__ แต่เรา
จะยังไม่ใช้ตัวนี้)

แสดงผล
Aow
Meow
Meow

Aow

Aow
Meow
'''
