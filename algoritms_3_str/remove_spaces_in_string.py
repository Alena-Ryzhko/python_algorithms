"""
Entering a string that may have
spaces at the beginning, end, and between words more than one space.
Bring it to a normalized form, i.e. remove all leading and trailing spaces,
and leave only one space between words.

A program to remove spaces in string:
"""
# Approach 1

string = input(f'Enter the string')


def normalize(string):
    while string[0] == ' ':
        string = string[1:]
    while string[len(string) - 1] == ' ':
        string = string[:-1]
    index = 0
    while index < len(string):
        if string[index] == ' ' and string[index + 1] == ' ':
            string = string[:index + 1] + string[index + 2:]
        else:
            index += 1
    return string


print(normalize(string))


# Approach 2
string = input(f'Enter the string')


def normalize(string):
    return ' '.join(string.split())


print(normalize(string))