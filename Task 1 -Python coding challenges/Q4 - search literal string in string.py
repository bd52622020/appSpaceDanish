#!/usr/bin/env python

def searchstring(string):
    list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    if string in list:
        print("I found " + string + " in list")
    else:
        print("This word is not in the list")

if __name__ == "__main__":
    x = input("Enter the word you would like to search from the string: ")
    searchstring(x)
