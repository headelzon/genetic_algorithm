import scheduling_module
import random
import numpy


periods = 4
units = 7
capacity = [20, 15, 35, 40, 15, 15, 10]
max_cap = [80, 90, 65, 70]
population = 5

if len(max_cap) != periods:
    raise ValueError('Number of periods is wrong')

no_elem = periods * units


x = [[random.randint(0, 1) for i in range(no_elem)] for b in range(population)]
# print('Population initialized: {} elements.\n'.format(population))

ff = scheduling_module.ff(x, capacity, max_cap)

# temp = []
# for i in range(4):
#     temp.append(x[0][i * 7:(i * 7) + 7])
#
# print()
# for i in range(4):
#     print(temp[i])

print(ff)

