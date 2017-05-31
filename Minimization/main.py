import random
import genetic_min
from matplotlib import pyplot


# PARAMETERS INITIALIZATION
n_elem = 16  # Each x parameter is encoded in binary by a maximum of 3 bits
population_init = 100
mutation_prob = 0.05
crossover_prob = 0.8

a, c = [], []
for i in range(5):
    c.append(round(random.uniform(0.1, 0.7), 1))
    temp = []
    for j in range(4):
        temp.append(random.randint(1, 9))
    a.append(temp)

# print('a:')
# for x in range(5):
#     print(a[x])
#
# print('\nc:\n{}\n'.format(c))

# POPULATION INITIALIZATION
# Parameters values are generated as decimal
# and then converted to binary
# and saved into one list (matrix) x[]
# Each 4 bits represent one parameter x(i)

x = []
for w in range(population_init):
    x1 = []
    for i in range(4):
        x1_prim = random.randint(0, 10)
        x1_bin = "{0:b}".format(x1_prim)
        x1_list = list(x1_bin)

        while len(x1_list) < 4:
            x1_list.insert(0, '0')

        x1_list = [int(x) for x in x1_list]
        x1.extend(x1_list)
    x.append(x1)

answer = genetic_min.bruteforce(a, c)   # solution given as a list of x's
worst = answer[2]
best = answer[1]

ff_init = genetic_min.ff(a, c, x, worst, best)
ff_av_init = genetic_min.ff_av(ff_init)

b = max(ff_init, key=lambda tup: tup[0])
w = min(ff_init, key=lambda tup: tup[0])
diff = b[0] - w[0]

iterations = 0
mutation_count = 0
ff = ff_init
ff_av = ff_av_init
ff_av_points, iteration_points = [], []


for h in range(100):
    selected = genetic_min.select(ff)

    new_x = genetic_min.mate(x, selected, crossover_prob)
    genetic_min.save_elite(x, new_x, a, c, worst, best)
    x = new_x

    mutated = genetic_min.mutate(x, mutation_prob)
    if mutated:
        mutation_count += 1

    ff = genetic_min.ff(a, c, x, worst, best)
    ff_av = genetic_min.ff_av(ff)

    iterations += 1
    iteration_points.append(iterations)
    ff_av_points.append(ff_av)

print(answer)
# genetic_min.print_parameters(a, c, x, worst, best)
# print('Initial average: {}'.format(ff_av_init))
print('Average current: {}'.format(ff_av))
# print('Mutation count: {}'.format(mutation_count))

# GRAPHS
pyplot.figure(1)
pyplot.plot(iteration_points, ff_av_points)
pyplot.xlabel('Iterations')
pyplot.ylabel('Average fitness')
pyplot.grid(True)
pyplot.show()