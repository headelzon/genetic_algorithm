# Genetic algorithm test
# W. F. Koziak

import random
import knapsack_genetic as gen
from matplotlib import pyplot
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
big_iterations_points = []

for q in tqdm(range(1000)):

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

    # data = [[weights], [benefits]]

    x = [[random.randint(0, 1) for i in range(elements)] for b in range(population)]

    # FITNESS FUNCTION
    ff_init = gen.ff(data, x, weight_limit)
    ff = ff_init

    while iteration_count < 100:
        # SELECTION
        selected = gen.select_roulette(ff)
        # TODO group selection

        # CROSS-OVER
        new_x = gen.mate(x, selected, crossover_prob)
        gen.save_elite(x, new_x, data, weight_limit)
        x = new_x

        # MUTATION
        mutated = gen.mutate(x, mutation_prob)

        if mutated:
            mutation_count += 1

        ff = gen.ff(data, x, weight_limit)
        ff_av = gen.ff_av(ff)
        iteration_count += 1

    results.append(ff_av)

    big_iterations += 1
    big_iterations_points.append(big_iterations)

print('Max value: {}'.format(max(results)))

pyplot.figure(1)
pyplot.plot(big_iterations_points, results)
pyplot.xlabel('Iterations')
pyplot.ylabel('Achieved max fitness')
pyplot.grid(True)
pyplot.show()