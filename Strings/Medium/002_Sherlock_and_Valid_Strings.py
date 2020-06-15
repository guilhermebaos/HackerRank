def isValid(s):
    ascii_string = []
    for ascii_chr in range(0, ord('z')-ord('a')+1):
        ascii_string += [0]

    for letter in s:
        ascii_string[ord(letter) - ord('a')] += 1

    ascii_zeros = ascii_string.count(0)
    for _ in range(0, ascii_zeros):
        ascii_string.remove(0)

    downsize = min(ascii_string) - 1
    for ind in range(0, len(ascii_string)):
        ascii_string[ind] -= downsize

    if ascii_string.count(ascii_string[0]) == len(ascii_string):
        return 'YES'
    else:
        frequency = []
        for number in ascii_string:
            found = False
            for f in frequency:
                if f[0] == number:
                    f[1] += 1
                    found = True
                    break
            if not found:
                frequency += [[number, 1]]

        new_frequency = []
        numbers = []
        for item in frequency:
            numbers += [item[0]]
            new_frequency += [[]]
        numbers.sort()

        for item in frequency:
            new_frequency[numbers.index(item[0])] = item

        frequency = new_frequency[:]

        freq_of_freq = []
        for pair in frequency:
            freq_of_freq += [pair[1]]
        max_index = freq_of_freq.index(max(freq_of_freq))

        print(frequency, max_index)

        try:
            if frequency[0][1] == 1 and len(frequency) == 2:
                return 'YES'
            elif frequency[max_index + 1][1] == 1 and frequency[max_index + 1][0] == frequency[max_index][0] + 1 and len(frequency) == 2:
                return 'YES'
            else:
                return 'NO'
        except IndexError:
            return 'NO'


print(isValid('xxxaabbccrry'))
