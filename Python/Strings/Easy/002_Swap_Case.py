def swap_case(s=''):
    new_string = ''
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                new_string += letter.upper()
            else:
                new_string += letter.lower()
        else:
            new_string += letter
    return new_string
