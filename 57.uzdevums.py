from random import randint
MasivsB = [0,0,0,0,0,0,0,0]

for indekss in range(8):
    MasivsB[indekss] = randint(0,20)

for indekss in range(8):
    print(MasivsB[indekss], end='\t')