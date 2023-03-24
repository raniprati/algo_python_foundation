doors = [False] * 101

for j in range(1, 101):
    for i in range(1, 101, j):
        doors[j] = not doors[j]

open = 0
for i in range(1, 101):
    if doors[i]:
        print("Open door: ", i)
        open += 1

print("No. of open doors = ", open)
