#Example 2.05
#Python3.6.5

def example_205(): 
    Hello = 0
    print ("1)",Hello)

    Hello = "Hello!!!"
    print ("2)",Hello)

    Hello = Hello
    print ("3)",Hello)

    Hello = Hello+Hello
    print ("4)",Hello)

    Hello = "Hello!!!" 
    Hello = Hello*3
    print ("5)", Hello)
           
example_205()

'''
Hello = 0               กำหนดค่า Hello = 0
print ("1)",Hello)      แสดงผล 1) 0

Hello = "Hello!!!"      กำหนดค่า Hello = "Hello!!!"
print ("2)",Hello)      แสดงผล 2) Hello!!!

Hello = Hello           กำหนดค่า Hello = Hello ให้เท่ากับกตัวเองคือ Hello!!!
print ("3)",Hello)      แสดงผล 3) Hello!!!

Hello = Hello+Hello     กำหนดค่า Hello = Hello+Hello ได้ Hello!!!Hello!!!
print ("4)",Hello)      แสดงผล 4) Hello!!!Hello!!!

Hello = "Hello!!!"      กำหนดค่า Hello = "Hello!!!"
Hello = Hello*3         กำหนดค่า Hello = Hello x3 หรือ Hello 3 ครั้งต่อกัน
print ("5)", Hello)     แสดงผล 5) Hello!!!Hello!!!Hello!!!
'''
