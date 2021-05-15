#Python 3.9.5
#Example 2-10-3

def gcd(aList):
    'หารร่วมมาก(หรม.) greatest common divisor (gcd) หลายจำนวน'
    
    while len(aList)>1:
        while aList[1]!=0:
            aList[0],aList[1] = aList[1],aList[0]%aList[1]
        del aList[1]
    return aList[0]

if __name__ == "__main__":
    print ("หรม 10,15,20,30 =",gcd([10,15,20,30]))
    print ("หรม 45,30,120,60 =",gcd([45,30,120,60]))
    print ("หรม 49,35,77,70 =",gcd([49,35,77,70]))
    print ("หรม 26,39 =",gcd([26,39]))
    
