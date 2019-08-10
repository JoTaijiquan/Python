#Python 3.7.3
#Example 2-3-1

def prime(n):
    'Create Prime Number List from 2 to n'
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