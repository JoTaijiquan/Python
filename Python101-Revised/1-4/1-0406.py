'''
Create By Joompot Sriyapan
Date 14/4/2019

Name 
    Example 1.4.6
Description 
    for loop
Note
เมื่อ i มีค่าเท่ากับ 5 ให้เอา i=i+3  ได้ 8 แล้วไปแสดงผล
ดังนั้นค่าที่แสดงจะกระโดด 0 1 2 3 4 8 (5+3) แล้วจึงค่อยเป็น 6
Display
0
1
2
3
4
8
6
7
8
9
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.4.6
#Python 3.7.3

def example_406():
    for i in range(10):
        if i==5:
            i=i+3
        print (i)

example_406()
