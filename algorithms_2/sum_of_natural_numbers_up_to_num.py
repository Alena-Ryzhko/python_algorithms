"""
Sum of natural numbers up to num.

A program to find the sum of n natural numbers using while loop and display it:
"""

num = 16

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate until zero
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)
