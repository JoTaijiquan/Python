#Python 3.7.3
#Example 1-9-6

class Cat:
    '2 objects, 2 instances'

    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("I am a Cat")
    def __del__(self):
        print ("AAAAAAHHH")
 
if __name__ == "__main__":
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