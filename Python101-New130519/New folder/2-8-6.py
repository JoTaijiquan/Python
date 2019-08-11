#Python 3.7.3
#Example 2-8-6

def draw_diamond(max=10):
    'Draw diamond star'
    for i in range (max):
        counter = i+1
        space = " " * (max-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star,counter)

    for i in range (max,1,-1):
        counter = i-1
        space = " " * (max-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star,counter)
        
if __name__=='__main__':
    draw_diamond(10)