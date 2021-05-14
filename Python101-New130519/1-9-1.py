#Python 3.9.5
#Example 1-9-1

class Cat:
    'Class name Cat'

    def say(self):
        'Method name say'
        print ("Meow")

if __name__ == "__main__":
    tom = Cat()
    tom.say()
    print ("*****************")
    print ("Type of tom is",type(tom))
    print ("Type of tom.say is",type(tom.say))
    print ("Class's doc is",tom.__doc__)
    print ("Method's doc is",tom.say.__doc__)
    