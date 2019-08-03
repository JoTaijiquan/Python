#Example 1.9.7
#Python 3.6.5
#Created By Jooompot Sriyapan

class Cat:
    def __init__(self,n,c):
        self.name = n
        self.color = c
    def say(self):
        print ("My name is",self.name)

tom = Cat("tom","B&W")
tom.say()
print (tom.color)
tom.name = "Tom"
tom.color = "Black & White"
tom.say()
print (tom.name,"is",tom.color)



'''
มีการส่ง parameter หรือส่งค่า ตอนสร้าง ojbject ด้วยก็ได้
โดยกำหนดค่าที่จะส่งไว้ที่ __init__(self,n,c) ส่งค่าเข้ามาสองตัวไว้ที่ n กับ c

self.name = n
self.color = c
สองบรรทัดนี้เป็นการกำหนดค่าที่เรียกว่า attribute ของ class หรือว่าง่ายๆ คือ
ตัวแปรในระบบของ class ละ ทฤษฎีไว้ทีหลัง มาดูวิธีใช้เลย


tom = Cat("tom","B&W") ส่งค่า tom และ B&W เข้าไปในตัวแปร n และ c
ซึ่งใน __init__ ก็จะกำหนด self.name = n และ self.color = c

tom.say() method say() ทำงาน จะได้ My name is tom โดยเอาค่าใน self.name มาแสดง
print(tom.color) ได้ B&W  จะเห็นว่าสามารถเรียกใช้ attribute หรือตัวแปร color ได้โดยตรงเลย
tom.name = "Tom" กำหนดค่าใหม่ให้ tom.name = "Tom" T ตัวใหญ่
tom.color = "Black & White" กำหนดค่าใหม่ให้ tom.color = "Black & White"
tom.say() ได้ My name is Tom จะเห็นว่า tom.name กลายเป็น Tom ละ

print (tom.name, "is", tom.color) ได้ Tom is Black & White 

แสดงผล
My name is tom
B&W
My name is Tom
Tom is Black & White
'''
