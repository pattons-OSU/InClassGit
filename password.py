#! /usr/bin/env python3
import string
import random

"""
    Simeon Patton
    OSU CS362 Spring 2021
    In class activity 2 - Git in action

        c) Create a password Generator by use of random characters given a number from the user.

            Some code inspiration from pynative @
            https://pynative.com/python-generate-random-string/

"""


def password(a):
    characters = string.ascii_lowercase
    for i in range(a):
        result = ''.join(random.choice(characters))
        print(result)



def a_input():
    a = input("Please enter the number of characters that your password should be: ")
    a = int(a)
    print("")
    return int(a)

if __name__ == "__main__":
    print("")
    a = a_input()
    password(a)
    print("")