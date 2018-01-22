import os
class Personne:
	"""la class personne est caracterisée par:
	-son nom
	-son prenom
	-son age
	-son adresse"""
	#le constructeur
	def __init__(self,nom,prenom,age):
		"""initialisationdes attribut de la class"""
		self.nom=nom
		self.prenom=prenom
		self.age=age
		self._adresse="Senegal" #noublier pas le_
	def _get_adresse(self):
		""" methode pour acceder aladresse"""
		print("adresse de residence:")
		return self._adresse
		
	def _set_adresse(self,nouvelle_adresse):
		""" methode pour modifier lattribut adresse"""
		print("attention il semble que {} {} a changé d'adresse".format(self.prenom,self.nom,nouvelle_adresse))
		self._adresse=nouvelle_adresse
		#signaler klattribut _adresse point vers une property
	adresse=property(_get_adresse,_set_adresse)
	    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
        self.nom, self.prenom, self.age)
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre
        objet"""
        return "{} {}, âgé de {} ans".format(
        self.prenom, self.nom, self.age)
os.system("pause")
