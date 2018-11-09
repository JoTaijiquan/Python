#Example 9.09
#Python3.6.5

class Animal:
    def __init__(self,common_name='cat'):
        self.common_name = common_name
    def say(self,say='...'):
        print ("I am",self.common_name,say)

class Bird(Animal):
    def __init__(self):
        self.common_name = 'bird'
    def sing(self):
        print ("tweet tweet tweety")
    
tom = Animal()
tom.say()
tom.say("Meow")
print ("************")

tweety = Bird()
tweety.say()
tweety.say("Tweet")
tweety.sing()


'''
มีการสืบทอด class เรียกว่าการ Inherit หรือ Inheritance
โดย class Bird(Animal) สืบทอดคุณสมบัติจาก class Animal
ซึ่งทำให้ object ที่สร้างจาก class Bird สามารถใช้ method ของ class Animal ได้เลย

ลองดูตัวอย่าง class Bird ไม่มี method say แต่ เมื่อสร้าง object ขึ้นมาก็สามารถใช้ say() ได้
แต่ object ที่สร้างจาก class Animal ไม่สามารถใช้ method ใน clas Bird ได้


แสดงผล
I am cat ...
I am cat Meow
************
I am bird ...
I am bird Tweet
tweet tweet tweety
'''
