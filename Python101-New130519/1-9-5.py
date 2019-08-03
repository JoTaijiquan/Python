#Python 3.7.3
#Example 1-9-5

class Cat:
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
    garfield = tom
    print ("--Object Created--")

    tom.say()
    garfield.say()

    print ("---Kill tom---")
    del tom

    #tom.say()
    garfield.say()

    print ("---Kill garfield---")
    del garfield
 