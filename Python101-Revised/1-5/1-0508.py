'''
Create By Joompot Sriyapan
Date 20/4/2019

Name 
    Example 1.5.8
Description 
    list
Note
    sort, reverse
Display
1) a= [2, 3, 6, 1, 4, 8, 1, 5, 3]
2) b= [2, 3, 6, 1, 4, 8, 1, 5, 3] 

3) sorted a= [1, 1, 2, 3, 3, 4, 5, 6, 8]
4) b= [1, 1, 2, 3, 3, 4, 5, 6, 8] 

5) reversed b= [8, 6, 5, 4, 3, 3, 2, 1, 1]
6) a= [8, 6, 5, 4, 3, 3, 2, 1, 1]

7) c= [7, 3, 2, 3, 5, 4, 2, 2, 1, 8]
8) reversed c= [8, 1, 2, 2, 4, 5, 3, 2, 3, 7]
9) revresed c= [7, 3, 2, 3, 5, 4, 2, 2, 1, 8]
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.5.8
#Python 3.7.3

def example_508():
    a = [2,3,6,1,4,8,1,5,3]
    b = a
    c =[7,3,2,3,5,4,2,2,1,8]
    
    print ("1) a=",a)
    print ("2) b=",b,"\n")
    a.sort()
    print("3) sorted a=",a)
    print("4) b=",b,"\n")
    b.reverse()
    print("5) reversed b=",b)
    print("6) a=",a,end="\n\n")
    print ("7) c=",c)
    c.reverse()
    print ("8) reversed c=",c)
    c.reverse()
    print ("9) revresed c=",c)

example_508()

'''
sort()  เรียงค่าใน list จากน้อยไปมาก
reverse() สลับตำแหน่งค่าใน list จากหลังมาหน้า
ข้อสังเกตเมื่อกำหนดให้ b=a
เมื่อ a.sort() ค่าใน b ก็เปลี่ยนตามไปด้วย
และเมื่อ b.reverse() ค่าใน a ก็เปลี่ยนตามไปด้วยเช่นกัน

แสดงผล
1) a= [2, 3, 6, 1, 4, 8, 1, 5, 3]
2) b= [2, 3, 6, 1, 4, 8, 1, 5, 3] 

3) sorted a= [1, 1, 2, 3, 3, 4, 5, 6, 8]
4) b= [1, 1, 2, 3, 3, 4, 5, 6, 8] 

5) reversed b= [8, 6, 5, 4, 3, 3, 2, 1, 1]
6) a= [8, 6, 5, 4, 3, 3, 2, 1, 1]

7) c= [8, 7, 3, 2, 3, 5, 4, 2, 2, 1]
8) reversed c= [1, 2, 2, 4, 5, 3, 2, 3, 7, 8]
'''
