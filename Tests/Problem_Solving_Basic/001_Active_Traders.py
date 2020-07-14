def mostActive(customers):
    n = len(customers)

    trade_nums = {}
    for trade in customers:
        try:
            trade_nums[trade] += 1
        except KeyError:
            trade_nums[trade] = 1

    active_traders = []
    for key in trade_nums.keys():
        if trade_nums[key] / n >= 0.05:
            active_traders += [key]

    active_traders.sort()
    return active_traders


print(mostActive(['Alpha', 'Omega', 'Epsilon', 'Alpha', 'Alpha', 'Alpha', 'Alpha', 'Alpha']))