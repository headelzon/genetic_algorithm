# Genetic algorithm test
# W. F. Koziak

import random
import genetic
import selections
import numpy
from tqdm import tqdm

n_elem = 10
population_init = 30

mutation_prob = 0.02
crossover_prob = 0.85

for w in range(1, 6):
    print('Take {}'.format(w))

    if w == 1:
        method = 'roulette'
    elif w == 2:
        method = 'basic deterministic'
    elif w == 3:
        method = 'rest with repeating'
    elif w == 4:
        method = 'rest without repeating'
    else:
        method = 'rank tournament'

    print('Selection method: ' + method)
    results = []

    for q in tqdm(range(100)):

        # INITIALIZATION
        x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population_init)]

        # EVALUATION
        ff_init = genetic.ff(x)  # initial evaluation (distinguished for comparison later on)
        ff_av_init = genetic.ff_av(ff_init)
        ff_total_init = genetic.ff_total(ff_init)
        ff_max_init = genetic.ff_max(ff_init)

        iterations = -1
        mutation_count = 0
        genetic.crossover_count = 0

        ff = ff_init  # ff used in the loop set to ff_init
        ff_av = ff_av_init

        ff_av_points, ff_max_points, ff_total_points, iteration_points = [], [], [], []

        # MAIN LOOP
        while ff_av < 1:

            ff.sort(key=lambda tup: tup[0])

            if w == 1:
                selected = selections.select_roulette(ff)
            elif w == 2:
                selected = selections.select_basic(ff)
            elif w == 3:
                selected = selections.select_rest_rep(ff)
            elif w == 4:
                selected = selections.select_rest_norep(ff)
            else:
                selected = selections.select_rank(ff)

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
            ff_av_points.append(ff_av)
            ff_max_points.append(ff_max)
            ff_total_points.append(genetic.ff_total(ff))

            iteration_points.append(iterations)

        results.append(iterations)

    iter_av = numpy.mean(results)

    print('Average iteration number: {}'.format(iter_av))
