#Python 3.9.5
#Example 1-7-4

def func_1_7_4(x):
    'การส่งค่าตัวแปร list เข้าไปในฟังก์ชัน'

    x[0] +=10
    print ("Now x=",x)

if __name__ == "__main__":
    x=[10]
    print ("x=",x)
    func_1_7_4(x)
    print ("x=",x)
    func_1_7_4(x)