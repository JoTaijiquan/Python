#Python 3.7.3
#Example 1-8-4

def func_1_8_4():
    'เซ็ต'

    x = set((3,5,7,8,3,8,3))
    y = x.copy()
    
    print ("1)",x,y)
    x.add(22)
    print ("2)",x,y)
    y.add(3)
    print ("3)",x,y)
    x.remove(3)
    print ("4)",x,y)

if __name__ == "__main__":
    func_1_8_4()