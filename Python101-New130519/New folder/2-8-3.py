#Python 3.7.3
#Example 2-8-3

def draw_reverse_triangle(max=10):
    'Draw reverse triangle star'
    for i in range(max,0,-1):
        counter = i
        star = "*" * counter
        print (star)
        
if __name__=='__main__':
    draw_reverse_triangle(10)