"""
Write a program which finds the sum of num natural numbers
(sum of digits of a randomly generated number n)
"""

from random import randint


def sum_of_natural_numbers_of_num(number_of_digits):

    down = 10**(number_of_digits-1)
    up = (10**number_of_digits)-1
    n = randint(down, up)                 # randomly generated number n
    print(f'We got number {n} ')
    sum = 0
    i = 0
    while i < number_of_digits:
        sum += n % 10
        n = n // 10
        i += 1
    print(f'The sum is  {sum}')


number_of_digits = int(input('Please enter number of digits of the random generated number '))

sum_of_natural_numbers_of_num(number_of_digits)

