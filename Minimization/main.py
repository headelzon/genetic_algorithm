import random
import genetic_min


# PARAMETERS INITIALIZATION
n_elem = 16  # Each x parameter is encoded in binary by a maximum of 3 bits
population_init = 30
mutation_prob = 0.02
crossover_prob = 0.85

a, c = [], []
for i in range(5):
    c.append(round(random.uniform(0.1, 0.7), 2))
    temp = []
    for j in range(4):
        temp.append(round(random.uniform(1, 9), 2))
    a.append(temp)

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
# # PRINT PARAMETERS X
# i, x = 0, []
# while i < 13:
#     y_prim = x1[i:i + 4]
#     y_prim = ''.join(map(str, y_prim))
#     y_prim = int(y_prim, 2)
#     x.append(y_prim)
#     i += 4
# print('Parameters: {}'.format(x))

ff_init = genetic_min.ff(a, c, x)
ff_av_init = genetic_min.ff_av(ff_init)

selected = genetic_min.select(ff_init)

x = genetic_min.mate(x, selected, crossover_prob)

ff = genetic_min.ff(a, c, x)
ff_av = genetic_min.ff_av(ff)
