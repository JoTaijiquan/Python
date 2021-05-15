#Python 3.9.5
#Example 2-11-1

def SelectionSort(aList):
    'Selection Sort'
    
    for i in range(len(aList)):
        min = i
        for j in range(i+1,len(aList)):
            if aList[min]>aList[j]:
                min =j
        #print (aList)        
        aList[i],aList[min]= aList[min],aList[i]
    return aList

if __name__ == "__main__":
    aList=[20,12,3,18,7,8,25,14]
    print ("Unsorted List = ",aList)
    print ("Sorted List = ",SelectionSort(aList))