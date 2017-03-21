# Genetic algorithm
# W. F. Koziak

import random
import warnings
import genetic


n_elem = 10
population = 30

if population % 2 != 0:
    warnings.warn('Population size should be even for algorithm to work properly!')

# Population initialization
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population)]

# Population evaluation
ff_init = genetic.ff(x)        # initial evaluation (distinguished for comparison later on)
ff_av_init = genetic.ff_av(ff_init)
ff_total_init = genetic.ff_total(ff_init)
ff_max_init = genetic.ff_max(ff_init)

# main algorithm
iterations = 0
ff = ff_init                    # ff used in the loop set to ff_init


while iterations < 100:

    # print('Iter: {}'.format(iterations))

    ff.sort(key=lambda tup: tup[0]) # sort ff by first digit in each tuple

    selected = genetic.select(ff)

    x = genetic.mate(x, selected)

    ff = genetic.ff(x)

    iterations+=1


print(iterations)
# print('Initial ff: {};\tFinal ff: {}'.format(ff_init, ff))
print('Initial average: {};\tFinal average: {}'.format(ff_av_init, genetic.ff_av(ff)))

# TODO plots