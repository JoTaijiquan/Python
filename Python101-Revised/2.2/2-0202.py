#Example 2.2.2
#Python 3.6.5
#Draw * to the right

def draw(max_number = 10):
    for i in range (max_number):
        counter = i+1
        star = "*" * counter
        print (star,counter)

    for i in range(max_number,1,-1):
        counter = i-1
        star = "*" * counter
        print (star,counter)

if __name__=='__main__':
    draw()
