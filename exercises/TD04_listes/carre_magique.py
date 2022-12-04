#Question2
carre_mag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]

#Question3
carre_pas_mag = []
for lignes in carre_mag:
  carre_pas_mag.append(lignes.copy())
carre_pas_mag [3][2] = 7

#Question4
def affichecarre(carre):
  for i in carre :
    print (i)
  print ()
affichecarre(carre_mag)
affichecarre(carre_pas_mag)

#Question5
def testlignesegales(carre):
  somme = sum(carre[0])
  for lignes in carre :
    if sum(lignes) != somme :
      return -1
  return somme
print (testlignesegales(carre_mag))
print (testlignesegales(carre_pas_mag))

#Question6
def testcolonnes(carre):
  colonne_1 = [lignes[0] for lignes in carre]
  somme = sum (colonne_1)
  for j in range (1, len(carre)):
    colonne = [lignes[j] for lignes in carre]
    if sum(colonne) != somme :
      return -1
  return somme
print(testcolonnes(carre_mag))
print(testcolonnes(carre_pas_mag))

#Question7
def testdiagonalesegales(carre):
  taille = len(carre)
  diagonale_1 = [carre[i][i] for i in range (taille)]
  diagonale_2 = [carre[i][taille - i - 1] for i in range (taille)]
  somme = sum(diagonale_1)
  if sum (diagonale_2) != somme :
    return -1
  else :
    return somme
print(testdiagonalesegales(carre_mag))
print(testdiagonalesegales(carre_pas_mag))

#Question8
def estcarremagique(carre):
  return testlignesegales(carre) == testcolonnes(carre) and testlignesegales(carre) == testdiagonalesegales(carre) and testlignesegales(carre) != -1
print(estcarremagique(carre_mag))
print(estcarremagique(carre_pas_mag))

#Question9
def estnormal(carre):
  liste = []
  for lignes in carre :
    liste.extend(lignes)
  taille = len(carre)
  for entier in range (1, taille * taille + 1) :
    if entier not in liste :
      return False
  return True
print(estnormal(carre_mag))
print(estnormal(carre_pas_mag))