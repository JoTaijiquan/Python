#Chapter 1.9

#Object Oriented Python

'''
#Example 9.01
class Cat:
    def say(self):
        print ("Meow")
        
tom = Cat()
tom.say()

###########################
'''

'''
#Example 9.02
class Cat:
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")

tom = Cat()
tom.say()

###########################
'''

'''
#Example 9.03
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

###########################
'''

'''
#Example 9.04
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

###########################
'''

'''
#Example 9.05
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

tom.say()
garfield.say()

print ("---Kill tom---")
del tom

#tom.say()
garfield.say()

print ("---Kill garfield---")
del garfield

###########################
'''

'''
#Example 9.06
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

###########################
'''

'''
#Example 9.07
class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def say(self):
        print ("My name is",self.name)

tom = Cat("tom","B&W")
tom.say()
print (tom.color)
tom.name = "Tom"
tom.color = "Black & White"
tom.say()
print (tom.name,"is",tom.color)

###########################
'''

'''
#Example 9.08
class Animal:
    def __init__(self,common_name='Cat'):
        self.common_name = common_name
    def say(self):
        print ("I am",self.common_name)

tom = Animal()
tom.say()
tweety = Animal("bird")
tweety.say()

###########################
'''

'''
#Example 9.09
class Animal:
    def __init__(self,common_name='cat'):
        self.common_name = common_name
    def say(self,say='...'):
        print ("I am",self.common_name,say)

class Bird(Animal):
    def __init__(self):
        self.common_name = 'bird'
    def sing(self):
        print ("tweet tweet tweety")
    
tom = Animal()
tom.say()
tom.say("Meow")
print ("************")

tweety = Bird()
tweety.say()
tweety.say("Tweet")
tweety.sing()

###########################
'''

'''
#Example 9.10
class Animal:
    def __init__(self,common_name='animal'):
        self.common_name = common_name
    def say(self,words='...'):
        print ("I am",self.common_name,words)

class Bird(Animal):
    def __init__(self):
        self.common_name = 'bird'
    def sing(self):
        print ("tweet tweet tweety")

class Cat(Animal):
    def __init__(self):
        self.common_name = 'cat'
    def say(self):
        print ("Meow")

tom = Animal()
tom.say()
tom.say("ha ha ha")
print ("************\n")

tweety = Bird()
tweety.say()
tweety.sing()
print ("************\n")

garfield = Cat()
garfield.say()
print (garfield.common_name)

###########################
'''
'''
#Example 9.11
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

###########################
'''

'''
#Example 9.12
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

###########################
'''

'''
#Example 9.13
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

###########################
'''

