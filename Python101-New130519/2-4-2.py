#Python 3.7.3
#Example 2-4-1

def BubbleSort(num):
    'Bubble Sort'
    n= len(num)
    for i in range(len(num)):
        for j in range(0,n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]            
    return num

if __name__ == "__main__":
    num=[20,12,3,18,7,8,25,14]
    print ("Unsorted List = ",num)
    print ("Sorted List = ",BubbleSort(num))