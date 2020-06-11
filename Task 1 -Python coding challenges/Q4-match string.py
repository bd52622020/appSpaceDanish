#!/usr/bin/env python
import re 


def match(string):
    pattern = '^[a-zA-Z0-9_]*$'
    if re.search(pattern, string):
        print("match found")
    else:
        print("no match found")
 
 
if __name__ == "__main__":
    x = input("Enter your string to match the pattern: ")
    match(x)