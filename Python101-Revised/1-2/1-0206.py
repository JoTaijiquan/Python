#Example 1.2.6
#Python 3.6.5
#Created By Jooompot Sriyapan


def example_206():
    a,b,c = 1,3,5
    print ("1) ",a,b,c)
    print ("2) ",(a,b,c)*2)
    print ("3) ",(a,b,c)*3)
    print ("4)",a*1,b*2,c*3)

example_206()

'''
a,b,c = 1,3,5               กำหนดค่า a,b,c = 1,3,5 ตามลำดับ
print ("1) ",a,b,c)         แสดงผล 1)  1 3 5
print ("2) ",(a,b,c)*2)     แสดงผล 2)  (1, 3, 5, 1, 3, 5)
print ("3) ",(a,b,c)*3)     แสดงผล 3)  (1, 3, 5, 1, 3, 5, 1, 3, 5)
print ("4)",a*1,b*2,c*3)    แสดงผล 4) 1 6 15 มาจาก a*1, b*2, c*3 คือ 1x1, 3x2, 5x3
'''
