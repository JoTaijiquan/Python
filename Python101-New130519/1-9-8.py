#Python 3.7.3
#Example 1-9-8
 
class Animal:
    def __init__(self,common_name='Cat'):
        self.common_name = common_name
    def say(self):
        print ("I am",self.common_name)

if __name__ == "__main__":
    tom = Animal()
    tom.say()
    tweety = Animal("Bird")
    tweety.say()
