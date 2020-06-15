#!/usr/bin/env python
import random
import string

def genpassword(x=15):
    y = string.ascii_letters + string.digits + str("@£$%&")
    return "".join(random.choice(y) for i in range(x))

print(genpassword())

if __name__ == "__main__":
    y = input("Please type how long you would like your password to be, or ignore for default length: ") or 15
    print(genpassword(int(y)))
    
