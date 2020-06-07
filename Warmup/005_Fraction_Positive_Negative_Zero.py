def plusMinus(arr):
    lenght = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for number in arr:
        if number > 0:
            pos += 1
        elif number < 0:
            neg += 1
        else:
            zer += 1
    print(pos/lenght)
    print(neg/lenght)
    print(zer/lenght)
