#Python 3.7.3
#Example 1-9-10

'method overriding'
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

if __name__ == "__main__":
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