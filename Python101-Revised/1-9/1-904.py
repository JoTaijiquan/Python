#Example 9.04
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
tom.say()
del tom

'''
ทฤษฎียาว อย่าคิดมาก เรียก method __del__ ง่ายๆ ว่า destructor ได้
คือเป็น function ที่จะทำงานอัตโนมัตเมื่อมีการลบ object นั้น

ในกรณีนี้ __del__(self) ทำงาน เมื่อ
del tom

ซึ่งเป็นการสั่งลบ object tom


แสดงผล
Aow
Meow
I am killed
'''
