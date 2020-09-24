"""
A function which finds the sum of num natural numbers.
(sum of digits of a randomly generated number n)

"""

from random import randint

# Approach 1


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

# Approach 2
# n = randint(100, 999)
#
# print(f'We got random number {n}')
#
# one = n % 10
# ten = n // 10 % 10
# hundred = n // 100
# sum = one + ten + hundred
#
# print(f'one ' + str(one))
# print(f'ten ' + str(ten))
# print(f'hundred ' + str(hundred))
#
# print(f'sum ' + str(one + ten + hundred))
# # or
# print(f'sum ' + str(sum))