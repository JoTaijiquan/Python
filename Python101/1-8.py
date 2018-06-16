#Chapter 1.8

#Dictionary

#Exampe 8.00
def example_800():
    x={ 'a': 'Hello',
        'b': 'World',
        'c': '!!!'
        }

    print (x)

#example_800()

def example_801():
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


example_801()
        
