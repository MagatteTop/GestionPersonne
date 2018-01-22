# -*-coding:Latin-1 -*
import os # On importe le module os
# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non
annee = input("Saisissez une année : ") # On attend quel'utilisateur saisisse l'année qu'il désire tester
try:
	annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
except TypeError:
	print("Erreur lors de la saisie de lannee.")
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print("L'année saisie est bissextile.")
else:
	print("L'année saisie n'est pas bissextile.")
os.system("pause")