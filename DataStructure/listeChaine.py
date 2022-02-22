

class Node:
    

    def __init__(self, valeur,next=None) -> None:
        self.valeur= valeur
        self.suivant = next 
    def nextNode(self, node ):
        
        self.suivant=node
        

    def value (self):
        return self.valeur
    def next (self):
        return self.suivant
    def print (self):
        print(self.valeur)
        print (self.nextNode)
    def __str__(self):
        if self.suivant == None :
            return f"{self.valeur} -> None"
        else :
            return f"{self.valeur} -> {str(self.suivant)}"
class ListeChainer ():
    def __init__(self,start) -> None:
         self.debut=start
    def __str__(self) -> str:  #affichage de la liste 
         if self.debut==None:
             return "liste vide"
         else:
            return str(self.debut)
    def length(self):
        nbr=0;
        next=self.debut
        while next!=None:
           
            nbr=nbr+1
            next=next.next()
        return nbr
    def tete(self):
        return self.debut
    def getItem(self,i): #obtention du i eme item de la liste
        taille= self.length()
        next=self.debut
        cpt=0
        if i >= taille :
            return " out of bound"
        while cpt<=i and cpt<taille:
            
            if i==cpt:
               return next.value()
            cpt=cpt+1
            next=next.next()
    def concat(self,liste): # concatenation de deux listes chainees
        next=self.debut
        
        while next!=None:
            prev=next
            next=next.next()
        prev.nextNode(liste.tete())
    def append(self, valeur ): # ajouter un element dans une liste 
         next=self.debut
         while next!=None:
              prev=next
              next=next.next()
         prev.nextNode(Node(valeur))
    def affichage (self) ->str:
        next=self.debut
        texte=""
        while next!=None:
            
            texte= texte + str(next.value())+"==>"
            next=next.next()
        return texte
node= Node (25,Node(24))
node1=Node(26,node)
liste= ListeChainer(node1)
liste1=ListeChainer(node)
liste2= ListeChainer(Node(65))
print(node1)
print("=================")
print(liste)
print(liste.getItem(3))
liste.concat(liste2)
for i in range (1000):
    liste.append(i)
liste.affichage()