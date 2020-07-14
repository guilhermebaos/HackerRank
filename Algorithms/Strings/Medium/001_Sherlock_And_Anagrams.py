def sherlockAndAnagrams(s):
    if unique(s):
        return 0

    anagrammatic_pairs = ap = 0

    for num_letters in range(1, len(s)):
        slices = []
        for c in range(0, len(s) - num_letters + 1):
            cut = s[c:c + num_letters]
            cut = sort_string(cut)
            if slices.__contains__(cut):
                ap += slices.count(cut)
            slices += [cut]
    return ap


def unique(string):
    string_list = []
    for letter in string:
        if string_list.__contains__(letter):
            return False
        else:
            string_list += [letter]
    return True


def sort_string(string):
    s_list = []
    for letter in string:
        s_list += [letter]
    s_list.sort()
    new_s = ''
    for letter in s_list:
        new_s += letter
    return new_s


print(sherlockAndAnagrams('kkkk'))
