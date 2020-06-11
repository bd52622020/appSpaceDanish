#!/usr/bin/env python

def checkrightangletri(x, y, z):
    if x > y and x > z:
        if (x ** 2) == ((y ** 2) + (z ** 2)):
            print("Yes, this is right angle triangle")
        else:
            print("No, this is not right angle triangle")
    elif y > x and y > z:
            if (y ** 2) == ((x ** 2) + (z ** 2)):
                print("Yes, this is right angle triangle")
            else:
                print("No, this is not right angle triangle")
    elif (z ** 2) == ((y ** 2) + (x ** 2)):
        print("Yes, this is right angle triangle")
    else:
        print("No, this is not right angle triangle")


if __name__ == "__main__":
    x = input("Please enter one side of the triangle: ")
    y = input("Please enter one side of the triangle: ")
    z = input("Please enter one side of the triangle: ")
    checkrightangletri(x, y, z)
