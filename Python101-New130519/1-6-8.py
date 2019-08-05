#Python 3.7.3
#Example 1-6-8

def func_1_6_8():
    'try กับ except เพื่อดักการเกิด error'

    x = [1,2,3]
    try:
        print (x[2])
    except:
        print ("Ha Ha Ha")
        
    try:
        print (x[6])
    except:
        print ("Error x is out of range")
    
if __name__ == "__main__":
    func_1_6_8()
