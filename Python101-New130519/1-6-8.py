#Python 3.7.3
#Example 1-6-8

def func_1_6_8():
    'try กับ except เพื่อดักการเกิด error'

    x = [1,2,3,4]
    try:
        print (x[2])
    except:
        print ("Ha Ha Ha")
    finally:
        print ("Ho Ho Ho")
        
    try:
        print (x[5])
    except:
        print ("Error x is out of range")
    finally:
        print ("Ho Ho Ho")
    
if __name__ == "__main__":
    func_1_6_8()
