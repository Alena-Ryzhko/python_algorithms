string = input(f'Enter the String: ')


def reverse_string(string):
    return ' '.join(list(reversed(string.split())))


print(reverse_string(string))