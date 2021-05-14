#Python 3.9.5
#Example 1-10-4

def func_1_10_4():
    'เขียนภาษาไทยลงในไฟล์'
    try:
        with open("test.txt",mode="r+",encoding="utf-8") as f:
            f.writelines("สวัสดี")
            print ("ชาวโลก",file=f)
            print ("***Current file position is",f.tell())
            f.seek(0)
            print ("***Set file position to",f.tell())
            print (f.readlines())
        print ("File Opened!!!")
    except:
        print ("Cannot open file")

if __name__ == "__main__":
    func_1_10_4()
