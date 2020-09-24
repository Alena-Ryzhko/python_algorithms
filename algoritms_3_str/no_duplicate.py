"""
No duplicate.
Example
              Input
              'alpha beta beta gamma   gamma gamma delta alpha beta beta gamma gamma gamma delta'

              Output
              'alpha beta gamma delta'

A function to remove all duplicate words from a string,
leaving only single (first) words entries:
"""


def no_duplicate(string):
    array = string.split(' ')
    result = []
    for item in array:
        if not item in result:
            result.append(item)
    return ' '.join(result)


string = 'alpha beta beta gamma   gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(no_duplicate(string))
