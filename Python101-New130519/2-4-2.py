#Python 3.7.3
#Example 2-4-2

def compound_int1(deposit,interest,n):
    'หาผลรวมเงินต้นกับดอกเบี้ยทบต้น n รอบ'
    for i in range(n):
        deposit+=deposit*interest
    return round(deposit,3)

def compound_int2(deposit,interest,n):
    'หาผลรวมเงินต้นกับดอกเบี้ยทบต้นจากสูตร PV*(1+i)**n'
    return round(deposit *(1+interest)**n,3)

if __name__ == "__main__":
    print ("เงินต้น 100 บาท เพิ่มวันละ 1% เป็นเวลา 1ปี (loop)=",compound_int1(100,0.01,365))
    print ("เงินต้น 100 บาท  เพิ่มวันละ 1% เป็นเวลา 1ปี (สูตร)=",compound_int2(100,0.01,365))
    print("\n")
    print ("เงินต้น 100 บาท ลดวันละ 1% เป็นเวลา 1ปี (loop)=",compound_int1(100,-0.01,365))
    print ("เงินต้น 100 บาท ลดวันละ 1% เป็นเวลา 1ปี (สูตร)=",compound_int2(100,-0.01,365))
    
    compound_int3=lambda deposit,interest,n: round(deposit*(1+interest)**n,3)
    print ("เงินต้น 100 บาท ลดวันละ 1% เป็นเวลา 1ปี (lambda)=",compound_int3(100,-0.01,365))