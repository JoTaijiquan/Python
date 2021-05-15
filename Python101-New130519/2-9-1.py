#Python 3.9.5
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
    print ("จำนวนเฉพาะที่น้อยกว่า 97 คือ",prime(97))
    print ("\n")
    print ("จำนวนเฉพาะที่น้อยกว่า 200 คือ",prime(200))