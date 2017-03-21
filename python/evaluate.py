import numpy


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
