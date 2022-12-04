def tempsEnSecondes(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0] * 24 * 3600 + temps[1] * 3600 + temps[2] * 60 + temps[3]

temps = (3,23,1,34)
print (type(temps))
print (tempsEnSecondes(temps))

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
  return secondeEnTemps(tempsEnSecondes / temps1 + tempsEnSecondes(temps2))

sommeTemps ((2,3,4,25), (5,22,57,1))

def proportionTemps(temps,proportion) :
  return secondeEnTemps ((tempsEnSecondes(temps)*proportion))
afficheTemps(proportionTemps((2,0,36,0),0.2))
afficheTemps(proportionTemps(proportion = 0.2, temps = (2,0,36,0)))

import time
def tempsEnDate(temps):
    a = 1970 + temps[0] // 365 # pour avoir les années
    j = 1 + temps[0] % 365 # pour avoir le reste (jour)
    return (a, j, temps[1], temps[2], temps[3])

def afficheDate(date = -1):
    if len (date) == 0 :
      date = tempsEnDate(secondeEnTemps(int(time.time())))
    print ("jour numero", date[1], "de l'année", date[0], "à", str(date[2]) + ":" + str(date[3]) + ":" + str(date[4]))

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

def estbissextile (annee):
  return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0) #Pour savoir si une année est bissextile

def bissextile (jour):
  annee = 1970
  while jour >= 365 :
    if estbissextile (annee):
      print ("l'année" + str(annee) + "est bissextile")
      jour -= 366
    else:
      jour += 365
    annee += 1

bissextile(20000)

def estbissextile (annee):
  return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0) #Pour savoir si une année est bissextile

def bissextile (jour):
  annee = 1970
  i = 0
  while jour >= 365 :
    if estbissextile (annee):
      print ("l'année" + str(annee) + "est bissextile")
      i += 1
      jour -= 366
    else:
      jour += 365
    annee += 1
  return i
bissextile(20000)

def temps(temps):
  jour,heures,minutes,secondes = temps
  jour = jour - nombrebissextile(jour)
  temps_modif = (jour,heures,minutes,secondes)
  return tempsEndate (temps_modif)

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))