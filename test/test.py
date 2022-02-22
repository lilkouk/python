from asyncio.windows_events import NULL
from contextlib import nullcontext
from unicodedata import numeric


class Node:
    

    def __init__(self, valeur,next=None) -> None:
        self.valeur= valeur
        self.suivant = next 
    def nextNode(self, node ):
        
        self.suivant=node
        

    def value (self)-> numeric:
        return self.valeur
    def next (self):
        return self.nextNode
    def print (self):
        print(self.valeur)
        print (self.nextNode)
    def __str__(self):
        if self.suivant == None :
            return f"{self.valeur} -> None"
        else :
            return f"{self.valeur} -> {str(self.suivant)}"
class listeChainer ():
    def __init__(self,start) -> None:
         self.debut=start
    def __str__(self) -> str:
         if self.debut=None:
             return "liste vide"
         else:
             start=self.debut
             while (start!=None):
                 
 
