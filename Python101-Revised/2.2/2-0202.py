#Example 2.1.1
#Python 3.6.5
#Dice random dice.


def Dice():
    return random.randint(1,6)

if __name__=='__main__':

    for i in range (11,0,-1):
        print (" "*i,"*")

