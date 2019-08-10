#Python 3.7.3
#Example 2-3-1

'Not complete yet*****************'

def prime(n):
    num = list(range(2,n))
    num.append(9999)
    j=-1
    try:
        while num[j]!=999:
            j+=1
            i=0
            while num[i]!=9999:
                i+=1
                if num[i]%num[j]==0:
                    num.remove(num[i])
    except:
        return num
        
    return num

if __name__ == "__main__":
    print (prime(97))