"""
Create a function to Print the Fibonacci sequence.

The Fibonacci Sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

Fn = Fn-1 + Fn-2
but F0 = 0 and F1 = 1
"""


n = int(input("How many numbers will be in the sequence? Enter please "))


def fibonacci(n):
    # First Fibonacci number is 0
    # Second Fibonacci number is 1
    n1, n2 = 0, 1
    count = 0

    # check if number of nth Fibonacci number is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


fibonacci(n)