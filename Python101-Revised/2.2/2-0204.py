#Example 2.2.4
#Python 3.6.5
#Draw * to both side.


def draw(max_number=10):    
    for i in range (max_number):
        counter = i+1
        space = " " * (max_number-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star,counter)

    for i in range (max_number,1,-1):
        counter = i-1
        space = " " * (max_number-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star,counter)

if __name__=='__main__':
    draw()
