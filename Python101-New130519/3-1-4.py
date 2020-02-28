#Python 3.8.1
#Example 3-1-4

from calendar import isleap

if __name__ == "__main__":
    x = 99
    while x != 0:
        x = int(input("Enter Year: (0 to exit) "))
        if isleap(x):
            print (f"{x} is leap year.")
        else:
            print (f"{x} is not leap year.")
