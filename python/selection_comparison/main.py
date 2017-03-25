# Genetic algorithm
# W. F. Koziak

import random
import warnings
import genetic_v2
from matplotlib import pyplot


n_elem = 10
population = 100

mutation_prob = 0.02
crossover_prob = 0.85

if population % 2 != 0:
    warnings.warn('Population size should be even for algorithm to work properly!')

# INITIALIZATION
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population)]

# EVALUATION
ff_init = genetic_v2.ff(x)  # initial evaluation (distinguished for comparison later on)
ff_av_init = genetic_v2.ff_av(ff_init)
ff_total_init = genetic_v2.ff_total(ff_init)
ff_max_init = genetic_v2.ff_max(ff_init)

iterations = -1
mutation_count = 0
genetic_v2.crossover_count = 0

ff = ff_init  # ff used in the loop set to ff_init
ff_av = ff_av_init

ff_av_points, ff_max_points, ff_total_points, iteration_points = [], [], [], []

# MAIN LOOP
while ff_av < 1:          # repeat until all individuals have fitness = 10

    ff.sort(key=lambda tup: tup[0])     # sort ff by first digit in each tuple

    selected = genetic_v2.select_roulette(ff)

    x = genetic_v2.mate(x, selected, crossover_prob)

    mutated = genetic_v2.mutate(x, mutation_prob)

    if mutated:
        mutation_count += 1

    ff = genetic_v2.ff(x)
    ff_av = genetic_v2.ff_av(ff)
    ff_max = genetic_v2.ff_max(ff)

    iterations += 1
    ff_av_points.append(ff_av)
    ff_max_points.append(ff_max)
    ff_total_points.append(genetic_v2.ff_total(ff))

    iteration_points.append(iterations)

max_crossover = population/2 * iterations

# OUTPUT
print('Iterations: {}'.format(iterations))
print('Initial average: {};\tFinal average: {}'.format(round(ff_av_init, 2), genetic_v2.ff_av(ff)))
print('No of mutations: {} ({}% rate)'.format(mutation_count, round((mutation_count/iterations)*100, 2)))
print('No of crossovers: {} ({}% rate)'.format(genetic_v2.crossover_count, round((genetic_v2.crossover_count/max_crossover)*100, 2)))

# GRAPHS
pyplot.figure(1)
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()

pyplot.figure(2)
pyplot.plot(iteration_points, ff_max_points, 'r')
pyplot.xlabel('Iterations')
pyplot.ylabel('Maximum fitness')
pyplot.grid(True)
pyplot.show()
