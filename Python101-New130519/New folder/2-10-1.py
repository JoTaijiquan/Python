#Python 3.7.3
#Example 2-10-1

def gcd(n1,n2):
    'หาค่าหารร่วมมาก greatest common diversor หรือ ครม ของสองจำนวน'
    
    while n2!=0:
        n1,n2 = n2, n1%n2
    return n1

if __name__ == "__main__":
    print (gcd(5,3))
    print (gcd(2,8))
    print (gcd(6,8))
    print (gcd(35,77))
    print (gcd(625,50))