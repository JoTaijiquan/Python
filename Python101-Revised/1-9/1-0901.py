#Example 1.9.1
#Python 3.6.5
#Created By Jooompot Sriyapan

class Cat:
    def say(self):
        print ("Meow")
        
tom = Cat()
tom.say()


'''
class เป็นการเขียน program แบบ object oriented programming
ภาคทฤษฎีค่อยว่ากัน ดูตัวอย่างก่อน

class Cat:
    def say(self):
        print ("Meow")

เป็นการสร้าง class ชื่อ Cat ซึ่งมีสมาชิกเป็น function ชื่อ say(self)

tom = Cat() เป็นการกำหนดให้ tom เป็นตัวแทน class Cat
ซึ่ง tom ก็จะใช้ความสามารถทุกอย่างของ class Cat ได้ ซึ่งตอนนี้มีอย่าสงเดียวคือ function say(self)
self ใน function say(self) เอาไว้อ้างถึงตัวเอง ยังไม่ต้องสนใจ

tom.say() เป็นการเรียกใช้ function ของ class Cat

แสดงผล
Meow
'''
