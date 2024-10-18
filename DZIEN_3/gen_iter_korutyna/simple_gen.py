def generuj(k):
    for i in range(k):
        yield 1.6*i-0.3

h = generuj(5)

# print(list(h))
print(len(list(h)))
for p in h:
    print(p)

print(len(list(h)))
