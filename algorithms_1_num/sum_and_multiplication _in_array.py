"""
Fill an array of numbers with keyboard input.
Calculate the sum and product of the array elements.
Display the array itself, the resulting sum and the product of its elements.

A function to sum and multiplication in array:
"""

length = int(input(f"Enter array length  "))
array = []
for item in range(length):
    number = int(input(f"Enter array element "))
    array.append(number)


def sum_and_mult(array):
    sum = 0
    mult = 1
    for item in array:
        sum += item
        mult *= item
    return {
        "summ": sum,
        "mult": mult,
        "array": array
    }


print(sum_and_mult(array))