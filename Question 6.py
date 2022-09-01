print("first nested loop\n")

for i in range(1, 8):
    for j in range(1, i+1):
        print('*', end='')
    print()

print("\nsecond nested loop\n")

for i in range(7, 0, -1):
    for j in range(1, i+1):
        print('*', end='')
    print()
