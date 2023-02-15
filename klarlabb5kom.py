#Laboration 5
#Erik Hellström, Eyasu Alemiye
#Hitta väg mellan ord med uskrift av väg


#importerar kö-klassen
from linkedqlabb5 import LinkedQ

#importerar binärt träd-klassen
from bintreefilelabb5 import Bintreelabb5

#skapar ett binärträd för att lagra svenska ordlistan
svenska = Bintreelabb5()

#skapar ett binärträd för att lagra redan "testade" ord
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
        #print(ordet) ta bort denna för att se vilka ord som går att välja på från ordlistan



#funktion utan inparameter som frågar användare om input för första och sista ord för att sedan returnera de 2 valen
def fråga_ord():
    första_ord = input("skriv det första ordet: ")
    sista_ord = input("skriv det andra ordet: ")
    return första_ord, sista_ord

#klass för att representera en nod (varje ord som finns på vägen mellan start & slutord med nextpekare mellan)
class ParentNode:
    #kontruktor med attributen word och parent
    #om ingen parent anges är det startordet (head) eftersom den saknar parent 
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

#används för att få en string-representation av orden (value & parent) Denna användes under tiden då labben gjordes
    # def __str__(self):
    #     rep = self.parent
    #     return rep

#rekurskiv metod som skriver ut vägen från start till slutord
    def writechain(self,child):
        if child != None:
        

            self.writechain(child.parent) #om man byter plats på denna rad och den nedan kommer ordningen förändras. Det visas i den förberedande
            print(child.word)
            
            
        
        


#funktion som skapar barnen. Skapar 26 * 3 st kombinationer av varje ord och testar sedan om de finns i svenskalistan och att de ej förekommer
#sedan tidigare, alltså ej med i binärträdet "gamla"
def makechildren(inord,q):
    #print(startord.word) #använd denna för att se vilket ord som är inparameter i funktionen
    första_byte = [c + inord.word[1:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    andra_byte = [inord.word[0:1] + c + inord.word[2:3] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    tredje_byte = [inord.word[0:2] + c + inord.word[3:] for c in 'abcdefghijklmnopqrstvuwxyzåäö']
    totallista = första_byte + andra_byte + tredje_byte
    #print(totallista) #Använd denna för att se vad för ord som genereras i varje omgång, en lista med 26*3 ord kommer lagras i totallista för varje omgång
    
    for ordet in totallista:
        if ordet in svenska:
            if ordet not in gamla:
                #print(ordet) #använd denna för att se vilka ord som enqueas varje omgång
                
                
                barn = ParentNode(ordet,inord)
                q.enqueue(barn)
                gamla.put(ordet)
                

#funktion som undersöker om det finns en väg mellan start och slutord
def hitta_väg(startord,slutord):
    q = LinkedQ() #skapar ett köobjekt
    gamla.put(startord) #lägger in det första ordet i gamla-listan (detta sker en gång)
    första = ParentNode(startord) #skapar 
    
    makechildren(första,q)
    
    
    while True:
        #om kön är tom finns det ingen väg
            if q.isEmpty() == True:
                print("Tyvärr finns det ingen väg")
                break
            else:
                
                uttaget = q.dequeue() 
                makechildren(uttaget,q)
                #print(uttaget.word)
            
                #om makechilden skapar ett ord som är samma som slutordet innebär det att en väg finns
                if uttaget.word == slutord:
                    print("det FINNS en väg, vägen som hittades var följande: ")
                    
                    första.writechain(uttaget)
                    

                    
                    break





#funktionsanrop
valda_ord = fråga_ord() #hämtar input från användaren som returneras och lagras i en variabel valda_ord
hitta_väg(valda_ord[0],valda_ord[1]) #input tas som inparameter för att hitta väg mellan 2 st ord