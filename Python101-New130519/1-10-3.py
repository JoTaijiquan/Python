#Python 3.9.5
#Example 1-10-3

def func_1_10_3():
    'อ่านไฟล์'
    try:
        with open("test.txt","r") as f:
            a = f.readline()
            print (a)
            print (f.readlines())
            print ("***Current file position is",f.tell())
            f.seek(0)
            print ("***Set current file position to",f.tell())
            print (f.readlines())
            f.seek(3)
            print ("***Set current file position to",f.tell())
            print (f.readline())
            print ("***Current file position is",f.tell())
        print ("File Read!!!")
    except:
        print ("Cannot open file")

if __name__ == "__main__":
    func_1_10_3()
