import random
import numpy
import itertools
import math


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
    worst = min(fitness, key=lambda tup: tup[0])
    t = (list(possible[best[1]]), best[0], worst[0])
    return t


def convert_to_decimal(chromosome):
    i, y_list = 0, []
    while i < 13:
        y_prim = chromosome[i:i + 4]
        y_prim = ''.join(map(str, y_prim))
        y_prim = int(y_prim, 2)
        y_list.append(y_prim)
        i += 4
    return y_list


def ff(a, c, x, worst, best):
    fitness, func = [], 0
    for w in range(len(x)):
        chromosome = convert_to_decimal(x[w])
        denominator = []
        for i in range(5):
            temp = []
            for j in range(4):
                exp = pow((chromosome[j] - a[i][j]), 2) + c[i]
                temp.append(exp)
            b = round(sum(temp), 4)
            denominator.append(b)

        fraction = []
        for i in range(5):
            fraction.append(1 / denominator[i])

        func = sum(fraction)

        if 0.01 > func > 10.1532:
            raise ValueError('Value of the function is incorrect!')
        else:
            func = numpy.interp(func, [worst, best], [0, 1])
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


def save_elite(population, new_population, a, c, worst, best):
    ff_now = ff(a, c, population, worst, best)
    ff_new = ff(a, c, new_population, worst, best)

    worst = min(ff_new, key=lambda tup: tup[0])
    best = max(ff_now, key=lambda tup: tup[0])

    new_population[worst[1]] = population[best[1]]


def mutate(population, mutation_prob):

    mut = random.uniform(0, 1)

    if mut <= mutation_prob:
        selected_indiv = random.randint(0, len(population) - 1)
        selected_bit = random.randint(0, len(population[0]) - 1)

        if population[selected_indiv][selected_bit] == 0:
            population[selected_indiv][selected_bit] = 1
        else:
            population[selected_indiv][selected_bit] = 0

        saturation(population[selected_indiv])

        return True

    else:
        return False


def print_parameters(a, c, population, worst, best):
    fitness = ff(a, c, population, worst, best)
    best2 = max(fitness, key=lambda tup: tup[0])
    best2 = population[best2[1]]

    i, x = 0, []
    while i < 13:
        y_prim = best2[i:i + 4]
        y_prim = ''.join(map(str, y_prim))
        y_prim = int(y_prim, 2)
        x.append(y_prim)
        i += 4
    print('Current best parameters: {}'.format(x))