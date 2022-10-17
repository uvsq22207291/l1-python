#Question 1
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jours_en_secondes = temps[0] * 86400
    heures_en_secondes = temps[1] * 3600
    minutes_en_secondes = temps[2] * 60
    secondes = temps[3]
    pass
    return (jours_en_secondes + heures_en_secondes + minutes_en_secondes + secondes)

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps)) 

#Question 2
def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    minutes = seconde // 60
    seconde %= 60
    heures = minutes // 60
    minutes %= 60
    jours = heures // 24
    heures %= 24
    pass
    return (jours, heures, minutes,seconde)

temps = secondeEnTemps(10000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#Question 3

def afficheTemps(temps):
    if jours and heures and minutes and secondes > 1 :
        print ('jours', 'heures', 'minutes', 'secondes')
    jours = afficheTemps[0]
    heures = afficherTemps[1]
    minutes = afficherTemps[2]
    secondes = afficherTemps[3]
    return (jours,heures,minutes,secondes)
    
    pass
print (afficheTemps(temps))
afficheTemps = (1,0,14,23) 
#print (afficheTemps(temps))
