def camelcase(s):
    words = 1
    for letter in s:
        if letter.isupper():
            words += 1
    return words
