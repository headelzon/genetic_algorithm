import random
import genetic


x = [[random.randint(0, 1) for i in range(10)] for b in range(6)]

for i in x:
    print(i)

ff = genetic.ff(x)
print('')
print(ff)
print('')

ff.sort(key=lambda tup: tup[0])
print(ff)
print('')

selected = genetic.select(ff)
print('')
print(selected)
print('')

print(x[selected[0]][:3])
print('')

mat = []
mat.extend(x[selected[0]][:3])
mat.extend(x[selected[1]][3:])
print(mat)