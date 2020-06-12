#!/usr/bin/env python


mylist = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

def removedups(y):
    y = list(dict.fromkeys(y))
    print(y)
    

if __name__ == "__main__":
    removedups(mylist)
