#

def authorize(password, attempt):
    string = []
    for letter in password:
        string += [ord(letter)]
    p = 131
    M = 1000000007
    n = len(string) - 1
    p_exponents = [p ** i for i in range(0, n + 2)]
    hash_value = 0
    for index, letter in enumerate(string):
        hash_value += letter * p_exponents[n - index]
    hash_value %= M
    if attempt == hash_value:
        return True
    string += [0]
    n += 1
    for append in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)):
        string[-1] = append
        hash_value = 0
        for index, letter in enumerate(string):
            hash_value += letter * p_exponents[n - index]
        hash_value %= M
        if attempt == hash_value:
            return True
    return False


def authEvents(events):
    password = ''
    results = []
    for command, value in events:
        if command == 'setPassword':
            password = value
        if command == 'authorize':
            if authorize(password, int(value)):
                results += [1]
            else:
                results += [0]
    return results
