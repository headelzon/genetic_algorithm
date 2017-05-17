import numpy
import random
import itertools
import math


def ff(data, population, limit):
    fitness = []
    seq = []
    for a in range(len(population[0])):
        seq.append(a)

    for i in range(len(population)):
        while True:
            total_weight, total_benefit = 0, 0
            for j in range(len(population[0])):
                total_weight += population[i][j] * data[0][j]
                total_benefit += population[i][j] * data[1][j]

            if total_weight >= limit:
                while len(seq) > 0:
                    choice = random.choice(seq)
                    seq.remove(choice)
                    if population[i][choice] == 1:
                        population[i][choice] = 0
                        break
                    else:
                        pass

            else:
                break

        fitness.append([total_weight, total_benefit, i])
    return fitness


def ff_av(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][1])

    return numpy.mean(temp)


def select_roulette(fitt):
    fit, ind = [], []  # will store only indices

    for j in range(len(fitt)):
        fit.append(fitt[j][1])

    for j in range(len(fitt)):
        ind.append(fitt[j][2])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    # Python library random consists of a function which can select k elements of list according to given
    # weights, which is exactly the way proportionate selection works

    selected = random.choices(ind, probability, k=len(fit))
    return selected  # returns indices of selected individuals


def select_rest_rep(fitt):
    fit, ind = [], []

    for j in range(len(fitt)):
        fit.append(fitt[j][1])

    for j in range(len(fitt)):
        ind.append(fitt[j][2])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    selected, rests = [], []
    for i in range(len(fit)):
        n = math.floor(len(fit) * probability[i])
        l = [ind[i]] * n
        selected.extend(l)
        t = (len(fit) * probability[i] - n, i)
        rests.append(t)

    empty = len(fit) - len(selected)

    fit, ind = [], []

    for j in range(len(rests)):
        fit.append(rests[j][0])

    for j in range(len(rests)):
        ind.append(rests[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    l = random.choices(ind, probability, k=empty)

    selected.extend(l)

    return selected


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

            new_x.append(cross_part_1)
            new_x.append(cross_part_2)

            # crossover_count += 1
            i -= 2

    return new_x


def save_elite(population, new_population, data, limit):
    ff_now = ff(data, population, limit)
    ff_new = ff(data, new_population, limit)

    worst = min(ff_new, key=lambda x: x[1])
    best = max(ff_now, key=lambda x: x[1])

    new_population[worst[2]] = population[best[2]]


def mutate(population, mutation_prob):
    mut = random.uniform(0, 1)

    if mut <= mutation_prob:
        selected_indiv = random.randint(0, len(population) - 1)
        selected_bit = random.randint(0, len(population[0]) - 1)

        if population[selected_indiv][selected_bit] == 0:
            population[selected_indiv][selected_bit] = 1
        else:
            population[selected_indiv][selected_bit] = 0

        return True

    else:
        return False


def ff_short(data, population):
    fitness = []
    for i in range(len(population)):
        total_weight, total_benefit = 0, 0
        for j in range(len(population[0])):
            total_weight += population[i][j] * data[0][j]
            total_benefit += population[i][j] * data[1][j]

        fitness.append([total_weight, total_benefit, i])
    return fitness


def test(data, elements, limit):
    possible = list(itertools.product(range(2), repeat=elements))

    ff_init = ff_short(data, possible)

    below_limit = []

    for i in range(len(possible)):
        if ff_init[i][0] <= limit:
            below_limit.append(possible[i])
        else:
            pass

    ff = ff_short(data, below_limit)

    ff.sort(key=lambda x: x[1], reverse=True)

    return below_limit[ff[0][2]]