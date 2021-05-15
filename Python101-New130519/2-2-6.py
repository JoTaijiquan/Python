#Python 3.9.5
#Example 2-2-6

def draw_diamond(max=10):
    'ใช้ * วาดเป็นรูปเพชร'

    for i in range (max):
        counter = i+1
        space = " " * (max-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star)

    for i in range (max,1,-1):
        counter = i-1
        space = " " * (max-counter)
        star = "*" * counter + "*" * (counter-1)
        print (space+star)
        
if __name__=='__main__':
    draw_diamond()