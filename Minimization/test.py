import itertools
import random


o = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
possible = list(itertools.product(o, repeat=4))

a = [[2.61, 7.1, 5.0, 7.01], [3.13, 3.49, 4.7, 5.24], [1.27, 2.31, 3.75, 7.23], [5.48, 1.29, 5.91, 6.21], [6.34, 2.8, 3.44, 1.66]]
c = [0.42, 0.42, 0.59, 0.64, 0.19]

func, fitness = 0, []

for w in range(len(possible)):
    x = possible[w]
    denominator = []
    for i in range(5):
        temp = []
        for j in range(4):
            exp = pow((x[j] - a[i][j]), 2) + c[i]
            temp.append(exp)
        b = round(sum(temp), 4)
        denominator.append(b)

    fraction = []
    for i in range(5):
        fraction.append(1 / denominator[i])

    func = sum(fraction)
    t = (func, w)
    fitness.append(t)

print(len(fitness))
best = max(fitness, key=lambda tup: tup[0])
worst = min(fitness, key=lambda tup: tup[0])
print("{}, {}".format(best[0], list(possible[best[1]])))
print("{}, {}".format(worst[0], possible[worst[1]]))