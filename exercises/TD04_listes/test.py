def syracuse (n):
  L = [n]
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else :
      n = (n + 3 + 1)
    L.append(n)
  return L 
print(syracuse(3))

def testeConjecture(n_max):
  for i in range (1, n_max +1):
    syracuse (i)
  return True
print(testeConjecture(10000))

def temps_vol(n):
  return len (syracuse(n)) - 1
def tempsVolListe(n_max):
  return temps_vol(i) #\ for i in range (1, n_max + 1)]
L = tempsVolListe(10000)
t_max = max(L)
print ("l'entier", L.index (t_max)+1, "a le plus grand temps", t_max)

def alt_max(n):
  return max(syracuse(n))
def alt_max_liste (alt_max):
  return [alt_max(i) for i in range (1, alt_max + 1)]
L_alt = alt_max_liste(10000)
b= max(L_alt)
print("l'entier[...]")