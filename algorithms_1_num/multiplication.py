"""
A function to find multiplication of two numbers:
"""


def multiplication(number_1, number_2):

    iterator = 0
    result = 0
    while iterator < number_2:
          result += number_1
          iterator += 1
    return result


print(multiplication(6786, 776))