#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

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