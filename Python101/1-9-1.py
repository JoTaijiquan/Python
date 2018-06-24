#Chapter 1.9

#Object Oriented Python

'''
#Example 9.00
class Cat:
    def say(self):
        return("Meow")
    
    
tom = Cat()
print (tom.say())
'''





'''
#Exampe 9.00
class Cat:
    def say(self):
        pass

garfield = Cat()

print (Cat())
print (Cat)
print (garfield)
garfield.say()
'''

'''
#Example 9.01
class Cat:
    def say(self):
        print ("Meow")
        
garfield = Cat()

garfield.say()
'''

'''
#Example 9.02
class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")

garfield = Cat()
garfield.say()
print (garfield)
'''

'''
#Example 9.03
class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("class Cat")

garfield = Cat()
garfield.say()
print (garfield)
'''

'''
#Example 9.04
class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("class Cat")
    def __del__(self):
        print ("class Cat Deleted!!!")

garfield = Cat()
garfield.say()
print (garfield)
print (Cat)
del garfield
#garfield.say()
'''

'''
#Example 9.05
class Cat:
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")
        
    def __str__(self):
        return ("class Cat")
        
    def __del__(self):
        print ("class Cat Deleted!!!")

garfield = Cat()
tom = garfield

garfield.say()
tom.say()
print (garfield)
print (tom)

print ("----- Delete garfield -----")
del garfield

print ("\n")
#print (garfield)
tom.say()
print (tom)

print ("----- Delete tom -----")
del tom
'''

'''
#Example 9.06
class Cat:
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")
        
    def __str__(self):
        return ("class Cat")
        
    def __del__(self):
        print ("class Cat Deleted!!!")

garfield = Cat()
tom = Cat()

print ("----- Delete garfield -----")
del garfield
print ("\n")

print ("----- Delete tom -----")
del tom
'''

'''
#Example 9.07
class Cat:
    color = ''
    name = ''
    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")
        
    def __str__(self):
        return ("class Cat")
        
    def __del__(self):
        print ("class Cat Deleted!!!")

g = Cat()
g.color = 'orange'
g.name = 'Garfield'
g.say()
print (g.name, g.color)
t = g
print (t.name,t.color)
t.color = 'B&W'
t.name = 'Tom'
print (t.name, t.color)
print (g.name, g.color)
del g
t.say()
del t
'''

'''
#Example 9.08
class Cat:
    color = 'White'
    name = 'John'
    
    def __init__(self):
        print ("Aow")
        
    def say(sefl,s="Meow"):
        print (s)
        
    def __str__(self):
        return ("class Cat")
        
    def __del__(self):
        print ("class Cat Deleted!!!")

g = Cat()
t = Cat()
print ('\n')

g.color = 'orange'
g.name = 'Garfield'
g.say ("Wooowwwww")
print (g.name, g.color)
print ("\n")

t.say()
print (t.name,t.color)
print ("\n")

t.color = 'B&W'
t.name = 'Tom'
print (t.name, t.color)
print (g.name, g.color)

print("\n")
del g
del t
'''

'''
#Example 9.09
class Cat:
    
    def __init__(self,n):
        print ('Aow!! I\'m',n)
        self.name = n
        
    def say(self):
        print ('I\'m the great',self.name)
        
    def __str__(self):
        return (self.name+' is class Cat')
        
    def __del__(self):
        print (self.name, 'is Killed!!!')


t = Cat('Tom')
t.say()
print (t.name)
print (t)
del t
'''

'''
#Example 9.10
class Animal:
    #name='...'
    def __init__(self,n,classes='bird',legs=2):
        self.name = n
        self.classes = classes
        self.legs = legs
        
    def say(self):
        print ('I\'m',self.name)

class Cat(Animal):
    def __init__(self):
        pass
'''   
    
'''        
class Cat:
    
    def __init__(self,n):
        print ('Aow!! I\'m',n)
        self.name = n
        
    def say(self):
        print ('I\'m the great', self.name)
        
    def __str__(self):
        return (self.name+' is class Cat')
        
    def __del__(self):
        print (self.name, 'is Killed!!!')
'''
'''
a = Animal(n='cat')
a.say()
b = Cat()
b.say()
'''


