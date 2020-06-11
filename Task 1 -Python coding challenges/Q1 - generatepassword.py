#!/usr/bin/env python

import random
import string
from Crypto.Util.number import getRandomInteger

def genpassword(x=15):
    y = string.ascii_letters + string.digits
    return "".join(random.choice(y) for i in range(x))

if __name__ == "__main__":
    print(genpassword())
