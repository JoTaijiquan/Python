#Python 3.7.3

def func_1_8_2():
    'Dictionary'
    x={ 'Jo': '123 Bangkok',
        'Mo': '456 Nonthaburi',
        'Yo': '789 Chiangmai'
        }

    for name,address in x.items():
        print (name,address)
        
    del x['Jo']
    print ('\n--- Delete Key Jo ---\n')

    for name,address in x.items():
        print (name,address)

    x['Go'] = '200 Chiangrai'
    x['Do'] = '321 Lumpoon'
    print ('\n--- Add Key Go and Do ---\n')

    for name,address in x.items():
        print (name,address)

if __name__ == "__main__":
    func_1_8_2()
