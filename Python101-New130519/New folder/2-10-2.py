#Python 3.7.3
#Example 2-10-2

def gcd(aList):
    'หาค่าหารร่วมมาก greatest common diversor หรือ ครม หลายจำนวน'
    while len(aList)>1:        
        n1 = aList[0]
        n2 = aList[1]
        while n2!=0:
            n1,n2 = n2,n1%n2
        aList[1] = n1
        del aList[0]
    return n1

if __name__ == "__main__":
    print (gcd([10,15,20,30]))
    print (gcd([45,30,15,60]))
    print (gcd([49,35,77,70]))
    print (gcd([26,39]))
    
