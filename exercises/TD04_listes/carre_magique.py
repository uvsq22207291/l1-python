#Question 1
# Il s'agit bien d'un carrée magique car la somme des nombres de chaque rangée, colonne et diagonale principale est égale. La constante magique est 34.

#Question 2
carre_mag = [[0] * 4 for i in range(4)]
for i in range(4) :
    for j in range(4) :
        if i == j :
            carre_mag [i][j] = 1
        elif i < j :
            carre_mag[i][j] = 2
            
for i in carre_mag:
    print(' '.join([str(j) for j in i]))
#OU
nombres = [4,14,15,1,9,7,6,12,5,11,10,8,16,2,3,13]
print(nombres[0:4])
print(nombres[4:8])
print(nombres[8:12])
print(nombres[12:16])
#OU
carre_mag = [
    [4,14,15,1],
    [9,7,6,12],
    [5,11,10,8],
    [16,2,3,13]
]

for i in range (len(carre_mag)) :
    for j in range (len(carre_mag[i])) :
        print (carre_mag[i][j], end= " ")
    print ()

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

nombres = [4,14,15,1,9,3,6,12,5,11,10,8,16,2,3,13]
print(nombres[0:4])
print(nombres[4:8])
print(nombres[8:12])
print(nombres[12:16])
#OU

carre_non_mag = [
    [4,14,15,1],
    [9,3,6,12],
    [5,11,10,8],
    [16,2,3,13]
]

for i in range (len(carre_non_mag)) :
    for j in range (len(carre_non_mag[i])) :
        print (carre_non_mag[i][j], end= " ")
    print ()

#Exercice 4
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    pass

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)
