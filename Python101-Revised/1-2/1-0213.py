#Example 2.13
#Python3.6.5

def example_213():
    a = """Hello
World!"""
    b = "Hello!\nWorld."
    c = "Hello \
World"
    d \
      =5
    e= \
       6
    print ("1) ",a)
    print ("2) ",b)
    print ("3) ",c)
    print ("4) ",d)
    print ("5) ",e)

example_213() 

'''
ใช้ """ สามารถพิมพ์ string หลายบรรทัด
ใช้ \n สั่งขึ้นบรรทัดใหม่ใน string
ใช้ \ กรณีเขียนคำสั่งยาวๆ หลายบรรทัด

แสดงผล
1)  Hello
World!
2)  Hello!
World.
3)  Hello World
4)  5
5)  6
'''
