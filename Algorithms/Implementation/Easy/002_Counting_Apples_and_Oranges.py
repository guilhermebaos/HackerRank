def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_apples = 0
    for d in apples:
        if s <= a+d <= t:
            num_apples += 1

    num_oranges = 0
    for d in oranges:
        if s <= b+d <= t:
            num_oranges += 1

    print(num_apples)
    print(num_oranges)
