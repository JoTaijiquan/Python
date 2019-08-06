#Python 3.7.3
#Example 2-4-1

def SelectionSort(num):
    'Selection Sort'
    
    for i in range(len(num)):
        min = i
        for j in range(i+1,len(num)):
            if num[min]>num[j]:
                min =j
        num[i],num[min]= num[min],num[i]
    return num

if __name__ == "__main__":
    num=[20,12,3,18,7,8,25,14]
    print ("Unsorted List = ",num)
    print ("Sorted List = ",SelectionSort(num))