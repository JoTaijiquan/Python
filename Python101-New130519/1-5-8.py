#Python 3.7.3
#Example 1-5-8

def func_1_5_8():
    'การ copy list'
    
    a = [1,3,5,7,9]
    b = a
    c = a[:]
    
    print ("a =",a)
    print ("b =",b)
    print ("c =",c,"\n")
    a[2] = 11
    print ("a =",a)
    print ("b =",b)
    print ("c =",c,"\n")
    b.append(13)
    print ("a =",a)
    print ("b =",b)
    print ("c =",c)

if __name__ == "__main__":
    func_1_5_8()
