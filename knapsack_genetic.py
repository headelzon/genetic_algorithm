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


# def select_roulette(ff):
#     fit, ind = [], []  # will store only indices
#
#     for j in range(len(ff)):
#         fit.append(ff[j][0])
#
#     for j in range(len(ff)):
#         ind.append(ff[j][1])
#
#     probability = []
#
#     for j in range(len(fit)):
#         probability.append(fit[j] / sum(fit))
#
#     # Python library random consists of a function which can select k elements of list according to given
#     # weights, which is exactly the way proportionate selection works
#
#     selected = random.choices(ind, probability, k=len(fit))
#     return selected  # returns indices of selected individuals


# def select_group(ff):
#
#     return selected