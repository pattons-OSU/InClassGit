#! /usr/bin/env python3

"""
    Simeon Patton
    OSU CS362 Spring 2021
    In class activity 2 - Git in action

        b) Create a program to find all of the nubers that a number is evenly divisible by.

            Some code inspiration from GeeksforGeeks @
            https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
"""

def divisor(a):
    ## Number to enumerate by
    i = 1
    print(f"The even divisors of {a} are: ")
    ## If given number is even mod divisible then print value and move on
    while i <= a:
        if (a % i == 0):
            print(i)
        i = i + 1

    

def a_input():
    a = input("Please enter a number to find it's divisors: ")
    a = int(a)
    print("")
    return int(a)

if __name__ == "__main__":
    print("")
    a = a_input()
    divisor(a)
    print("")