#Python 3.7.3
#Example 2-3-2

def factorize(num):
    'Factorize number'

    factor = []
    i=2
    while i<=num:
        if num%i==0:
            num=num/i
            factor.append(i)
            i=2
        else:
            i+=1
    return set(factor)

if __name__ == "__main__":
    print (factorize(10))
    print (factorize(8))
    print (factorize(16))
    print (factorize(30))
    print ("factorize of ", str(2*3*7*2*5*11*11), "is",*factorize(2*3*7*2*5*11*11))
    print (' * '.join(map(str,factorize(99020))), " = 99020")