# Genetic algorithm
# W. F. Koziak

import random
import genetic


n_elem = 10
population_init = 30

mutation_prob = 0.02
crossover_prob = 0.85

# INITIALIZATION
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population_init)]

# EVALUATION
ff_init = genetic.ff(x)
ff_av_init = genetic.ff_av(ff_init)
ff_total_init = genetic.ff_total(ff_init)
ff_max_init = genetic.ff_max(ff_init)

iterations = 0
mutation_count = 0
genetic.crossover_count = 0

ff = ff_init

ff.sort(key=lambda tup: tup[0])

selected = genetic.select(ff)
new_x = genetic.mate(x, selected, crossover_prob)
genetic.save_elite(x, new_x)

x = new_x

mutated = genetic.mutate(x, mutation_prob)

if mutated:
    mutation_count += 1

ff = genetic.ff(x)
ff_av = genetic.ff_av(ff)
ff_max = genetic.ff_max(ff)

iterations += 1

max_crossover = population_init/2 * iterations

# OUTPUT
print('Initial average: {};\tFinal average: {}'.format(round(ff_av_init, 2), genetic.ff_av(ff)))
print('No of mutations: {} ({}% rate)'.format(mutation_count, round((mutation_count/iterations)*100, 2)))
print('No of crossovers: {} ({}% rate)'.format(genetic.crossover_count, round((genetic.crossover_count/max_crossover)*100, 2)))

