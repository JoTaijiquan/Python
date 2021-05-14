#Python 3.9.5
#Example 1-7-8

def func_1_7_8(x,y):
    'ฟัง์ชันหนึ่ง มี return จากหลายจุดได้'

    if x>y:
        return x
    elif x<y:
        return y
    else:
        return "x=y!!"

if __name__ == "__main__":
    print(func_1_7_8(10,20))
    print(func_1_7_8(9,1))
    print(func_1_7_8(100,100))