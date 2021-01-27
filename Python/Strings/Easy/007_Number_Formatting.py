def print_formatted(number):
    max_width = len(str(bin(number))) - 2
    for i in range(1, number + 1):
        print(str(i).rjust(max_width),
              str(oct(i))[2:].rjust(max_width),
              str(hex(i))[2:].upper().rjust(max_width),
              str(bin(i))[2:].rjust(max_width))
