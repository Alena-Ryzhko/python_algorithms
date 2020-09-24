"""
A function to print Seconds to  Hours, Minutes, Seconds ---> h:m:s
"""


def sec_to_hms(seconds):
    hours = seconds // 3600
    minutes = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    if hours > 0:
        return f'{hours}:{minutes}:{seconds}'

    elif minutes > 0:
        return f'0:{minutes}:{seconds}'

    else:
        return f'0:0:{seconds}'


print(sec_to_hms(3654))