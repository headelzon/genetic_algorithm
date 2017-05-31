import random
import scheduling_module
from matplotlib import pyplot


periods = 4
units = 7
capacity = [20, 15, 35, 40, 15, 15, 10]
max_cap = [80, 90, 65, 70]
population = 1000

crossover_prob = 0.8
mutation_prob = 0.02

if len(max_cap) != periods:
    raise ValueError('Number of periods is wrong')

no_elem = periods * units

x = [[random.randint(0, 1) for i in range(no_elem)] for b in range(population)]
# x = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print('Population initialized: {} elements.\n'.format(population))

x = scheduling_module.check_conditions(x)

ff_init = scheduling_module.ff(x, capacity, max_cap)
ff_av_init = scheduling_module.ff_av(ff_init)

print('Initial fitness average: {}'.format(round(ff_av_init, 2)))

# TODO selection, crossover, main loop

ff = ff_init
ff_av = ff_av_init
mutation_count = 0
iterations = 0
ff_av_points, iteration_points = [], []

# main loop begin
while ff_av < 1:
    selected = scheduling_module.select_rank(ff)                    # selection
    new_x = scheduling_module.mate(x, selected, crossover_prob)     # cross-over

    scheduling_module.save_elite(x, new_x, capacity, max_cap)                          # save elite
    x = new_x
    mutated = scheduling_module.mutate(x, mutation_prob)            # mutation

    if mutated:
        mutation_count += 1

    ff = scheduling_module.ff(x, capacity, max_cap)                 # stats
    ff_av = scheduling_module.ff_av(ff)
    ff_av_points.append(ff_av)
    iteration_points.append(iterations)
    iterations += 1

    if iterations % 100 == 0:
        print('Iterations: {}\tff_av = {}'.format(iterations, ff_av))

    if iterations == 2000:
        break

# main loop end

# OUTPUT
print('Iterations: {}'.format(iterations))
print('Initial average: {};\tFinal average: {}'.format(round(ff_av_init, 2), ff_av))
print('No of mutations: {}'.format(mutation_count))

# PLOTS
pyplot.figure(1)
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()

# record high: 0.7541666666666664