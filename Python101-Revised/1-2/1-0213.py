'''
Create By Joompot Sriyapan
Date 7/4/2019

Name 
    Example 1.2.13
Description 
    multi-line command
Note
    ในกรณีที่คำสั่งยาวมากๆ แล้วอยากเขียนให้อยู่ในหลายๆ บรรทัด
    แทนที่จะเป็นบรรทัดเดียวยาวไปเรื่อยๆ สามารถใช้เครื่องหมาย \ 
    ในการต่อคำสั่งระหว่างบรรทัด

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
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.2.13
#Python 3.7.3

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