# Genetic algorithm test
# W. F. Koziak

import random
import knapsack_genetic as gen
import numpy
import math
from tqdm import tqdm

elements = 10
population = 10
data = []   # matrix containing info about elements (their wights and benefits)
weight_limit = math.ceil((0.5 * (10*elements)) - (0.125 * (10*elements)))
mutation_prob = 0.005
crossover_prob = 0.75

results = []
big_iterations = 1

for q in tqdm(range(10)):

    weights, benefits = [], []
    ff_av_points, iteration_points = [], []
    mutation_count = 0
    iteration_count = 1
    ff_av = 0

    for i in range(elements):
        weights.append(random.randint(1, 10))
        benefits.append(random.randint(1, 10))

    data.append(weights)
    data.append(benefits)

    max_possible = gen.test(data, elements, weight_limit)

    # data = [[weights], [benefits]]

    x = [[random.randint(0, 1) for i in range(elements)] for b in range(population)]

    # FITNESS FUNCTION
    ff_init = gen.ff(data, x, weight_limit)
    ff = ff_init

    while gen.ff_av(ff) < max_possible:
        # SELECTION
        selected = gen.select_roulette(ff)

        # CROSS-OVER
        new_x = gen.mate(x, selected, crossover_prob)
        # gen.save_elite(x, new_x, data, weight_limit)
        x = new_x

        # MUTATION
        mutated = gen.mutate(x, mutation_prob)

        if mutated:
            mutation_count += 1

        ff = gen.ff(data, x, weight_limit)
        ff_av = gen.ff_av(ff)
        iteration_count += 1

    results.append(iteration_count)

    big_iterations += 1

print('Average iteration number: {}'.format(numpy.mean(results)))

