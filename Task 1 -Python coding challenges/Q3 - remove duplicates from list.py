#!/usr/bin/env python

def rmvdups(x): 
    return list(dict.fromkeys(x))

mylist = ["a", "b", "a", "c", "c", "c", "b", "a", "c", "c", "c"]

#print(rmvdups(mylist))

def rmvduploop(x):
    nodupes = []
    for i in x:
        if i not in nodupes:
            nodupes.append(i)
    return nodupes

#print(rmvduploop(mylist))



if __name__ == "__main__":
    x = input("Enter your list with duplicates: ")
    rmvdups(x)
    rmvduploop(x)
