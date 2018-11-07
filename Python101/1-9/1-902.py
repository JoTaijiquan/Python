#Example 9.02
#Python3.6.5

class Cat:
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")

tom = Cat()
tom.say()
tom.say()

'''
สมาชิกของ class Cat มีสองตัวละ
__new__(self) constructor
__init__(self) initialiser

แสดงผล
Aow
Meow
Meow
'''
