#Python 3.7.3
#Example 2-1-1

'มีเงินอยู่ 500 บาท ถ้าใช้เงินวันละ 10% ของจำนวนเงินที่มี ต้องใช้กี่วันถึงจะมีเงินเหลือน้อยกว่าครึ่งหนึ่งของเงินตั้งต้น'

def func_2_1_1():
    x=500
    y=500/2
    counter = 0
    print ("มีเงินตั้งต้น",x,"บาท" )
    while x>y:
        x=x-x*0.1
        counter+=1

        print ("วันที่",counter,"เหลือเงิน",x,"บาท")
    print ("\nสรุป ใช้เวลา",counter,"วัน")

if __name__=="__main__":
        print (__doc__,"\n")
        func_2_1_1()
