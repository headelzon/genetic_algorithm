def change(x, i):
    x[i] = 2
    global count
    count += 1
    return True

x = [1, 1, 0, 1, 0, 0, 0]
count = 0

for i in range(5):
    change(x, i)

print(x)
print(count)