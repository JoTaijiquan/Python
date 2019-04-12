'''
Create By Joompot Sriyapan
Date 5/4/2019

Name 
    Example 1.1.5
Description 
    end=
Note
    print (1,2,3)               แสดงผล 1 2 3
    print (4,5,6)               แสดงผล 4 5 6

    print (7,8,9,end="")        แสดงผล 7 8 9
    print (10,11,12)            แสดงผล 7 8 910 11 12 (ต่อจากบรรทัดบนโดยไม่ขึ้นบรรทัดใหม่)

    print (1,2,3,end="-")       แสดงผล 1 2 3
    print (4,5,6)               แสดงผล 1 2 3-4 5 6 (ต่อจากบรรทัดบน คั่นด้วย -)
    print ()                    แสดงผล เว้นบรรทัด

    print (1,2,3,end="\n")      แสดงผล 1 2 3
    print (4,5,6,end="\n\n")    แสดงผล 4 5 6 เว้นหนึ่งบรรทัด
    print (7,8,9,end="\n\n\n")  แสดงผล 7 8 9 เว้นสองบรรทัด
    print (10)                  แสดงผล 10
Display
    1 2 3
    4 5 6
    7 8 910 11 12
    1 2 3-4 5 6

    1 2 3
    4 5 6

    7 8 9


    10
Required
    python 3.7.3
Pre-programmed
    -
'''

#Example 1.1.5
#Python 3.7.3

print (1,2,3)
print (4,5,6)

print (7,8,9,end="")
print (10,11,12)

print (1,2,3,end="-")
print (4,5,6)
print ()

print (1,2,3,end="\n")
print (4,5,6,end="\n\n")
print (7,8,9,end="\n\n\n")
print (10)

