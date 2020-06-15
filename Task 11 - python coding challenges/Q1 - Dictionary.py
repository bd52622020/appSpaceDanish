#!/usr/bin/env python

dictu={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

d = [k.upper() for (k,v) in dictu.items() if v < 5000]

if __name__ == "__main__":
    print(d)
    
