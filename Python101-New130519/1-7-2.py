#Python 3.9.5
#Example 1-7-2

def func_1_7_2(x,y):
    'ส่งค่าเข้าไปในฟังก์ชันสองตัว'

    print("x =",x)
    print("y =",y)
    print()

if __name__ == "__main__":
    func_1_7_2(10,20)
    func_1_7_2(10,"hello")
    func_1_7_2([123],(10,20,30))
    a = 10; b = 20
    func_1_7_2(a,b)

    
