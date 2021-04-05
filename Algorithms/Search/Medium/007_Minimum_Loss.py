# https://www.hackerrank.com/challenges/minimum-loss/problem

def minimumLoss(price):
    # Sort the prices and keep the original
    unsorted_prices = price[:]
    price.sort()

    # Get the deltas between each consecutive ordered price
    deltas = []
    for index in range(len(price) - 1):
        deltas += [price[index + 1] - price[index]]

    # Sort the deltas and keep the original
    unsorted_deltas = deltas[:]
    deltas.sort()

    # Go from the smallest possible delta to the larger and check if the lower price is after the higher one
    # This makes sure that minimum loss is achieved
    for d in deltas:
        delta_index = unsorted_deltas.index(d) + 1
        higher_price = price[delta_index]

        higher_price_index = unsorted_prices.index(higher_price)
        if higher_price - d in unsorted_prices[higher_price_index:]:
            break

    return d
