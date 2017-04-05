import random
import itertools
import knapsack_genetic as gen
import math


elements = 10
population = 10
data = []   # matrix containing info about elements (their wights and benefits)

weights, benefits = [], []
weight_limit = math.ceil((0.5 * (10*elements)) - (0.125 * (10*elements)))

for i in range(elements):
    weights.append(random.randint(1, 10))
    benefits.append(random.randint(1, 10))

data.append(weights)
data.append(benefits)

bin = [0, 1]
possible = list(itertools.product(range(2), repeat=elements))

ff_init = gen.ff_short(data, possible)

below_limit = []

for i in range(len(possible)):
    if ff_init[i][0] <= weight_limit:
        below_limit.append(possible[i])
    else:
        pass

ff = gen.ff_short(data, below_limit)

ff.sort(key=lambda x: x[1], reverse=True)

print('Maximum possible fitness: {}'.format(ff[0][1]))

