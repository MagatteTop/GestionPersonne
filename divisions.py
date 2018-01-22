# -*-coding:Latin-1 -*
import os
num = input("entrer le numerateur:")
try: # On essaye de convertir l'année en entier
	num = int(num)
except TypeError:
	print("La variable numerateur recoit un type incompatible avec la division.")
den = input("entrer le denominatuer")
try: # On essaye de convertir l'année en entier
	den=int(den)
except TypeError:
	print("La variable denominateur recoit un type incompatible avec la division.")
try: # On fait la division
	resultat=num/den
	assert den>0
except ValueError:
	print("La variable denominateur ne peut pas etre egale à 0")
else:
	print("Le resultat obtenu est", resultat)
os.system("pause")