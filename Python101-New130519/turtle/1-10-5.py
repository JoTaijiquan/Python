#Python 3.7.3
#Example 1-10-5

import json

def func_1_10_5():

    'not complete yet....'
    x = {
        "name": "Khem",
        "age": 16,
        "book": [   
            {"name": "แฮรี่ พอตเตอร์", "price": 250},
            {"name": "ขายหัวเราะ", "price": 10}
            ],
        "name": "Kram",
        "age": 14,
        "book": [   
            {"name": "นารุโตะ", "price": 45}
            ]
        }

    try:
        with open("test3.txt","w") as f:
            json.dump(x,f)
            json.dump(x,f)
        print ("File Created!!!")
    except:
        print ("Cannot open file!!!")
    

if __name__ == "__main__":
    func_1_10_5()
