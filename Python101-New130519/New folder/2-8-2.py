#Python 3.7.3
#Example 2-8-2

def draw_triangle(max=10):
    'Draw triangle *'
    for i in range (max):
        counter = i+1
        star = "*" * counter
        print (star)
    
if __name__=='__main__':
    draw_triangle(10)