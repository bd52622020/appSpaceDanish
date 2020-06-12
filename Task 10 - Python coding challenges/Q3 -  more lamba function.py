#!/usr/bin/env python

mylist = [1,2,13,19,26,39,40,39,38,37,36]

newlist = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), mylist)) 

if __name__ == "__main__":
    print(newlist)
    
