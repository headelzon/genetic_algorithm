import numpy
import random


def ff(array):
    fitness = []
    for x in range(len(array)):
        t = ((sum(array[x])), x)        # values in fitness matrix are tuples (to store indices)
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


def select(ff):

    fit, ind = [], []    # will store only indices

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j]/sum(fit))

    # Python library random consists of a function which can select k elements of list according to given
    # weights, which is exactly the way proportionate selection works

    selected = random.choices(ind, probability, k=len(fit))
    return selected     # returns indices of selected individuals


def mate(population, selected):

    cross_point = random.randint(2, len(population[0]))

    i = len(population)-1

    new_x = []

    while i - 1 > -1:
        cross_part_1, cross_part_2 = [], []

        cross_part_1.extend(population[selected[i]][:cross_point])
        cross_part_1.extend(population[selected[i-1]][cross_point:])

        cross_part_2.extend(population[selected[i-1]][:cross_point])
        cross_part_2.extend(population[selected[i]][cross_point:])


        new_x.append(cross_part_1)
        new_x.append(cross_part_2)

        i -= 2

    return new_x