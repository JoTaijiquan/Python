#Python 3.7.3
#Example 1-9-7

class Cat:
    'parameter และ attribute'

    def __init__(self,n,c):
        self.name = n
        self.color = c
    def say(self):
        print ("My name is",self.name)
 
if __name__ == "__main__":
    tom = Cat("tom","B&W")
    tom.say()
    print (tom.color)
    tom.name = "TOM"
    tom.color = "Black & White"
    tom.say()
    print (tom.name,"is",tom.color)