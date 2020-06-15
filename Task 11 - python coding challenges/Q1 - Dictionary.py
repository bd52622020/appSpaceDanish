#!/usr/bin/env python

dictu={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

d = dict( (a,b) for a, b in dictu.items() if b < 5000)

d = {k.upper(): v for k, v in d.items()}

if __name__ == "__main__":
    print(d)
    
