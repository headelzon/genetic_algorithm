import random


def ff(a, c, x):
    denominator = []
    for i in range(5):
        temp = []
        for j in range(4):
            exp = pow((x[j] - a[i][j]), 2) + c[i]
            temp.append(exp)
        b = round(sum(temp), 4)
        denominator.append(b)

    fraction = []
    for i in range(5):
        fraction.append(1 / denominator[i])

    func = sum(fraction)
    if 0.01 > func > 10.1532:
        print('Something\'s wrong\n')
    else:
        print(func)

    return func


def mate(population, selected, crossover_prob):

    global crossover_count

    i = len(population) - 1

    new_x = []

    while i - 1 > -1:

        if random.uniform(0, 1) > crossover_prob:
            new_x.append(population[selected[i]])
            new_x.append(population[selected[i-1]])
            i -= 2
            continue
        else:
            cross_point = random.randint(2, len(population[0]))

            cross_part_1, cross_part_2 = [], []

            cross_part_1.extend(population[selected[i]][:cross_point])
            cross_part_1.extend(population[selected[i - 1]][cross_point:])

            cross_part_2.extend(population[selected[i - 1]][:cross_point])
            cross_part_2.extend(population[selected[i]][cross_point:])

            cross_part_1 = saturation(cross_part_1)
            cross_part_2 = saturation(cross_part_2)

            new_x.append(cross_part_1)
            new_x.append(cross_part_2)

            crossover_count += 1
            i -= 2

    return new_x


def saturation(chromosome):
    # convert to decimal
    y_prim, i, x = 0, 0, []
    while i < 13:
        y_prim = chromosome[i:i + 4]
        y_prim = ''.join(map(str, y_prim))
        y_prim = int(y_prim, 2)

        # check criterion
        if y_prim > 10:
            chromosome[i:i+4] = [1, 0, 1, 0]    # decrease to max possible value if too big

        i += 4

    return chromosome   # return corrected individual