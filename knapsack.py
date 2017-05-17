# Knapsack Problem using Genetic Algorithms
# W. F. Koziak

import random
import knapsack_genetic as gen
from matplotlib import pyplot
import math


elements = 10
population = 50
data = []   # matrix containing info about elements (their wights and benefits)
weight_limit = math.ceil((0.5 * (10*elements)) - (0.3 * (10*elements)))
mutation_prob = 0.02
crossover_prob = 0.75

weights, benefits = [], []
ff_av_points, iteration_points = [], []
mutation_count = 0
iteration_count = 1

for i in range(elements):
    weights.append(random.randint(1, 10))
    benefits.append(random.randint(1, 10))

data.append(weights)
data.append(benefits)

max_possible = gen.test(data, elements, weight_limit)

print('Weights: {}'.format(data[0]))
print('Values: {}'.format(data[1]))
print('Obtained result: {}'.format(max_possible))

# data = [[weights], [benefits]]
x = [[random.randint(0, 1) for a in range(elements)] for b in range(population)]

# FITNESS FUNCTION
ff_init = gen.ff(data, x, weight_limit)
print('Initial average fitness: {}'.format(gen.ff_av(ff_init)))

ff = ff_init

while gen.ff_av(ff) < max_possible:
    # SELECTION
    selected = gen.select_rest_rep(ff)

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

    ff_av_points.append(ff_av/max_possible)
    iteration_points.append(iteration_count)

ff_av = (gen.ff_av(ff))/max_possible

print('Final average fitness: {}'.format(ff_av))
print('Mutations: {}'.format(mutation_count))
print('Iterations: {}'.format(iteration_count))

print('Weights: {}'.format(data[0]))
print('Values: {}'.format(data[1]))
print('Obtained result: {}'.format(x[0]))

# GRAPHS
pyplot.figure(1)
pyplot.axhline(y=1, xmin=0, xmax=101, linewidth=2, color='r')
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()
