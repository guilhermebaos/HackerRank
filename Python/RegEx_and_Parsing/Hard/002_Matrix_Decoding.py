import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

raw_string = ''
for column in range(len(matrix[0])):
    for row in range(len(matrix)):
        raw_string += matrix[row][column]

reg_ex = r'(?<=\w)\W+(?=\w)'
matches = re.findall(reg_ex, raw_string)

readable_string = raw_string
for m in matches:
    readable_string = readable_string.replace(m, ' ', 1)

print(readable_string)
