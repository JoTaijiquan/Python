#Python 3.7.3
#Example 2-8-5

def draw_mirror_reverse_triangle(max=10):
    'Draw mirror triangle star'
    for i in range (0,max):
        counter = i
        space = " " * counter
        star = "*" * (max-counter)
        print (space+star)
        
if __name__=='__main__':
    draw_mirror_reverse_triangle(10)