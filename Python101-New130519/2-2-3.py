#Python 3.9.5
#Example 2-2-3

def draw_upside_triangle(max=10):
    'ใช้ * วาดเป็นสามเหลี่ยมกลับหัว'

    for i in range(max,0,-1):
        counter = i
        star = "*" * counter
        print (star)
        
if __name__=='__main__':
    draw_upside_triangle()