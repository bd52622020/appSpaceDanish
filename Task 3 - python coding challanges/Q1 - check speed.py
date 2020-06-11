#!/usr/bin/env python

def checkspeed(speed):
    points = 0
    if speed < 70:
        print("Ok")
    else:
        while speed>70:
            points +=1
            speed -= 5
            continue
    if points <= 12:
        print("You have " + str(points)  + " points")
    else:
        print("License suspended")


if __name__ == "__main__":
    x = input("Please enter your speed: ")
    checkspeed(x)
