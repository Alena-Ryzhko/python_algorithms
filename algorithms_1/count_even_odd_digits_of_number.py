"""
A function to count Even/Odd Digits of Number.

"""
n = int(input(f'Enter a number '))


def count_odd_even(n):
    odd_count = 0
    even_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = n // 10
    print(f"Odd numbers in number  {odd_count}")
    print(f"Even numbers in number  {even_count}")


count_odd_even(n)
