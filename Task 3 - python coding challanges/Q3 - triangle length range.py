#!/usr/bin/env python

def trianglecalc(x,y):
    z = x + y
    v = y - x
    v = abs(v)
    print(v, "< x <",z)

if __name__ == "__main__":
    one = input("Please enter one length of your triangle: ")
    two = input("Please enter the second length of your triangle: ")
    checkfile(one, two)
