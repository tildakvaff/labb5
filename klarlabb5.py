#Laboration 4
#Erik Hellström, Eyasu Alemiye
#Version 2

from linkedqlabb5 import LinkedQ
from bintreefilelabb5 import Bintreelabb5
svenska = Bintreelabb5()
gamla = Bintreelabb5()


#Använder koden från laboration 3 för att läsa in orden och lagra i ett binärt träd
with open("ordlistalabb5.txt", "r", encoding = "utf-8") as svenskfil:
#with open("egenordlabb5.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()              # Ett trebokstavsord per rad
        if ordet in svenska:           #om ordet redan finns i listan kommer det ej läggas till som dublett
            pass 
            
        else:
            svenska.put(ordet)
        #print(ordet) ta bort denna för att se vilka ord som går att välja på



#frågar om start & slutord
def fråga_ord():
    första_ord = input("skriv det första ordet: ")
    sista_ord = input("skriv det andra ordet: ")
    return första_ord, sista_ord


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def __str__(self):
        rep = self.parent
        return rep

    def writechain(self,child):

        if child != None:
        

            self.writechain(child.parent) #om man byter plats på denna rad och den nedan kommer ordningen förändras. Det visas i den förberedande
            print(child.word)
            
            
        
        


#skapar en ordlista för gamla ord:
def makechildren(startord,q):
    #print(startord.word)
    första_byte = [c + startord.word[1:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    andra_byte = [startord.word[0:1] + c + startord.word[2:3] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    tredje_byte = [startord.word[0:2] + c + startord.word[3:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    totallista = första_byte + andra_byte + tredje_byte
    #print(totallista) #Använd denna för att se vad för ord som genereras i varje omgång
    
    for ordet in totallista:
        if ordet in svenska:
            if ordet not in gamla:
                #print(ordet) #använd denna för att se vilka ord som enqueas varje runda
                
                
                nytt_barn = ParentNode(ordet,startord)
                q.enqueue(nytt_barn)
                gamla.put(ordet)
                


def hitta_väg(startord,slutord):
    q = LinkedQ()
    gamla.put(startord)


    första = ParentNode(startord)
    
    makechildren(första,q)
    
    
    while True:
        
            if q.isEmpty() == True:
                print("Tyvärr finns det ingen väg")
                break
            else:
                
                uttaget = q.dequeue() 
                makechildren(uttaget,q)
                #print(uttaget.word)
            
            
                if uttaget.word == slutord:
                    print("det FINNS en väg, vägen som hittades var följande: ")
                    
                    första.writechain(uttaget)
                    

                    
                    break





#funktionsanrop
valda_ord = fråga_ord() #hämtar input från användaren som returneras och lagras i en variabel valda_ord
hitta_väg(valda_ord[0],valda_ord[1]) #input tas som inparameter för att hitta väg mellan 2 st ord