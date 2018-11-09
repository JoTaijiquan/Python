#Example 3.04
#Python3.6.5

def example_304():
    x = input("Input x (guess 1-10) ")

    if x=="10":
        print ("Yes, you win x=10")
    elif x=="11":
        print ("Very close, try again (try 10)")
    else:
        print ("Noooo, try again (try 11)")

example_304()

'''
แสดงผล

Input x (guess 1-10)
ลองป้อน 1
Noooo, try again (try 11)

สั่ง Run อีกที
Input x (guess 1-10)
ลองป้อน 11
Very close, try again (try 10)

สั่ง Run อีกที
Input x (guess 1-10)
ลองป้อน 10
Yes, you win x=10
'''
