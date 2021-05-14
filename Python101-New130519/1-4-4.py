#Python 3.9.5
#Example 1-4-4

def func_1_4_4():
    'ตรวจสอบเงื่อนไขของวงรอบในคำสั่ง while'
    y = 2
    
    while y<10000:
        print ("y=",y)
        y*=2

if __name__ == "__main__":
    func_1_4_4()