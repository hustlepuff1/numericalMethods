a = []

b = []

for i in range(1, 10):
    for j in range(1, 10):
        ans = i * j
        a.append(ans)
    b.append(a)
print(b)
