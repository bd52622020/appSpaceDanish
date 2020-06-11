#!/usr/bin/env python

import re          
       

def checklist(list):
    if list[0] == list[-1]:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    one = input("Please enter the list you would like to check is the first and last number are same: ")
    checklist(one)
