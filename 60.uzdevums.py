x = [0] * 10

for number in range(10):
    x[number] = int(input('Ievadiet' + str(number + 1) + '.skaitli:'))

summa = 0
for number in range(10):
    summa = summa + x[number]

print()
print(f'Ievadīto skaitļu vidēja vērtība ir {summa/10:0.2f}')