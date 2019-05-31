#Python 3.7.3

def func_1_7_5(x=10,y=20):
    print(x,y)

if __name__ == "__main__":
    func_1_7_5()
    func_1_7_5(100)
    func_1_7_5(y=100)
    func_1_7_5(y="hello",x=100)
    