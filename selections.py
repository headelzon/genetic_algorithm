import random
import math


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
        selected.extend(l)
        t = (len(fit) * probability[i] - n, i)
        rests.append(t)

    empty = len(fit) - len(selected)
    rests.sort(reverse=True, key=lambda tup: tup[0])

    b = rests[:empty]
    for i in range(empty):
        selected.append(b[i][1])

    return selected


def select_rest_rep(ff):
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


def select_rest_norep(ff):
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
        selected.extend(l)
        t = (len(fit) * probability[i] - n, i)
        rests.append(t)

    empty = len(fit) - len(selected)

    fit, ind, probability, l = [], [], [], []

    for j in range(len(rests)):
        fit.append(rests[j][0])

    for j in range(len(rests)):
        ind.append(rests[j][1])

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    for i in range(empty):
        p = random.choices(ind, probability)
        p = p[0]
        if p in l:
            while p in l:
                p = random.choices(ind, probability)
                p = p[0]
            l.append(p)
        else:
            l.append(p)

    selected.extend(l)

    return selected


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
    return selected


def select_rank(ff):
    fit, ind = [], []

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability, selected = [], []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    while len(selected) < len(ff):
        for i in range(3):
            competitors = []
            p = random.choices(ind, probability)
            p = p[0]
            if p in competitors:
                while p in competitors:
                    p = random.choices(ind, probability)
                    p = p[0]
                competitors.append(p)
            else:
                competitors.append(p)

        fit2 = [(fit[y], y) for y in competitors]
        winner = max(fit2, key=lambda tup: tup[0])
        selected.append(winner[1])

    return selected
