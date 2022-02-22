class Personne:
    def __init__ (self,nom="vide",prenom="vide",age=0,adresse="montreal"):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.adresse=adresse
class compteur:
    cpt=0
    def __init__(self):
        compteur.cpt+=1
class TableauNoir():
    def __init__(self):
        self.surface=""
    def message (self,message):
        if self.surface!="":
            self.surface +="\n"
        self.surface += message
    def affichage (self):
       print("affichage du tableau {} ".format(tab.surface))
tab=TableauNoir()


tab.message("bonjour gabriel")
tab.message("comment vas tu?")
#print("affichage du tableau {} ".format(tab.surface))
tab.affichage()
client=Personne()
a= compteur()
b=compteur()
print("voici le nom du client: {0} {1}".format(client.nom, client.prenom) )   
print("nombre d'objets compteurs crees {} ".format(a.cpt))