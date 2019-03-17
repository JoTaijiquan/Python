#Example 1.9.3
#Python 3.6.5
#Created By Jooompot Sriyapan

class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("I am a Cat")

tom = Cat()
tom.say()
print (tom)

'''
__str__ เป็น method พิเศษตัวหนึ่ง เอาไว้ return ค่าของ object ออกมาตามที่เราต้องการ
ในกรณีนี้คือ เมื่อ สั่ง print(tom) 

ศัพท์ควรรู้

tom = Cat() คือการสร้าง object ชื่อ tom โดยมี class เป็น Cat()
จึงเรียก tom ว่า object นะครับ ไม่ใช่ class
และเรียก function ใน class ว่า method

แสดงผล
Aow
Meow
I am a Cat
'''
