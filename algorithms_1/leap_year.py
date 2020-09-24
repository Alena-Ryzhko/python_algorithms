"""
Write a program to check whether a year is leap year or not.

"""

# Leap year

year = int(input('Enter year '))

if year % 4 != 0:
    print('Not Leap year')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            if year > 0:
                print("Leap year")
        else:
            print('Not Leap year')
    else:
        print('Leap year')