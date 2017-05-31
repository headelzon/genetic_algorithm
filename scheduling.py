import random
import scheduling_module


periods = 4
units = 7
capacity = [20, 15, 35, 40, 15, 15, 10]
max_cap = [80, 90, 65, 70]

crossover_prob = 0.8
mutation_prob = 0.02

if len(max_cap) != periods:
    raise ValueError('Number of periods is wrong')

no_elem = periods * units
population = 10

x = [[random.randint(0, 1) for i in range(no_elem)] for b in range(population)]
# x = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print('Population initialized: {} elements.\n'.format(population))

x = scheduling_module.check_conditions(x)

ff_init = scheduling_module.ff(x, capacity, max_cap)
ff_av_init = scheduling_module.ff_av(ff_init)

print('Initial fitness average: {}'.format(round(ff_av_init, 2)))

# TODO selection, crossover, main loop

ff = ff_init

# main loop begin

selected = scheduling_module.select_rank(ff)                    # selection
new_x = scheduling_module.mate(x, selected, crossover_prob)     # cross-over
scheduling_module.save_elite(x, new_x)                          # save elite
x = new_x



# main loop end
