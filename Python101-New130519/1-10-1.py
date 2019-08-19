#Python 3.7.3
#Example 1-10-1

def func_1_10_1():
    'สร้าง และเขียนข้อมูลลงในไฟล์ ถ้ามีไฟล์ชื่อเดิมอยู่จะสร้างใหม่ทับไป'
    try:
        with open("test.txt","w") as f:
            f.write ("hello, world!")
            f.write ("123 456 789\n")
            print ("HELLO", file=f)
            print ("WORLD", file=f)
        print ("File Created!!!")
    except:
        print ("Cannot open file!!!")

if __name__ == "__main__":
    func_1_10_1()
