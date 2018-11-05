#Example 3.06
#Python3.6.5

def example_306():
    x=0
    
    while x!=10:
        x = input ("Input x ")
        x = int(x)
    
        if x==10:
            print ("Yes, you win x=10")
        elif x>10:
            print ("Too much, try again")
        elif x<10:
            print ("Too little, try again")

    print ("End Game!!!")

example_306()

'''
แสดงผล

Input x

ลองป้อน 5

Too little, try again
Input x

ลองป้อน 11

Too much, try again
Input x

ลองป้อน 10
Yes, you win x=10
End Game!!!

คำสั่ง while x!=10 คือคำสั่งวนรอบ ถ้า x!=10 (x ไม่เท่ากับ 10) ให้วนไปเรื่อยๆ 
'''
