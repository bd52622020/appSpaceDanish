#!/usr/bin/env python

def starpattern(x = 5):
    for i in range(x):
        for j in range(i):
            print("*", end="")
        print()
    for i in range(x):
        for j in range(x-i):
            print("*", end="")
        print()



if __name__ == "__main__":
    x = input("Please enter number of rows: ")
    starpattern(x)
