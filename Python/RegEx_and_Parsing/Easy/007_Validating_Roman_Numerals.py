import re

thousands = r'M{0,3}'
hundreds = r'(C[MD]|D?C{0,3})'
tens = r'(X[CL]|L?X{0,3})'
ones = r'(I[XV]|V?I{0,3})'

regex_pattern = thousands + hundreds + tens + ones + '$'
print(regex_pattern)

print(str(bool(re.match(regex_pattern, input()))))
