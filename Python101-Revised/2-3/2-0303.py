#Example 2.3.3
#Python 3.6.5
#Draw * hard code style.

class wordclass:
        word = {
        "1":"สวัสดีวันอาทิตย์",
        "2":"สวัสดีวันจันทร์์",
        "3":"สวัสดีวันอังคาร",
        "4":"สวัสดีวันพุธ",
        "5":"สวัสดีวันพฤหัสบดี",
        "6":"สวัสดีวันศุกร์",
        "7":"สวัสดีวันเสาร์",
        "000":"ลาก่อน"   
    }

    

if __name__=='__main__':
    loop = True

    w = wordclass()
    while loop:
        x = input("ป้อนเลข 1-7 (ป้อน 0 เพื่อออกจากโปรแกรม) :")
        if x in w.word:
            print (w.word[x])
        elif x == "0":
            print (w.word["000"])
            loop = False
        
