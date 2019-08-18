#Python 3.7.3
#Example 2-2-5

def draw_mirror_upside_triangle(max=10):
    'ใช้ * วาดเป็นสามเหลี่ยมกลับด้านและกลับหัว'

    for i in range (0,max):
        counter = i
        space = " " * counter
        star = "*" * (max-counter)
        print (space+star)
        
if __name__=='__main__':
    draw_mirror_upside_triangle()