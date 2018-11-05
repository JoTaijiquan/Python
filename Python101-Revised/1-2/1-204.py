#Example 2.04
#Python3.6.5

def example_204():
    a = 3+5
    b = True
    c = 999
    d = "ddd"
    e = "eee"
    f = "fff"

    print ("1) a b c =",a,b,c)

    a,b,c = b,c,a
    print ("2) a b c =",a,b,c,)

    a,b,c = d,e,f
    print ("3) a b c = ",a,b,c)

example_204()

'''
a = 3+5                         กำหนดค่า a = 3+5
b = True                        กำหนดค่า b = True
c = 999                         กำหนดค่า c = 999
d = "ddd"                       กำหนดค่า d = "ddd"
e = "eee"                       กำหนดค่า e = "eee"
f = "fff"                       กำหนดค่า f = "fff"

print ("1) a b c =",a,b,c)      แสดงผล 1) a b c = 8 True 999

a,b,c = b,c,a                   สลับค่า a b c กับ b c a 
print ("2) a b c =",a,b,c,)     แสดงผล 2) a b c = True 999 8

a,b,c = d,e,f                   กำหนดค่า a b c เป็น d e f
print ("3) a b c = ",a,b,c)     แสดงผล 3) a b c =  ddd eee fff
'''
