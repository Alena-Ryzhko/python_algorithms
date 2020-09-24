"""
Palindrome.
A string is said to be palindrome if the reverse of the string is the same as string.
For example, “radar” is a palindrome, but “radix” is not a palindrome,
            “malayalam” is a palindrome, but “geeks” is not a palindrome

Input : radar                                Input : malayalam
Output : True                                Output : True

Input : radix                                Input : geeks
Output : False                               Output : False

Python program to check if a string is palindrome or not:
"""
string = input(f'Enter the String ')


def palindrome_check(string):
    reversed_string = string[::-1]
    print('Reverse String: ' + reversed_string )
    if string == reversed_string:
        return True
    else:
        return False


print(palindrome_check(string))