"""
Reverse a string.

A function that takes a String(provided by the user) as an argument
and returns the backward String:
"""

string = input(f'Enter the String: ')


def reverse_string_a(string):
    return ' '.join(list(reversed(string.split())))


print(reverse_string_a(string))


# or

def reverse_string_b(string):
    return ' '.join(list(reversed(string.split())))


print(reverse_string_b("Rosa is red"))
