#Python 3.9.5
#Example 1-7-5

def func_1_7_5(x=10,y=20):
    'การกำหนดค่าเริ่มต้นให้กับตัวแปร parameter ของฟังก์ชัน'

    print(x,y)

if __name__ == "__main__":
    func_1_7_5()
    func_1_7_5(100)
    func_1_7_5(y=100)
    func_1_7_5(y="hello",x=100)
    