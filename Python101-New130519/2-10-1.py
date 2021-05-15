#Python 3.9.5
#Example 2-10-1

def gcd(n1,n2):
    'หารร่วมมาก(หรม.) greatest common divisor(gcd) สองจำนวน'
    
    while n2!=0:
        #print (n1,n2)
        n1,n2 = n2, n1%n2
    return n1

if __name__ == "__main__":
    print ("หรม. 5,3 =",gcd(5,3))
    print ("หรม. 8,2 =",gcd(8,2))
    print ("หรม. 2,8 =",gcd(2,8))
    print ("หรม. 6,8 =",gcd(6,8))
    print ("หรม. 35,77 =",gcd(35,77))
    print ("หรม. 625,50 =",gcd(625,50))
    print ("หรม. 72,21 =",gcd(72,21))
