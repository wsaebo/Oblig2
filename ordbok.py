#oppgave 2 om ordbok
ordbok={"melk":14.90,"brød":24.90,"yoghurt":12.90,"pizza":39.90} #legger inn alle i ordboken
print ("Dette er ordboken med priser i ", ordbok)
i = 0
while i<=1: #While løkke for å legge inn to nye varer og pris 
    print ("Legg inn varenavn og pris, man må trykke enter etter at man har tastet inn varenavnet og derretter prisen" )
    ordbok.update({input():float(input())}) #Bruker update metoden for å legge dette inn. 
    i+=1 #Øker i med en slik at vi får riktig antall varer og pris 
print("Ordbok med nye varer og pris", ordbok) #Printer ut ordboken med de to nye varene og prisen

#Dette er kanskje ikke den mest elegante måten å løse oppgaven på, men den fungerer på et vis. 


