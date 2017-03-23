import random
import genetic
from matplotlib import pyplot


n_elem = 10
population = 30
mutation_prob = 0.02
crossover_prob = 0.85
iterations = 1
mutation_count = 0
genetic.crossover_count = 0


# INITIALIZATION
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population)]

# EVALUATION
ff = genetic.ff(x)  # initial evaluation (distinguished for comparison later on)
ff_av_init = genetic.ff_av(ff)
ff_av_points, iteration_points = [], []

while iterations < 100:
    ff.sort(key=lambda tup: tup[0])
    selected = genetic.select(ff)

    x = genetic.mate(x, selected, crossover_prob)

    mutated = genetic.mutate(x, mutation_prob)

    if mutated:
        mutation_count += 1

    ff = genetic.ff(x)
    ff_av = genetic.ff_av(ff)

    iterations += 1
    ff_av_points.append(genetic.ff_av(ff))
    iteration_points.append(iterations)

pyplot.figure(1)
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()

max_crossover = population/2 * iterations

print('Iterations: {}'.format(iterations))
print('Initial average: {};\tFinal average: {}'.format(round(ff_av_init, 2), round(genetic.ff_av(ff), 2)))
print('No of mutations: {} ({}% rate)'.format(mutation_count, round((mutation_count/iterations)*100, 2)))
print('No of crossovers: {} ({}% rate)'.format(genetic.crossover_count, round((genetic.crossover_count/max_crossover)*100, 2)))
