#Example 1.9.11
#Python 3.6.5
#Created By Jooompot Sriyapan

class Animal:
    def __init__(self,common_name='animal'):   
        self.common_name = common_name
    def say (self,words='...'):
        print ("I am",self.common_name,words)

class Action:
    def walk(self):
        print ("walk")
    def run(self):
        print ("run")

class Cat(Animal,Action):
    def run(self):
        print ("run run run")
    def dance(self):
        self.walk()
        self.run()
        self.walk()

tom = Cat()
print (tom.common_name)
tom.dance()
print ("************\n")
tom.say("ha ha ha")
tom.walk()
tom.run()


'''
ตัวอย่างการสืบทอดจากสอง class
class Cat(Animal, Action) สืบทอดมาจาก class Animal และ class Action

tom = Cat()
tom.say ได้  say มีใน Aืnimal เรียกใช้ได้เลย
tom.walk ได้ walk มีใน Action เรียกใช้ได้
tom.run ได้ run มีใน Action จริงๆ เรียกได้เลย แต่ class Cat สร้าง run ใหม่ต่างจากของเดิม
tom.dance ก็ได้ ซึ่ง dance() เรียกใช้ method ที่มีในตัวเองผ่าน self


แสดงผล
animal
walk
run run run
walk
************

I am animal ha ha ha
walk
run run run

'''
