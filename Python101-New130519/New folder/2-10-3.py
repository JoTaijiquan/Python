#Python 3.7.3
#Example 2-10-3

def gcd(aList):
    'หาค่าหารร่วมมาก greatest common diversor หรือ ครม ของสองจำนวน'
    
    while len(aList)>1:
        while aList[1]!=0:
            aList[0],aList[1] = aList[1],aList[0]%aList[1]
        del aList[1]
    return aList[0]

if __name__ == "__main__":
    print (gcd([10,15,20,30]))
    print (gcd([45,30,15,60]))
    print (gcd([49,35,77,70]))
    print (gcd([26,39]))
    
