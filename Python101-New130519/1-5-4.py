#Python 3.9.5
#Example 1-5-4

def func_1_5_4():
    'list ซ้อน list'
    
    a = [[3,4,5], 
        [6,7,8], 
        ['a','b','hello']]

    print (a)
    print (a[1])
    print (a[2][1])
    print (a[2][2][2])

if __name__ == "__main__":
    func_1_5_4()
