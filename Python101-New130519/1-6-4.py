#Python 3.9.5
#Example 1-6-4

def func_1_6_4():
    'ใช้ break เพื่อหยุดการทำงานของ for'

    for i in (1,3,5,7,8,9,10):
        print (i)
        if i==5:
            break
        else:
            pass
    print ("end at",i)
    
if __name__ == "__main__":
    func_1_6_4()
