#Example 1.4.14
#Python 3.6.5
#Created By Jooompot Sriyapan

def example_414():
    while (True):
        x = input("Input 1-10 (10 to Break) ")
        if x== "10":
            print ("End Loop")
            break
        else:
            print ("x = ",x)
    #Can use Ctrl-C or Ctrl-D to break loop

example_414()

'''
while (True): เป็นจริงตลอดกาล จึงวนรอบไปเรื่อยๆ
ออกจากวนรอบได้เมื่อเจอคำสั่ง break
หรือกดปุ่ม Ctrl-C หรือ Ctrl-D เพื่อหยุดลูป (การวนรอบ)
    
แสดงผล
Input 1-10 (10 to Break) 5
x =  5
Input 1-10 (10 to Break) 7
x =  7
Input 1-10 (10 to Break) 10
End Loop
'''
