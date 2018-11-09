#Example 9.13
#Python3.6.5

class Animal():
    'Class Animal'
    def say(self):
        'Function Say'
        print ("hi")
        
tom = Animal()
tom.say()
print ("************\n")

print (Animal.__doc__)
print (Animal.say.__doc__)
print (Animal.__name__)
print (Animal.say.__name__)

'''
ตัวอย่าง class ง่ายๆ ให้ดูการใช้งาน class document ซึ่งเขียนไว้บรรทัดแรกใต้ชื่อ class
หรือ function document ที่เขียนไว้บรรทัดแรกหลังชื่อ function หรือ method

เรียกใช้ได้ตามตัวอย่างเลย มี __doc__ กับ __name__

แสดงผล

hi
************

Class Animal
Function Say
Animal
say
'''
