import itertools


def bruteforce(a, c):
    o = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    possible = list(itertools.product(o, repeat=4))

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

    best = max(fitness, key=lambda tup: tup[0])
    worst = min(fitness, key=lambda tup: tup[0])
    t = (list(possible[best[1]]), best[0], worst[0])
    return t


chromosome = [4, 4, 4, 4]
a = [[7, 7, 1, 9], [8, 2, 7, 5], [9, 7, 1, 8], [9, 1, 8, 8], [4, 3, 5, 7]]
c = [0.3, 0.2, 0.2, 0.6, 0.2]

denominator = []
for i in range(5):
    temp = []
    for j in range(4):
        exp = pow((chromosome[j] - a[i][j]), 2) + c[i]
        temp.append(exp)
    b = round(sum(temp), 4)
    denominator.append(b)

fraction = []
for i in range(5):
    fraction.append(1 / denominator[i])

func = sum(fraction)
print(func)

print(bruteforce(a, c))