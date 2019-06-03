#Python 3.7.3
#Example 1-7-7

def func_1_7_7(x,y,z):
    'return ค่าหลายๆ ตัวเป็น tuple'
    
    return(x,y,z)

if __name__ == "__main__":
    print(func_1_7_7(1,10,20))
    print(func_1_7_7((1,2),[3,4],"hello"))
