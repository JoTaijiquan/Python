#Python 3.9.5
#Example 2-10-2

def gcd(aList):
    'หารร่วมมาก(หรม.) greatest common divisor (gcd) หลายจำนวน'
    while len(aList)>1:        
        n1 = aList[0]
        n2 = aList[1]
        while n2!=0:
            n1,n2 = n2,n1%n2
        aList[1] = n1
        del aList[0]
    return n1

if __name__ == "__main__":

    print ("หรม 10,15,20,30 =",gcd([10,15,20,30]))
    print ("หรม 45,30,60,120 =",gcd([45,30,60,120]))
    print ("หรม 49,35,77,70 =",gcd([49,35,77,70]))
    print ("หรม 26,39 =",gcd([26,39]))
    
