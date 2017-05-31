import numpy


benefit = 2
max_benefit = 2.7

t = numpy.interp(benefit, [2, max_benefit], [0, 1])

print(t)