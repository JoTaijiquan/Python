#Python 3.9.5
#Example 2-2-4

def draw_mirror_triangle(max=10):
    'ใช้ * วาดเป็นสามเหลี่ยมกลับด้าน'

    for i in range (max,0,-1):
        counter = i-1
        space = " " * counter
        star = "*" * (max-counter)
        print (space+star)
        
if __name__=='__main__':
    draw_mirror_triangle()