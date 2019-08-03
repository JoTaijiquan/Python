#Python 3.7.3
#Example 1-9-4

class Cat:
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("I am a Cat")
    def __del__(self):
        print ("I am killed")
 
if __name__ == "__main__":
    tom = Cat()
    tom.say()
    del tom
 