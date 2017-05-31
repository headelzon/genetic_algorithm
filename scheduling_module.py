import numpy
import random


def check_conditions(pop):
    new_pop = []

    for chromosome in pop:
        chromosome = continuity(chromosome)
        chromosome = was_checked(chromosome)
        new_pop.append(chromosome)

    return new_pop


def was_checked(chromosome):
    temp = []
    for i in range(4):
        temp.append(chromosome[i * 7:(i * 7) + 7])

    # if unit was maintained in previous intervals, the unit should be left on for the rest of the time
    # due to complications, a unit should be on in at least one interval

    for i in range(4):
        for j in range(0, 2):
            if temp[i][j] == 0:
                for k in range(2 - i):
                    temp[i + k + 2][j] = 1

    if temp[3][0] == 0 and temp[2][0] != 0:
        temp[2][0] = 0

    if temp[3][1] == 0 and temp[2][1] != 0:
        temp[2][1] = 0

    col = [[], [], [], [], [], [], []]

    for i in range(4):
        for j in range(7):
            col[j].append(temp[i][j])

    for j in range(7):
        if sum(col[j]) == 0:
            choice_interval = random.sample([0, 1, 2, 3], 2)
            temp[choice_interval[0]][j] = 1
            temp[choice_interval[1]][j] = 1
        elif sum(col[j]) == 1:
            zeros = []
            for z in range(len(col[j])):
                if col[j][z] == 0:
                    zeros.append(z)
            choice_interval = random.choice(zeros)
            temp[choice_interval][j] = 1

    x_new = []
    for i in range(4):
        x_new.extend(temp[i])
    return x_new


def continuity(chromosome):
    temp = []
    for i in range(4):
        temp.append(chromosome[i * 7:(i * 7) + 7])

    col = [[], [], [], [], [], [], []]

    for i in range(4):
        for j in range(7):
            col[j].append(temp[i][j])

    for j in range(7):
        if sum(col[j]) >= 3:
            ones = []
            for z in range(len(col[j])):
                if col[j][z] == 1:
                    ones.append(z)
            choice_interval = random.choice(ones)
            temp[choice_interval][j] = 0

    for i in range(3):
        if temp[i][0] == 0:
            temp[i + 1][0] = 0
        if temp[i][1] == 0:
            temp[i + 1][1] = 0

    x_new = []
    for i in range(4):
        x_new.extend(temp[i])
    return x_new


def ff(pop, weights, capacities):
    fitness = []

    for q in range(len(pop)):

        temp = []
        for i in range(4):
            temp.append(pop[q][i * 7:(i * 7) + 7])

        temp_cost = 0
        for i in range(4):
            total_power = 0
            for j in range(7):
                total_power += temp[i][j] * weights[j]
            temp_cost += capacities[i] - total_power

        max_power = sum(weights)
        max_temp_cost = []
        for i in range(4):
            max_temp_cost.append(capacities[i] - max_power)

        max_cost = sum(max_temp_cost)
        min_cost = sum(capacities)

        col = [[], [], [], [], [], [], []]

        for i in range(4):
            for j in range(7):
                col[j].append(temp[i][j])

        col_benefit, benefit = 0, 0
        for i in range(4):
            col_benefit += sum(temp[i])
        benefit = col_benefit / 7

        max_benefit = ((5 * 3) + 4) / 7
        # max benefit when all machines are turned on 3 times per cycle (excluding 1 and 2, which are always turned
        # on only 2 times)
        # min benefit = 2, when all machines run only 2 times per cycle

        benefit = numpy.interp(benefit, [2, max_benefit], [0, 1])
        cost = numpy.interp(temp_cost, [max_cost, min_cost], [0, 1])

        fit = numpy.interp(benefit + cost, [0, 2], [0, 1])

        fitness.append((fit, q))

    return fitness


def ff_av(ff):
    temp = []
    for x in range(len(ff)):
        temp.append(ff[x][0])

    return numpy.mean(temp)


def select_rank(ff):
    fit, ind = [], []

    for j in range(len(ff)):
        fit.append(ff[j][0])

    for j in range(len(ff)):
        ind.append(ff[j][1])

    probability, selected = [], []

    for j in range(len(fit)):
        probability.append(fit[j] / sum(fit))

    while len(selected) < len(ff):
        for i in range(3):
            competitors = []
            p = random.choices(ind, probability)
            p = p[0]
            if p in competitors:
                while p in competitors:
                    p = random.choices(ind, probability)
                    p = p[0]
                competitors.append(p)
            else:
                competitors.append(p)

        fit2 = [(fit[y], y) for y in competitors]
        winner = max(fit2, key=lambda tup: tup[0])
        selected.append(winner[1])

    return selected


def mate(population, selected, crossover_prob):

    i = len(population) - 1

    new_x = []

    while i - 1 > -1:

        if random.uniform(0, 1) > crossover_prob:
            new_x.append(population[selected[i]])
            new_x.append(population[selected[i-1]])
            i -= 2
            continue
        else:
            cross_point = random.randint(2, len(population[0]))

            cross_part_1, cross_part_2 = [], []

            cross_part_1.extend(population[selected[i]][:cross_point])
            cross_part_1.extend(population[selected[i - 1]][cross_point:])

            cross_part_2.extend(population[selected[i - 1]][:cross_point])
            cross_part_2.extend(population[selected[i]][cross_point:])

            new_x.append(cross_part_1)
            new_x.append(cross_part_2)

            i -= 2

    return new_x


def mutate(population, mutation_prob):

    mut = random.uniform(0, 1)

    if mut <= mutation_prob:
        selected_indiv = random.randint(0, len(population) - 1)
        selected_bit = random.randint(0, len(population[0]) - 1)

        if population[selected_indiv][selected_bit] == 0:
            population[selected_indiv][selected_bit] = 1
        else:
            population[selected_indiv][selected_bit] = 0

        return True

    else:
        return False


def save_elite(population, new_population, weights, capacities):
    ff_now = ff(population, weights, capacities)
    ff_new = ff(new_population, weights, capacities)

    worst = min(ff_new, key=lambda tup: tup[0])
    best = max(ff_now, key=lambda tup: tup[0])

    new_population[worst[1]] = population[best[1]]