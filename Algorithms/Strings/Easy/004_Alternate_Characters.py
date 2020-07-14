def alternate(s):
    s_list = []
    for letter in s:
        s_list += [letter]

    while True:
        to_remove = []
        for c in range(len(s_list) - 1):
            if s_list[c] == s_list[c + 1]:
                if not to_remove.__contains__(s_list[c]):
                    to_remove += [s_list[c]]
        if len(to_remove) == 0:
            break
        else:
            for char in to_remove:
                for _ in range(s_list.count(char)):
                    s_list.remove(char)

    unique_letters = []
    unique_freq = []
    for letter in s_list:
        if not unique_letters.__contains__(letter):
            unique_letters += [letter]
            unique_freq += [s_list.count(letter)]

    disorg_freq = unique_freq[:]
    unique_freq.sort()
    org_letters = []
    for f in unique_freq:
        org_letters += [unique_letters[disorg_freq.index(f)]]

    possible = []
    for char1 in unique_letters:
        for char2 in unique_letters:
            experiment = []
            if char1 == char2:
                pass
            else:
                for letter in s_list:
                    if letter == char1:
                        experiment += [char1]
                    elif letter == char2:
                        experiment += [char2]

            to_remove = []
            for c in range(len(experiment) - 1):
                if experiment[c] == experiment[c + 1]:
                    if not to_remove.__contains__(experiment[c]):
                        to_remove += [experiment[c]]

            if len(to_remove) == 0:
                possible += [len(experiment)]

    if len(possible) == 0:
        return 0

    print('\n', possible)
    return max(possible)
