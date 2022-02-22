

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
    def __str__(self) -> str:
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
    def getItem(self,i):
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
    
        
 

node= Node (25,Node(24))
node1=Node(26,node)
Liste= ListeChainer(node1)
print(node1)
print("=================")
print(Liste)
print(Liste.getItem(3))
