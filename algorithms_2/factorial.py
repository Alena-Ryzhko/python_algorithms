"""
For example, the factorial of 6 is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.

A function to find the factorial of a number n provided by the user and display it:
"""

# Approach 1


def factorial_1(n):
    result = 1

    if n < 0:
        return 'Sorry, factorial does not exist for negative numbers'
    elif n == 0:
        return 'The factorial of 0 is 1'
    else:
        for i in range(1, n + 1):
            result *= i
        return result


n = int(input('Enter number to calculate factorial '))
print(factorial_1(n))


# Approach 2
# Factorial using recursion

m = int(input("Enter number to calculate factorial "))


def factorial_2(m):
    if m == 0:
        return 1
    else:
        return m * factorial_2(m - 1)


print(factorial_2(m))




