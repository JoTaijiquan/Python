#Example 1.9.12
#Python 3.6.5
#Created By Jooompot Sriyapan

class Animal:
    name = 'no name'
    action = 'no action'
    common_name = 'no common name'
    
    def say(self):
        print ("I am",self.name,",",self.action)
    def animal_say(self):
        print ("Animal say",Animal.name,",",Animal.action)

print ("1)")  
tom = Animal()
print (tom.name,tom.action)
print (Animal.name,Animal.action)
tom.say()
tom.animal_say()
print ("************\n")

print ("2)")  
tom.name = "Tom"
tom.action = "running"
print (tom.name,tom.action)
print (Animal.name,Animal.action)
tom.say()
tom.animal_say()
print ("************\n")

print ("3)")  
Animal.name = "..."
Animal.action = "..."
jerry = Animal()
tom.say()
jerry.say()
print (Animal.name,Animal.action)
print ("************\n")

print ("4)")  
tom.animal_say()
jerry.animal_say()

'''
ไม่อธิบาย ลองทำความเข้าใจจากตัวอย่าง

แสดงผล

1)
no name no action
no name no action
I am no name , no action
Animal say no name , no action
************

2)
Tom running
no name no action
I am Tom , running
Animal say no name , no action
************

3)
I am Tom , running
I am ... , ...
... ...
************

4)
Animal say ... , ...
Animal say ... , ...

'''
