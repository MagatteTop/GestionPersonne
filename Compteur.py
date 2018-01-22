import os
class Compteur:
	""" cette classe detient un attribut nb_objet qui sincrement a chque foisqu'un nouveau objet est cléé"""
	nb_objet=0
	def __init__(self):#methode dobjet ou constructeur
		""" lattribut nb_objet sincremente a chaque creation """
		Compteur.nb_objet+=1
	def combien(cls): #methode de class
		""" combien est une methode de class permettant dafficher le nombre dobjet créé"""
		print("on a {} objets créés por le moment.".format(cls.nb_objet))
		combien=classmethod(combien)
	def afficher():#methode statique
		""" fonction chargée dafficher quelques choses"""
		print("ceci es un exemple de methode statique")
	afficher=staticmethod(afficher)
os.system("pause")