#Example 9.08
#Python3.6.5

class Animal:
    def __init__(self,common_name='Cat'):
        self.common_name = common_name
    def say(self):
        print ("I am",self.common_name)

tom = Animal()
tom.say()
tweety = Animal("Bird")
tweety.say()



'''
กำหนดค่าตั้งต้นให้กับ parameter ที่ส่งเข้าไปที่ class ได้

tom = Animal()
tom.say()  ก็เลยได้ I am Cat

tweety = Animal("Bird")
tweety.say() ได้ I am Bird เข้าใจไม่ยาก


แสดงผล
I am Cat
I am Bird
'''
