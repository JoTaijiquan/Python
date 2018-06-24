class Person(object):
    """A simple class.""" # docstring
    species = "Homo Sapiens" # class attribute

    def __init__(self, name): # special method
        """This is the initializer. It's a special
method (see below).
"""
        self.name = name # instance attribute

    def __str__(self): # special method
        """This method is run when Python tries
        to cast the object to a string.Return
this string
        when using print(), etc.
"""
        return self.name

    def rename(self, renamed): # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))

class Animal:
    def __init__(self, name="Cat"):
        self.name = name
    def say(self):
        return (self.name)
        
class Cat(Animal):
    def say(self):
        return (self.name+" Meow")

a = Animal()
b = Cat()
#a = Cat("AAA")
#b = Animal("BBB")
print (b.say())
print (a.say())
print (a.name)
print (b.name)
b.name = "Dog"
print (b.say())

'''
a = Person("Jo")
print (a)
a.rename("Bo")
print (a)
print (a.__class__)
'''
