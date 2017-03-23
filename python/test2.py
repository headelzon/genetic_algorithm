def change(x):
    x[2] = 2
    return True

x = [1, 1, 0, 1, 0, 0, 0]

d = change(x)
print(d)
print(x)