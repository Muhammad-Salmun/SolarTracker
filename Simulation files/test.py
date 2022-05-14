L = []
x=1
y=2
z=3
n=4
for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j != n and i + k != n and k + j != n and i + j + k != n:
                L.append([i, j, k])
print(L)