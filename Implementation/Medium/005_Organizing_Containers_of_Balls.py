def organizingContainers(container):
    total_balls = []
    possible_containers = []
    for _ in range(len(container)):
        total_balls += [0]
        possible_containers += [0]

    for box in container:
        for ball_num, balls in enumerate(box):
            total_balls[ball_num] += balls

    possible = []
    for box_num, box in enumerate(container):
        possible += [[]]
        for ball_num, balls in enumerate(total_balls):
            give = 0
            for other_balls in box:
                give += other_balls
            give -= box[ball_num]
            want = balls - box[ball_num]
            if give == want:
                possible[-1] += [ball_num]

    for box_possible in possible:
        for poss in box_possible:
            possible_containers[poss] += 1

    for poss in possible_containers:
        if poss == 0:
            return 'Impossible'
    return 'Possible'
