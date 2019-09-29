#Python 3.7.3
#Example 1-9-14
'Static variable'

class Hero:
    x = 0
    y = 10

    def __init__(self,name):
        print ("I'm",name)
        self.z = 20

    def change(self):
        self.x = "lalala"

    def changey(self):
        Hero.y = "aaaaa"
 
if __name__ == "__main__":
    superman = Hero("Superman")
    spiderman = Hero("Spiderman")
    ironman = Hero("ironman")

    superman.z = 30
    print (superman.z)
    print (spiderman.z)
    print (ironman.z)

    Hero.x = "Hahaha"
    superman.x = "0000"
    print (superman.x)
    print (spiderman.x)
    print (ironman.x)
    print (Hero.x)
    print ("******************")
    spiderman.change()
    print (superman.x)
    print (spiderman.x)
    print (ironman.x)
    print (Hero.x)
    Hero.x = "HOHOHOHO"
    print ("******************")
    print (superman.x)
    print (spiderman.x)
    print (ironman.x)
    print (Hero.x)

    print ("******************")
    superman.changey()
    print (superman.y)
    print (spiderman.y)
    print (ironman.y)
    print (Hero.y)
    