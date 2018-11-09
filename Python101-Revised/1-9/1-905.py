#Example 9.05
#Python3.6.5

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
garfield = tom
print ("--Object Created--")

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
tom = Cat() สังเกตว่า Initializer ทำงาน print("Aow")
garfield = tom ไม่มีอะไรเกิดขึ้น

tom.say()  ก็ Meow
garfield.say() ก็ Meow เหมือนกัน

del tom ไม่เกิดอะไรขึ้นครับ เนื่องจากถึงแม้ tom จะตายไป แต่ garfield ยังอยู่

#.tom.say() เอา # วางไว้เพื่อไม่ให้คำสั่งนี้ทำงาน เพราะถ้าสั่ง tom.say() จะ error (ลองดูได้)

garfield.say() ได้ Meow ตามปกติ

del garfield คราวนี้ตายจริง คำสั่ง __del__(self) ทำงาน แสดงผล I am killed


แสดงผล
Aow
--Object Created--
Meow
Meow
---Kill tom---
Meow
---Kill garfield---
I am killed
'''
