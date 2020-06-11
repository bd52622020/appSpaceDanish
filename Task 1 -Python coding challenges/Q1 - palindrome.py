#!/usr/bin/env python

def ispalin(word):
    word2 = word[::-1]
    if word == word2:
        print("this string is a palindrome")
    else:
        print("this string is not a palindrome")

if __name__ == "__main__":
    w = input("Enter your word: ")
    ispalin(2)