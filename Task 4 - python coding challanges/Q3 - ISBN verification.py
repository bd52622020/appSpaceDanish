#!/usr/bin/env python

import re          
       
def ibnverification(num):
    pattern = (r"[0-9]{1}-[0-9]{3}-[0-9]{5}-[0-9]{1}")
    if len(num) == 13:
        if re.search(pattern, num):
            print("this is a correct pattern")
        else:
            print("pattern incorrect")
    else:
        print("pattern incorrect size")


if __name__ == "__main__":
    one = input("Please enter the ISBN number you would like to verify: ")
    ibnverification(one)
