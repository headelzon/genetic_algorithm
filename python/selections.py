import random
import math


def select_roulette(ff):
    fit, ind = [], []  # will store only indices

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    selected = random.choices(ind, probability, k=len(fit))
    return selected  # returns indices of selected individuals


def select_basic(ff):
    fit, ind = [], []

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    selected, rests = [], []
    for i in range(len(fit)):
        n = math.floor(len(fit) * probability[i])
        l = [ind[i]] * n
        t = (len(fit) * probability[i] - n, i)
        rests.append(t)
        selected.extend(l)

    empty = len(fit) - len(selected)
    rests.sort(reverse=True, key=lambda tup: tup[0])

    b = rests[:empty]
    for i in range(empty):
        selected.append(b[i][1])

    return selected
