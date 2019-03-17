#Example 1.9.6
#Python 3.6.5
#Created By Jooompot Sriyapan

class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("I am a Cat")
    def __del__(self):
        print ("I am killed")

tom = Cat()
garfield = Cat()

tom.say()
garfield.say()

print ("---Kill tom---")
del tom

#tom.say()
garfield.say()

print ("---Kill garfield---")
del garfield

'''
เมื่อ
คราวนี้ลองอีกแบบ
tom = Cat() __init__ ทำงาน ได้ Aow
garfield = Cat() __init__ ก็ทำงาน ไ้ด Aow

กรณีนี้ garfield เป็นคนละ object กับ tom ไม่เกี่ยวกัน เพียงแต่ว่าเป็นชนิด class Cat() ด้วยกัน

tom.say() ก็ Meow
garfield.say() ก็ Meow

del tom __del__ ทำงาน ได้ I am killed

ดังนั้นถ้าสั่ง tom.say() ก็ error แน่ๆ
แต่ garfield.say() ยังได้ Meow

และสุดท้าย
del garfield  __del__ ทำงาน ได้ I am killed


แสดงผล
Aow
Aow
Meow
Meow
---Kill tom---
I am killed
Meow
---Kill garfield---
I am killed
'''
