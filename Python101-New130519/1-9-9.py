#Python 3.7.3
#Example 1-9-9

'inheritance'
 
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

if __name__ == "__main__":
    tom = Animal()
    tom.say()
    tom.say("Meow")
    print ("************")

    tweety = Bird()
    tweety.say()
    tweety.say("Tweet")
    tweety.sing()