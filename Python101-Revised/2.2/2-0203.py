#Example 2.2.3
#Python 3.6.5
#Draw * to the left

def draw(max_number=10):
    
    for i in range (max_number,0,-1):
        counter = i-1
        space = " " * counter
        star = "*" * (max_number-counter)
        print (space+star, counter)

    for i in range (1,max_number):
        counter = i
        space = " " * counter
        star = "*" * (max_number-counter)
        print (space+star, counter)

if __name__=='__main__':
    draw()
