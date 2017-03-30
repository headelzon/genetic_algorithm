# Knapsack Problem using Genetic Algorithms
# W. F. Koziak

import random
import knapsack_genetic

elements = 4
population = 30
data = []   # matrix containing info about elements (their wights and benefits)

for i in range(elements):
    # t = (weight, benefit, index)
    t = (random.randint(1, 10), random.randint(1, 10), i)
    data.append(t)

print(data)

x = [[random.randint(0, 1) for i in range(elements)] for b in range(population)]

# TODO FITNESS FUNCTION
# for each 1 in chromosome add its benefit and weight to total benefit and total weight

# SELECTION
# genetic.select()
# TODO group selection

# CROSS-OVER
# from genetic.mate()

# MUTATION
# from genetic.mutate()

# STOPPING CONDITION
# until 90% of chromosomes are identical
