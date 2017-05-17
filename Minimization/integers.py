import random
import genetic
import binascii


n_elem = 16             # Each x parameter is encoded in binary by a maximum of 3 bits
population_init = 30
mutation_prob = 0.02
crossover_prob = 0.85

# INITIALIZATION
# Parameters values are generated as decimal
# and then converted to binary
# and saved into one list (matrix) x[]
# Each 4 bits represent one parameter x(i)

x = []
for i in range(4):
    x_prim = random.randint(0, 10)
    x_bin = "{0:b}".format(x_prim)
    x_list = list(x_bin)

    while len(x_list) < 4:
        x_list.insert(0, '0')

    x_list = [int(x) for x in x_list]
    x.extend(x_list)

print(x)

# # PRINT PARAMETERS X
# i = 0
# while i < 13:
#     y_prim = x[i:i+4]
#     y_prim = ''.join(map(str, y_prim))
#     y_prim = int(y_prim, 2)
#     print(y_prim)
#     i += 4

# Value estimation



# Fitness function: just invert the value of the function

# The rest is the same