def caesarCipher(s, k):
    new_s = ''
    if k > 26:
        k %= 26
    for letter in s:
        l_num = ord(letter)
        if ord('a') <= ord(letter) <= ord('z'):
            l_num += k
            if l_num > ord('z'):
                l_num = l_num - ord('z') - 1 + ord('a')
        if ord('A') <= ord(letter) <= ord('Z'):
            l_num += k
            if l_num > ord('Z'):
                l_num = l_num - ord('Z') - 1 + ord('A')
        new_s += chr(l_num)
    return new_s


print(caesarCipher('www.abc.xy', 87))