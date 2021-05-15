#Python 3.9.5
#Example 2-10-6

def gcd(n1,n2):
    'หารร่วมมาก(หรม.) สองจำนวน'
    while n2!=0:
        n1,n2 = n2, n1%n2
    return n1

def lcm(aList):
    'คูณร่วมน้อย(ครน.) หลายจำนวน'
    ans = aList[0]
    for i in aList[1:]:
        ans = int(ans*i/gcd(ans,i))
    return ans

if __name__ == "__main__":
    print ("ครน.20,30,40,5=",lcm([20,30,40,5]))
    print ("ครน.3,7,3=",lcm([3,7,2]))
    print("ครน.15,30,45,60=",lcm([15,30,45,60]))
    print("ครน.2,5,10,12=",lcm([2,5,10,12]))  


