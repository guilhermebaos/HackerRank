from time import asctime

common_lenght = 0
string_len = 0


def loop_through(pairs_list, observe, compatible_list, max_lenghts_list, depth):
    # print(pairs_list, '\n' + str(observe), '\n' + str(compatible_list), '\n\n')
    # input('')
    global common_lenght
    global string_len
    results = []
    # observe = observe[0:int(len(observe)*0.075)]
    for index, pair in enumerate(pairs_list):
        if observe.__contains__(pair):
            if compatible_list[index]:
                if string_len - pair[0] + depth > common_lenght:
                    if max_lenghts_list[index]:
                        results += [max_lenghts_list[index]]
                    else:
                        depth += 1
                        x = max(loop_through(pairs_list, compatible_list[index], compatible_list, max_lenghts_list, depth)) + 1
                        if x > common_lenght:
                            common_lenght = x
                        results += [x]
                        max_lenghts_list[index] = x
            else:
                results += [1]
    if len(results) == 0:
        return [1]
    return results


def commonChild(s1, s2):
    new_s1 = ''
    for letter in s1:
        if s2.__contains__(letter):
            new_s1 += letter

    new_s2 = ''
    for letter in s2:
        if s1.__contains__(letter):
            new_s2 += letter

    if len(new_s1) == 0:
        return 0

    global string_len
    string_len = len(new_s1)

    print(str(len(new_s1)) + '\n' + new_s1 + '\n' + new_s2 + '\n')
    new_s2_letter_indexes = {}
    letter_index = -1
    for letter in new_s2:
        letter_index += 1
        try:
            new_s2_letter_indexes[letter] += [letter_index]
        except KeyError:
            new_s2_letter_indexes[letter] = [letter_index]

    grouped_pairs = []
    pairs = []
    for start, letter1 in enumerate(new_s1):
        grouped_pairs += [[]]
        for end in new_s2_letter_indexes[letter1]:
            pairs += [[start, end]]
            grouped_pairs[-1] += [[start, end]]

    print(asctime())
    print(len(pairs))
    print(pairs)
    print(grouped_pairs, '\n\n')

    compatible = []

    for index, pair_group in enumerate(grouped_pairs):
        for pair_add in pair_group:
            compatible += [[]]
            for pair_compare_group in grouped_pairs[index + 1:]:
                for pair_compare in pair_compare_group[::-1]:
                    if pair_add[1] > pair_compare[1] > pair_add[1]:
                        compatible[-1] += [pair_compare]
                    else:
                        break

    print(asctime())
    # print(compatible, '\n\n')
    print(len(compatible), len(compatible[0]))

    max_lenghts = []
    for _ in pairs:
        max_lenghts += [[]]

    loop_through(pairs, pairs, compatible, max_lenghts, 0)

    print(asctime())
    return common_lenght


string_1 = 'APMCTKBUKYRGZPAUVZEBVUXRGDVITOYXWQWRVCSXESMEHQLHPDJQWETAWQVSBRRNRRFDLFTRXOTKQHFTYAZSGBORDNAMUAJTPVOKERLVOLEALDQQLUDCUIRXJHQEZBRWYPFJXNTPELEZHNJILIZVZLYQJDFYSYQNRFFAOYXHQBQVRLFDIIOGWKQIZGVELYOUKZBKMHVYGIKIPSEMWSCWYOJTHOQKMLBAIZYNAKYNCXKDTTESODDAEAHKCDHCJYAHERACMLYQHXIRDFUSRTZDNVHSYFKCSPPYSLHOGIBTNUJTZQWVTHKUNDNWZADMATSUXEISCACQNQXIHNTXGCZUGIGBDONYTUXAXFINAYGZJVDCTZCWPGFNQDPERUCNJUXIFDSQHULYPZRNUOKMLMMQAJMLKCHJMEFJVRYZIPFQOBSDPAITHGMNKROCWJEGESCGOIUOQHOYUEQNPJPBMCNRZUHOSQNSUNCSTVQVWFGMUFJZGMEUVUPH'
string_2 = 'JUVSDRRSHFGSSLLLZEPJDVAWDPKQBKUHHOZFFXKQMGAACZUYOMNPHWGTYZWQGSMNYXWNFYNOIVVMPZXUNKJQYBYJINBOHXUWIVRTVLEKCOPDMTKTGDBWECDAVPMLHQLERZHDVZJZODPSAPGSRWJXNGFEBQBLTLNDIEGFHEGHJWFOIYXRUJMODSNXUFWBIJJMXTFMUKQEYPNBTZFEJNLDNWCGQLVUQUKGZHJOKZNPMUYEQLEYNNORKJQAMSTHTBCCPQTTCPRZATWNJQJXPODRXKIWDOFUBZVSDTAPFRMXJBJMUGVRZOCDUIPXVEGMRQNKXDKNWXMTNDJSETAKVSYMJISAREEJPLRABMXJSRQNASOJNEEVAMWCFJBCIOCKMHCMYCRCGYFNZKNALDUNPUSTSWGOYHOSWRHWSMFGZDWSBXWXGVKQPHGINRKMDXEVTNNZTBJPXYNAXLWZSBUMVMJXDIKORHBIBECJNKWJJJSRLYQIKKPXSNUT'

small_1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
small_2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
print(commonChild(string_1, string_2))