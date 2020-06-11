#!/usr/bin/env python
def primenums(x):
    prime = []
    for num in range(0, x):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    prime.append(num)
    print(prime)

if __name__ == "__main__":
    one = input("Please enter the range up to which you would like prime numbers: ")
    primenums(one)
