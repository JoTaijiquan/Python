#Example 2.3.1
#Python 3.6.5
#Draw * hard code style.

if __name__=='__main__':
    loop = True
    
    while loop:
        x = input("ป้อนเลข 1-7 (ป้อน 0 เพื่อออกจากโปรแกรม) :")
        if x=="1":
            print ("สวัสดีวันอาทิตย์์")
        elif x=="2":
            print ("สวัสดีวันจันทร์")
        elif x=="3":
            print ("สวัสดีวันอังคาร")
        elif x=="4":
            print ("สวัสดีวันพุธ")
        elif x=="5":
            print ("สวัสดีวันพฤหัสบดี")
        elif x=="6":
            print ("สวัสดีวันศุกร์")
        elif x=="7":
            print ("สวัสดีวันเสาร์")
        elif x=="0":
            print ("ลาก่อน")
            loop = False
