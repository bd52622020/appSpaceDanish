#!/usr/bin/env python

 
 
def checkifkeyexists(key):
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    if key in d:
        print("This Key is in the Dictionary")
    else:
        print("This Key is not in the Dictionary")


if __name__ == "__main__":
    x = input("Please enter key you would like to check: ")
    checkifkeyexists(x)
