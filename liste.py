#Oppgave 1 om liste 
import numpy #Importeren modulen numpy for å kunne få tilgang til matematiske funksjoner. 
liste=[10,60,65] #Legger til tallene 10, 60 og 65 i listen
liste.append(6) #Legger til tallet 6 i lista
print ("Første element", liste[0] ,"og trejde element",liste[2]) #Printer ut element 1 som er 10 og element 3 som er 65
navneliste=[]
i=0
while i <=3: #Bruker en while løkke for å legge inn navn i navnelista
    navn=input("Tast inn navn ")
    navneliste.append(navn)
    i+=1

print ( "Her er navnelista", navneliste)
for x in navneliste: #Traverserer navnelista
    if x=="William":
        print ("Du husket meg")
        break #Ikke noe poeng å fortsette loopen om man har funnet navnet mitt
    else:
        print ("Glemte du meg?")
        break #Heller ikke noe poeng å fortsette loopen om ikke navnet mitt er der, den vil da skrive ut navnet for hvert sted i lista
nyliste = []
nyliste.append(sum(liste)) #Bruker sum funksjonen  for å summere tallene i lista
nyliste.append(numpy.product(liste))  #Bruker en funksjon fra numpy om å multiplere tallene i den opprinnelige listen
print ("Den nye lista med to tall er", nyliste) #Printer ut nyliste
nyliste2=liste+nyliste #Slårsammen liste og nyliste inn i nyliste 2
print ("Den sammenslåtte tallisten er ", nyliste2) #Printer ut nyliste 2 
nyliste2.pop()
nyliste2.pop() 
 #Fjerner de to siste elementene i lista , altså de som står på plass 4 og 5, metoden må kalles to ganger da pop kun tar ett argument
print ("Den sammenslåtte hvor de to siste er fjerent  ", nyliste2) #Printer ut nyliste2 







