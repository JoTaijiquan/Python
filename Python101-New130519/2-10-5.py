#Python 3.9.5
#Example 2-10-5

def gcd(n1,n2):
    'หารร่วมมาก(หรม.) สองจำนวน'
    while n2!=0:
        n1,n2 = n2, n1%n2
    return n1

def lcm(n1,n2):
    'คูณร่วมน้อย(ครม.) least common multiple (lcm) สองจำนวน'
    return int(n1*n2/gcd(n1,n2))

if __name__ == "__main__":
    print ("ครน. 20,30 =",lcm(20,30))
    print ("ครน. 3,7 =",lcm(3,7))
    print("ครน. 15,30 =",lcm(15,30))

