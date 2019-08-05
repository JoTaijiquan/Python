#Python 3.7.3
#Example 1-9-2

class Cat:
    'Initializer หรือ Constructor'

    def __init__(self):
        print ("Aow")
        
    def say(self):
        print ("Meow")

if __name__ == "__main__":
    tom = Cat()
    tom.say()
    tom.say()
    print()

    Cat()
    print()

    Cat().say()