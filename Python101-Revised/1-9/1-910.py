#Example 9.10
#Python3.6.5

class Animal:
    def __init__(self,common_name='animal'):
        self.common_name = common_name
    def say(self,words='...'):
        print ("I am",self.common_name,words)

class Bird(Animal):
    def __init__(self):
        self.common_name = 'bird'
    def sing(self):
        print ("tweet tweet tweety")

class Cat(Animal):
    def __init__(self):
        self.common_name = 'cat'
    def say(self):
        print ("Meow")

tom = Animal()
tom.say()
tom.say("ha ha ha")
print ("************\n")

tweety = Bird()
tweety.say()
tweety.sing()
print ("************\n")

garfield = Cat()
garfield.say()
print (garfield.common_name)


'''
สร้าง class Bird และ class cat ซึ่ง inherit หรือสืบทอดจาก class Animal
จะเห็นว่า clss Cat สร้าง method ชื่อ say ขึนมาใหม่เอง
ดังนั้นเมื่อ object ที่สร้างจาก class Cat เรียก method say ก็จะได้ตาม say ตัวใหม่นี้

ในตัวอย่างคือ
garfield = Cat()
garfield.say() จะได้ Meow
print (garfield.common_name) จะได้ cat


แสดงผล
I am animal ...
I am animal ha ha ha
************

I am bird ...
tweet tweet tweety
************

Meow
cat

'''
