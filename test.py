import random
import genetic
import math

n_elem = 10
population_init = 30

# INITIALIZATION
x = [[random.randint(0, 1) for i in range(n_elem)] for b in range(population_init)]
ff = genetic.ff(x)

fit, ind = [], []

for j in range(len(ff)):
    fit.append(ff[j][0])

for j in range(len(ff)):
    ind.append(ff[j][1])

probability = []

for j in range(len(fit)):
    probability.append(fit[j] / sum(fit))

selected, rests = [], []
for i in range(len(fit)):
    n = math.floor(len(fit) * probability[i])
    l = [ind[i]] * n
    selected.extend(l)
    t = (len(fit) * probability[i] - n, i)
    rests.append(t)

print(selected)

empty = len(fit) - len(selected)

fit, ind, probability, l = [], [], [], []

for j in range(len(rests)):
    fit.append(rests[j][0])

for j in range(len(rests)):
    ind.append(rests[j][1])

for j in range(len(fit)):
    probability.append(fit[j] / sum(fit))

for i in range(empty):
    p = random.choices(ind, probability)
    p = p[0]
    if p in l:
        while p in l:
            p = random.choices(ind, probability)
            p = p[0]
        l.append(p)
    else:
        l.append(p)

selected.extend(l)

print(selected)