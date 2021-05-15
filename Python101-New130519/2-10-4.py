#Python 3.9.5
#Example 2-10-4

'หารร่วมมาก(หรม.) ด้วย math library'
import math

if __name__ == "__main__":
    print ("หรม. 5,3 =",math.gcd(5,3))
    print ("หรม. 2,8 =",math.gcd(2,8))
    print ("หรม. 6,8 =",math.gcd(6,8))
    print ("หรม. 35,77 =",math.gcd(35,77))
    print ("หรม. 625,50 =",math. gcd(625,50))
    print ("หรม. 49,35,77 =", \
        math.gcd(math.gcd(math.gcd(49,35),77),70))
        
