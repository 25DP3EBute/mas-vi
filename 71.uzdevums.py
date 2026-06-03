a = [ [" " for kolona in range(2)] for rinda in range(2) ]  # masīvs 2x2

# Sākuma kara lauks ir tukšs.
a[0][0] = '0'
a[0][1] = '0'
a[1][0] = '0'
a[1][1] = '0'

for m in range(2) :
    i = int( input('Pirmais spēlētājs, ievadi ' + str(m + 1) + ' kuģa koordinātas x, y:') )
    j = int( input() )
    a[i][j] = 'k'

# attīrīt
for attirit in range(100) :
    print()

trap = 0
for m in range(2) :
    i = int( input('Otrais spēlētājs, ievadi šāviena koordinātas x, y:') )
    j = int( input() )
    if a[i][j] == 'k' :
        trap = trap + 1
        a[i][j] = 'x'
    else :
        a[i][j] = 'm'

print()