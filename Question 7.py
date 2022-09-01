r = 4
c = 3
a = []

for i in range(r):
    a.append([0]*c)
print("Part a")

for i in range(r):
    print(*a[i])

for i in range(r):
    if i == 0:
        a[i] = [1] * c
    else:
        a[i] = [3] * c
print("Part b")

for i in range(r):
    print(*a[i])

for i in range(r):
    a[i][0] = 2

for i in range(r):
    a[i][1] = a[i][0] * 2
    a[i][2] = a[i][1] * 2
print("Part c")

for i in range(r):
    print(*a[i])
