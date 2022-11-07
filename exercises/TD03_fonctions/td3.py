def tempsEnSecondes(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]

temps = (3,23,1,34)
print (type(temps))
print (tempsEnSeconde(temps))

def secondeEnTemps(secondes):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = secondes // (24*3600)
    heures = (secondes % (24*3600)) // 3600
    minutes = (secondes % (24*3600)) % 3600 // 60
    secondes = (secondes %  (24*3600)) % 3600 % 60
    return (jours, heures, minutes, secondes)

temps = secondeEnTemps(100000)
print (temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

def affichepluriel(mots,nb) :
    if nb > 0 :
      print ("", nb, mots, end = "")
    if nb > 1 :
      print ("s", end = "")

def afficheTemps(temps) :
    affichepluriel ("jour", temps[0])
    affichepluriel ("heure", temps[1])
    affichepluriel ("minute", temps[2])
    affichepluriel ("seconde", temps[3])

afficheTemps((1,0,14,23))

def demandeTemps():
    j = -1
    h = -1
    m = -1
    s = -1
    while j < 0 :
      j = int(input("entrez un nombre"))
    while (h < 0 or h >= 24) :
      h = int(input("entrez un nombre"))
    while (m < 0 or m >= 60) :
      m = int(input("entrez un nombre"))
    while (s < 0 or s >= 60) :
      s = int(input("entrez une seconde"))
    return (j, h, m, s)

afficheTemps(demandeTemps())

def sommeTemps(temps1, temps2):
  return secondeenTemps(tempsenSeconde) \ (temps1) + tempsEnSeconde(temps2)

sommeTemps ((2,3,4,25), (5,22,57,1))

def proportionTemps(temps,proportion) :
  return secondeenTemps ((TempsenSeconde(temps)*proportion))
afficheTemps (proportionTemps((2,0,36,0),0,2))
afficheTemps (proportionTemps(proportion = 0,2, temps = (2,0,36,0)))
