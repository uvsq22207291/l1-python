#Question 1
# Il s'agit bien d'un carrée magique car la somme des nombres de chaque rangée, colonne et diagonale principale est égale. La constante magique est 34.

#Question 2
carre_mag = [[0] * 4 for i in range(4)]
for i in range(4) :
    for j in range(4) :
        if i == j :
            carre_mag[i][j] = 1
        elif i < j :
            carre_mag[i][j] = 2
            
for i in carre_mag:
    print(' '.join([str(j) for j in i]))

#Question 3
carre_pas_mag = [[0] * 4 for i in range(4)]
for i in range(4) :
    for j in range(4) :
        if i == j :
            carre_pas_mag[i][j] = 4
        elif i < j :
            carre_pas_mag[i][j] = 2
            
for i in carre_pas_mag:
    print(' '.join([str(j) for j in i]))