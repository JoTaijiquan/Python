#Python3.7.1

from random import randint,seed

def dice():
    seed()
    
    dice=[0,0,0,0,0,0]
    guess=[0,0,0,0,0,0]
    
    for i in range(100000):
        d=randint(1,6)
        j=d-1
        dice[j]=dice[j]+1

        g=randint(1,6)
        #g=1
        if g==d:
            j=g-1
            guess[j]=guess[j]+1
    print (dice,guess)

def lotto():
    seed()

    win=0

    for i in range(625):
        prize=randint(1,10000)
        buy =1000
        buy=randint(1,10000)
        if buy==prize:
            win=win+1

    return(win)
    
#dice()
x = 0

for i  in range(10000):
    x=x+lotto()

print(x)
print ("*")
