#Python 3.9.5
#Example 2-11-2

def BubbleSort(aList):
    'Bubble Sort'
    n= len(aList)
    for i in range(len(aList)):
        for j in range(0,n-i-1):
            if aList[j]>aList[j+1]:
                #print (aList)
                aList[j],aList[j+1]=aList[j+1],aList[j]          
    return aList

if __name__ == "__main__":
    aList=[20,12,3,18,7,8,25,14]
    print ("Unsorted List = ",aList)
    print ("Sorted List = ",BubbleSort(aList))