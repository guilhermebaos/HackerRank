# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    # Time is AM
    if s[-2] == 'A':
        if s[0:2] == '12':
            return f'00{s[2:-2]}'
        else:
            return s[:-2]

    # Time is PM
    else:
        if s[0:2] == '12':
            return s[:-2]
        else:
            return f'{int(s[0:2]) + 12}{s[2:-2]}'
