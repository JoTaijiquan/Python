#Python 3.7.3
#Example 2-9-2

def factorize(num):
    'แยกตัวประกอบ'

    aList = []
    i=2
    while i<=num:
        if num%i==0:
            num=num/i
            aList.append(i)
            i=2
        else:
            i+=1
    return aList

if __name__ == "__main__":
    print (factorize(0))
    print (factorize(10))
    print (factorize(8))
    print (*factorize(16))
    print (*factorize(30))
    print ("factor of", str(2*3*7*2*5*11*11), \
    "is",*set(factorize(2*3*7*2*5*11*11)))
    print (' * '.join(map(str,factorize(99020)))," = 99020")
    print (' * '.join(map(str,factorize(990200))), " = 990200")
    print ("factor of 990200 is",set(factorize(990200)))
    
    