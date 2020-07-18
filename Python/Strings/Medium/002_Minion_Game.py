def minion_game(string):
    vowels = 'AEIOU'
    Stuart_points = 0  # Start with consonants
    Kevin_points = 0   # Start with vowels
    points = [Stuart_points, Kevin_points]

    n = len(string)
    for index, letter in enumerate(string):
        p = n - index
        if vowels.__contains__(letter):
            points[1] += p
        else:
            points[0] += p

    if points[0] > points[1]:
        print('Stuart', points[0])
    elif points[0] < points[1]:
        print('Kevin', points[1])
    else:
        print('Draw')


minion_game('BAANANAS')
