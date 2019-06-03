#Python 3.7.3
#Example 1-7-3

def func_1_7_3(x,y):
    'การเปลียนแปลงค่าตัวแปรในฟังก์ชันไม่ส่งผลต่อตัวแปรนอกฟังก์ชัน'

    x+=1
    y+=2
    print("func: x=",x," y=",y)

if __name__ == "__main__":
    x=10; y=20
    print("x=",x," y=",y)    
    func_1_7_3(x,y)
    print("x=",x," y=",y)