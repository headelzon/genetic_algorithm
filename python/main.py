# Genetic algorithm
# W. F. Koziak

import random
import warnings
import genetic
from matplotlib import pyplot

n_elem = 10
population = 30

mutation_prob = 0.02
crossover_prob = 0.85

if population % 2 != 0:
    warnings.warn('Population size should be even for algorithm to work properly!')

# Population initialization
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population)]

# Population evaluation
ff_init = genetic.ff(x)  # initial evaluation (distinguished for comparison later on)
ff_av_init = genetic.ff_av(ff_init)
ff_total_init = genetic.ff_total(ff_init)
ff_max_init = genetic.ff_max(ff_init)

# main algorithm
iterations = 1
mutation_count = 0

ff = ff_init  # ff used in the loop set to ff_init

ff_av_points, ff_max_points, ff_min_points, iteration_points = [], [], [], []

# while iterations < 100:
while genetic.ff_av(ff) != 10:

    # print('Iter: {}'.format(iterations))

    ff.sort(key=lambda tup: tup[0])  # sort ff by first digit in each tuple

    selected = genetic.select(ff)

    x = genetic.mate(x, selected)

    ff = genetic.ff(x)

    mutated = genetic.mutate(x, mutation_prob)

    if mutated:
        mutation_count += 1

    iterations += 1
    ff_av_points.append(genetic.ff_av(ff))
    ff_max_points.append(genetic.ff_max(ff))
    ff_min_points.append(genetic.ff_min(ff))
    iteration_points.append(iterations)


# TODO plots
pyplot.figure(1)
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()

pyplot.figure(2)
pyplot.hold(True)
pyplot.plot(iteration_points, ff_max_points, 'b-')
pyplot.plot(iteration_points, ff_min_points, 'r-')
pyplot.xlabel('Iterations')
pyplot.ylabel('Maximum and minimum fitness')
pyplot.grid(True)
pyplot.show()

print(iterations)
# print('Initial ff: {};\tFinal ff: {}'.format(ff_init, ff))
print('Initial average: {};\tFinal average: {}'.format(ff_av_init, genetic.ff_av(ff)))
print('No of mutations: {}'.format(mutation_count))

