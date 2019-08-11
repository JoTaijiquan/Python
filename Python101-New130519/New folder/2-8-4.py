#Python 3.7.3
#Example 2-8-4

def draw_mirror_triangle(max=10):
    'Draw mirror triangle star'
    for i in range (max,0,-1):
        counter = i-1
        space = " " * counter
        star = "*" * (max-counter)
        print (space+star)
        
if __name__=='__main__':
    draw_mirror_triangle(10)