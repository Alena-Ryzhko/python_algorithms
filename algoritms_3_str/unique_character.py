"""
Unique Characters in a String.

Example:
    Input : geeksforgeeks
    Output : geksfor

A program to remove all duplicates from a given string:
"""

string = input(f'Enter the String ')


def unique_characters_string(string):
    result = ''
    for char in string:
        if result.count(char) == 0:
            result += char
    return result


print(unique_characters_string(string))


# main function
if __name__ == "__main__":
    string = "geeksforgeeks"
    print("Unique Characters in a String =", unique_characters_string(string))
    assert unique_characters_string(string) == "geksfor"

