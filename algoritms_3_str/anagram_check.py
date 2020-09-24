"""
Anagram Check.

Given two strings str1 and str2, check if both the strings are anagrams of each other.

Example_1:
Input : str1 = "listen"
        str2 = "silent"
Output :  True                       # (because the strings are anagrams.)

Example_2:
Input : str1 = "dad"
        str2 = "bad"
Output : False                       # (because the strings aren't anagrams.)

"""


str1 = input(f"Enter First word ")
str2 = input(f"Enter Second word ")


def anagram_check(str1, str2):

    str1 = str1.upper()
    str2 = str2.upper()
    if str1 == str2 or len(str1) != len(str2):
        return False
    for char in str1:
        if str1.count(char) != str2.count(char):
            return False
    return True


print(anagram_check(str1, str2))