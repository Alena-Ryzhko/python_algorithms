"""
Recursion is a common mathematical and programming concept.
It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

A recursive function that displays a string value,
entered from the keyboard, n-th number of times,
n also entered from the keyboard:
"""

string = input('Enter String ')
n = int(input("Enter a number of repetitions "))


def recursive_replication(string, n):

    if n > 1:
        return recursive_replication(string, n-1) + string
    elif n == 1:
        return string


print(recursive_replication(string, n))

