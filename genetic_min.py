import random
import numpy
import itertools


def bruteforce(a, c):
    o = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    possible = list(itertools.product(o, repeat=4))

    func, fitness = 0, []

    for w in range(len(possible)):
        x = possible[w]
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
        t = (func, w)
        fitness.append(t)

    best = max(fitness, key=lambda tup: tup[0])
    return list(possible[best[1]])


def ff(a, c, x):
    fitness, func = [], 0
    for w in range(len(x)):
        denominator = []
        for i in range(5):
            temp = []
            for j in range(4):
                exp = pow((x[w][j] - a[i][j]), 2) + c[i]
                temp.append(exp)
            b = round(sum(temp), 4)
            denominator.append(b)

        fraction = []
        for i in range(5):
            fraction.append(1 / denominator[i])

        func = sum(fraction)
        if 0.01 > func > 10.1532:
            print('Something\'s wrong\n')
            break
        else:
            t = (func, w)
            fitness.append(t)
    return fitness


def ff_av(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][0])

    return numpy.mean(temp)


def select(ff):
    fit, ind = [], []  # will store only indices

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    selected = random.choices(ind, probability, k=len(fit))
    return sorted(selected)  # returns indices of selected individuals


def saturation(chromosome):
    # convert to decimal
    y_prim, i, x = 0, 0, []
    while i < 13:
        y_prim = chromosome[i:i + 4]
        y_prim = ''.join(map(str, y_prim))
        y_prim = int(y_prim, 2)

        # check criterion
        if y_prim > 10:
            chromosome[i:i + 4] = [1, 0, 1, 0]  # decrease to max possible value if too big

        i += 4
    return chromosome  # return corrected individual


def mate(population, selected, crossover_prob):
    # global crossover_count

    i = len(population) - 1

    new_x = []

    while i - 1 > -1:

        if random.uniform(0, 1) > crossover_prob:
            new_x.append(population[selected[i]])
            new_x.append(population[selected[i - 1]])
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

            # crossover_count += 1
            i -= 2

    return new_x
