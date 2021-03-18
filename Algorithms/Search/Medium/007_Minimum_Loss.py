# https://www.hackerrank.com/challenges/minimum-loss/problem

def minimumLoss(price):
    unsorted_prices = price[:]
    price.sort()

    deltas = []
    for index in range(len(price) - 1):
        deltas += [price[index + 1] - price[index]]

    unsorted_deltas = deltas[:]
    deltas.sort()

    for d in deltas:
        delta_index = unsorted_deltas.index(d) + 1
        higher_price = price[delta_index]

        higher_price_index = unsorted_prices.index(higher_price)
        if higher_price - d in unsorted_prices[higher_price_index:]:
            break

    return d
