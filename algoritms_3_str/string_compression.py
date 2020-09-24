"""
The string compression algorithm.

Given an input string of a certain length,
design an algorithm that compresses the string.
The string should be compressed such that consecutive duplicates of characters
are replaced with the character
and followed by the number of consecutive duplicates.

This kind of compression is called Run Length Encoding.


Example:
    Input : wwwwaaadexxxxxx                         # if the input string it is,
    Output : w4a3dex6                               # then the function should return it

"""

string = input(f"Enter the String please ")


def str_compress(string):
    counter = 1
    result = string[0]
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
            result += string[i + 1]
            counter = 1
    if counter > 1:
        result += str(counter)
    return result


print(f'The Run Length Encoded string is ' + str_compress(string))
