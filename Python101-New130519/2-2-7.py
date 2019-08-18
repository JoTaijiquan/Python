#Python 3.7.3
#Example 2-2-7

def print_line(counter,max):
    'แสดงผล * แต่ละแถว'

    space = " " * (max-counter)
    star = "*" * counter + "*" * (counter-1)
    print (space+star)

def draw_diamond(max=10):
    'ใช้ * วาดเป็นรูปเพชร'

    for i in range (max):
        counter = i+1
        print_line(counter,max)

    for i in range (max,1,-1):
        counter = i-1
        print_line(counter,max)

if __name__=='__main__':
    draw_diamond()