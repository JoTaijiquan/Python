#Python 3.9.5
#Example 2-4-1

def compound_interest(deposit,interest,n):
    'หาผลรวมเงินต้นกับดอกเบี้ยทบต้น n รอบ'

    amount = []
    for i in range(n):
        deposit+=deposit*interest
        amount.append(deposit)
    return amount

if __name__ == "__main__":
    print (compound_interest(100,0.01,10))
    print ("\n")
    print (*compound_interest(100,0.01,10))
    print ("\n")
    print (*compound_interest(100,0.01,10),sep="\n")
    print ("\n")
    print ("เงินต้น 100 เพิ่มวันละ 1% เป็นเวลา 1ปี =")
    print (round(compound_interest(100,0.01,365)[-1],2))
    print ("เงินต้น 100 บาท ลดวันละ 1% เป็นเวลา 1ปี =") 
    print (round(compound_interest(100,-0.01,365)[-1],2))
    
     