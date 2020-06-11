#!/usr/bin/env python

def countstring(string):
    count1 = 0
    count2 = 0
    for i in string:
        if(i.islower()):
            count1 +=1
        elif(i.isupper()):
            count2 +=1
    print("The lowercase count is: ", count1)
    print("The uppercase count is: ", count2)
    

if __name__ == "__main__":
    x = input("Enter your string: ")
    countstring(x)
