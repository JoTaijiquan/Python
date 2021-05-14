#Python 3.9.5
#Example 1-9-3

class Cat:
    'คืนค่า string ออกมาจาก object'
    
    def __init__(self):
        print ("Aow")
    def say(self):
        print ("Meow")
    def __str__(self):
        return ("I am a Cat")
 
if __name__ == "__main__":
    tom = Cat()
    tom.say()
    print (tom)
 