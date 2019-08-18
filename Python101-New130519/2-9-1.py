#Python 3.7.3
#Example 2-9-1

def prime(n):
    'หาจำนวนเฉพาะตั้งแต่ 2 ถึง n'
    
    aList=[2]
    for num in range(n):
        if num>1:
            for i in range(2,num):
                if num%i ==0:
                    break
                elif i==num-1:
                    aList.append(num) 
    return aList

if __name__ == "__main__":
    print (prime(97))
    print (prime(200))