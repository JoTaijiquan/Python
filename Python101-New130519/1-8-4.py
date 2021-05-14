#Python 3.9.5
#Example 1-8-4

def func_1_8_4():
    'การอ่านและนับค่าใน dictionary'
    x={}

    x['A'] = 'Ada'
    x['B'] = 'Basic'
    x['C'] = 'Cobol'

    for first, second in x.items():
        print (first,second)
        
    print ("***************")
    if 'A' in x:
        print ("A for",x['A'])
            
    print ("***************")
    print(x)
    print (x.items())
    print ("number of item in x=",len(x.items()))

if __name__ == "__main__":
    func_1_8_4()