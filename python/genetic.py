import numpy
import random


def ff(array):
    fitness = []
    for i in range(len(array)):
        B = []
        for j in array[i]:
            B.append(str(j))
        B = ''.join(B)
        B = int(B, 2)
        t = (round(numpy.interp(B, [0, 1023], [0, 1]), 2), i)
        fitness.append(t)

    return fitness


def ff_av(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][0])

    return numpy.mean(temp)


def ff_total(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][0])

    return sum(temp)


def ff_max(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][0])

    return max(temp)


def ff_min(ff_array):
    temp = []
    for x in range(len(ff_array)):
        temp.append(ff_array[x][0])
    return min(temp)


def select(ff):
    fit, ind = [], []  # will store only indices

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    # Python library random consists of a function which can select k elements of list according to given
    # weights, which is exactly the way proportionate selection works

    selected = random.choices(ind, probability, k=len(fit))
    return selected  # returns indices of selected individuals


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

            new_x.append(cross_part_1)
            new_x.append(cross_part_2)

            crossover_count += 1
            i -= 2

    return new_x


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


def save_elite(population, new_population):
    ff_now = ff(population)
    ff_new = ff(new_population)

    worst = min(ff_new, key=lambda tup: tup[0])
    best = max(ff_now, key=lambda tup: tup[0])

    new_population[worst[1]] = population[best[1]]
