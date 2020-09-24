"""
Reverse a string.

A function that takes a String(provided by the user) as an argument and returns the backward String.

"""

string = input(f'Enter the String ')


# Approach 1
def reverse_string1(string):
    return string[::-1]


print(reverse_string1(string))


# Approach 2
def reverse_string2(string):
    return ''.join(reversed(string))


print(reverse_string1(string))

print('--------------------------------------')

# Approach 3 (beautiful :))
result = ''
index = len(string)
while index > 0:
    result += string[index - 1]
    index -= 1
    print(result)
