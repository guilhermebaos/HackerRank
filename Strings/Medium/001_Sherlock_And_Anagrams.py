def sherlockAndAnagrams(s):
    if unique(s):
        return 0

    s_list = []
    for letter in s:
        s_list += [letter]



def unique(string):
    string_list = []
    for letter in string:
        if string_list.__contains__(letter):
            return False
        else:
            string_list += [letter]
    return True
