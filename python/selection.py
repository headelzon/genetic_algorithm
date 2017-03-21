import evaluate
import random


def select(ff):

    fit = []    # will store only values of fitness, without indices

    for j in range(len(ff)):
        fit.append(ff[j][0])

    probability = []

    for j in range(len(fit)):
        probability.append(fit[j]/sum(fit))

    # Python library random consists of a function which can select k elements of list according to given
    # weights, which is exactly the way proportionate selection works

    selected = random.choices(fit, probability, k=len(fit))
    return selected
