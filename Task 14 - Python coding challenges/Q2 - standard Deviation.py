#!/usr/bin/env python

import statistics

def stdev(x):
    print(statistics.pstdev(x))

data = [4, 2, 5, 8, 6]
    
if __name__ == "__main__":
    stdev(data)
    
