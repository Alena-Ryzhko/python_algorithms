"""
Find the sum of elements in an array
between the minimum and maximum elements.
The minimum and maximum elements themselves should not be included in the amount.

A function to find a Sum between min and max elements of an array:
"""


def sum_between_min_and_max(array):
    maximum = array[0]
    minimum = array[0]
    max_index = 0
    min_index = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        if array[index] < minimum:
            minimum = array[index]
            min_index = index
        index += 1
    subarray = array[min(min_index, max_index) + 1: max(min_index, max_index)]
    return sum(subarray)


print(sum_between_min_and_max([1, 1, 111, 5, 6, 7, -532, 7]))
