#!/usr/bin/env python

def pastriangle(num = 5):
    for i in range(1, num+1):
        for j in range(1, num-i+1):
            print(" ", end="")
        for j in range(i,0,-1):
            print(j, end="")
        for j in range(2,i+1):
            print(j,end="")
        print()
    

if __name__ == "__main__":
    x = input("Enter number of rows: ")
    pastriangle(x)
