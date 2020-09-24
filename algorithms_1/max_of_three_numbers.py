"""
A function to find the largest among three numbers and display it:
"""
num1 = int(input(f'First number '))
num2 = int(input(f'Second number '))
num3 = int(input(f'Third number '))


def max_of_three(num1, num2, num3):

    if num1 > num2:
        if num1 > num3:
            print(f'max from numbers {num1}, {num2}, {num3} is {num1}')
        else:
            print(f'max from numbers {num1}, {num2}, {num3} is {num3}')
    else:
        if num2 > num3:
            print(f'max from numbers {num1}, {num2}, {num3} is {num2}')
        else:
            print(f'max from numbers {num1}, {num2}, {num3} is {num3}')


max_of_three(num1, num2, num3)