#Python 3.7.3
#Example 1-10-2

def func_1_10_2():
    'เปิดไฟล์ และเขียนข้อมูลเพิ่ม ถ้าไม่มีไฟล์เดิม จะสร้างใหม่ให้'
    try:
        with open("test.txt","a") as f:
            f.write ("Append")
            f.write ("!!!\n")
            print ("HELLO", file=f)
            print ("AGAIN", file=f)
        print ("File Appended!!!")
    except:
        print ("Cannot open file")

if __name__ == "__main__":
    func_1_10_2()
