#Chapter 1.8

#Dictionary and Set

#Exampe 8.01
def example_801():
    x={ 'a': 'Hello',
        'b': 'World',
        'c': '!!!'
        }

    print (x)

#example_801()
###########################

#Example 8.02
def example_802():
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


#example_802()
###########################

#Example 8.03
def example_803():
        x={}

        x['A'] = 'Ada'
        x['B'] = 'Basic'
        x['C'] = 'Cobol'

        for first, second in x.items():
            print (first,second)

        if 'A' in x:
            print (x['A'])

        print (x.items())
        print ("number of item in x=",len(x.items()))

#example_803()
###########################

#Example 8.04
def example_804():
    x = set([3,5,7,8,3])
    y = x.copy()
    
    print ("1)",x,y)
    x.add(22)
    print ("2)",x,y)
    y.add(3)
    print ("3)",x,y)
    x.remove(3)
    print ("4)",x,y)

#example_804()
###########################
    
#Example 8.05
def example_805():
    x = set([5, 7, 8, 22])
    y = set([8, 3, 5, 7])
    print (x,y)
    print (x & y)
    print (y | x)

#example_805()
###########################

#Example 8.06
def example_806():
    x= set([3,5,7,9])
    y= set([1,3,5,7,9,11])

    print ("y is superset of x",y.issuperset(x))
    print ("x is subset of y",x.issubset(y))
    if x < y: print ("x<y")
 
#example_806()
###########################
