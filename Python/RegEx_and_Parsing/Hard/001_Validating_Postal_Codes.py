import re


regex_integer_in_range = r"^\d{6}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.


P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

print(re.findall(regex_alternating_repetitive_digit_pair, P))
