from random import randint

A = [0] * 10

for indekss in range(10):
    A[indekss] = randint(5, 20)

print('Masīvs A:')
for indekss in range(10):
    print(A[indekss], end='\t')

print()
print()
print('Iegūto skaitļu virkne:')

for indekss in range(7):
    print(A[indekss] + A[indekss+1] + A[indekss+2], end='\t')