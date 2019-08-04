#Python 3.7.3
#Example 1-9-12
 
class Animal:
    name = 'no name'
    action = 'no action'
    common_name = 'no common name'
    
    def say(self):
        print ("I am",self.name,",",self.action)
    def animal_say(self):
        print ("Animal say",Animal.name,",",Animal.action)


if __name__ == "__main__":
    print ("1)")  
    tom = Animal()
    print (tom.name,tom.action)
    print (Animal.name,Animal.action)
    tom.say()
    tom.animal_say()
    print ("************\n")

    print ("2)")  
    tom.name = "Tom"
    tom.action = "running"
    print (tom.name,tom.action)
    print (Animal.name,Animal.action)
    tom.say()
    tom.animal_say()
    print ("************\n")

    print ("3)")  
    Animal.name = "..."
    Animal.action = "..."
    jerry = Animal()
    tom.say()
    jerry.say()
    print (Animal.name,Animal.action)
    print ("************\n")

    print ("4)")  
    tom.animal_say()
    jerry.animal_say() 
