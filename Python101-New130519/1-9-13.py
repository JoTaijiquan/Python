#Python 3.7.3
#Example 1-9-13
 
class Animal():
    'Class Animal'
    def say(self):
        'Method Say'
        print ("hi")


if __name__ == "__main__":
    tom = Animal()
    tom.say()
    print ("************\n")

    print (Animal.__doc__)
    print (Animal.say.__doc__)
    print (Animal.__name__)
    print (Animal.say.__name__)