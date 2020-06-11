#!/usr/bin/env python
       
import os.path

def checkfile(filepath):
    try:
        os.path.exists(filepath)
    except:
        print("no file exists here")
    finally:
        with open(filepath, "r") as file:
            head = [next(file) for x in range(10)]
            print(head)
        file.close()


if __name__ == "__main__":
    x = input("Please enter your file path: ")
    checkfile(x)
