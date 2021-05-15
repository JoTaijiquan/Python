#Python 3.9.5
#Example 2-2-2

def draw_triangle(max=10):
    'ใช้ * วาดเป็นสามเหลี่ยม โดยใช้ loop'

    for i in range (max):
        counter = i+1
        star = "*" * counter
        print (star)
    
if __name__=='__main__':
    draw_triangle()