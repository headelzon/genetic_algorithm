import random
import warnings
import genetic


n_elem = 10
population = 6

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

print('Initial ff: {}'.format(ff))

ff.sort(key=lambda tup: tup[0]) # sort ff by first digit in each tuple
print('Sorted ff: {}'.format(ff))

selected = genetic.select(ff)
print('Selected indices: {}'.format(selected))

x = genetic.mate(x, selected)
print('New population: {}'.format(x))

ff = genetic.ff(x)
print('New ff: {}'.format(ff))


