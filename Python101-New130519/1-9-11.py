#Python 3.7.3
#Example 1-9-11

'multiple inheritance'
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


if __name__ == "__main__":
    tom = Cat()
    print (tom.common_name)
    tom.dance()
    print ("************\n")
    tom.say("ha ha ha")
    tom.walk()
    tom.run()
    