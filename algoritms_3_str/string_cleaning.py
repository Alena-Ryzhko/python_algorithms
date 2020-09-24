"""
A program to take in a string and clean out all numeric characters:
"""


def string_cleaning(string):
    result = ''
    for char in string:
        if not char.isdigit():
            result += char
    return result


print(string_cleaning('! !'))
print(string_cleaning('123456789'))
print(string_cleaning('This looks5 grea8t!'))

