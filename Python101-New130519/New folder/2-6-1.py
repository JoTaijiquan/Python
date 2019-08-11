#Python 3.7.3
#Example 2-6-1

def compound_interest(deposit,interest,round):
    'หาผลรวมดอกเบี้ยทบต้น'
    amount = []
    for i in range(round):
        deposit+=deposit*interest
        amount.append(deposit)

    return amount

if __name__ == "__main__":
    #print (*compound_interest(100,0.01,10),sep="\n")
    print (compound_interest(100,0.01,10))
    print ("\n")
    print (*compound_interest(100,0.01,10))
    print ("\n")
    print (*compound_interest(100,0.01,10),sep="\n")
    
     