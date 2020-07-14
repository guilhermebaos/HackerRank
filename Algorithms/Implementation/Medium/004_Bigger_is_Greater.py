def biggerIsGreater(w):
    ascii_word = []
    for letter in w:
        ascii_word += [ord(letter)]

    unsorted_word = ascii_word[:]
    ascii_word.reverse()
    reverse_word = ascii_word[:]
    ascii_word.sort(reverse=True)

    if ascii_word == unsorted_word:
        return 'no answer'
    else:
        max_letter = 0
        possible_pairs = []
        for index_letter, letter in enumerate(reverse_word):
            if letter >= max_letter:
                possible_pairs += [letter]
                max_letter = letter
            else:
                to_switch = letter
                to_switch_index = index_letter
                break

        for letter in possible_pairs:
            if letter <= to_switch:
                possible_pairs[possible_pairs.index(letter)] = 10000

        switch_to = min(possible_pairs)
        switch_to_index = reverse_word.index(switch_to)

        reverse_word[to_switch_index] = switch_to
        reverse_word[switch_to_index] = to_switch

        reverse_word[0:to_switch_index] = sorted(reverse_word[0:to_switch_index], reverse=True)

        reverse_word.reverse()
        new_word = ''

        for letter in reverse_word:
            new_word += chr(letter)

        return new_word
