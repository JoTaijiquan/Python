#Python 3.7.3
#Example 1-3-1

def func_1_3_1():
    'คำสั่ง input รับข้อมูลจากคีย์บอร์ด'

    x = input ("Input x ")
    print ("x=",x)
    print ("x=",x,type(x))
    print ("x+3 =",x+"3")
    x = int(x)
    print ("int(x) =",x,type(x))
    print ("x+3 =",x+3)
    x = float(x)
    print ("float(x) =",x,type(x))
    print ("x+3 =",x+3)

if __name__ == "__main__":
    func_1_3_1()