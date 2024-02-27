
#Oppgave 3 
def pris(): #Definerer prosedyren pris
  print("Skriv alder på kjøperen")
  alder=int(input()) #Definerer alder i input 
  billettpris=0 # Setter prisen = 0 
  if alder <=17: #Sjekker om alder er mindre eller lik 17 
    billettpris=30 #Setter billettpris = 30 
    #print("Billettprisen er ", billettpris)
  elif alder >17 and alder<67: #Sjekker om alder er større enn 17 og mindre enn 67 
    billettpris=50
    #print("Billettprisen er ", billettpris)
  elif alder>=67: #Sjekker om alder er større enn eller lik 17 
    billettpris=35
    #print("Billettprisen er ", billettpris)
    
  print("Billettprisen er ", billettpris)

pris()
   
#Svar på oppgave 3d - det fungerer jo med alle aldre. Men programmet et jo dog ikke helt idiotsikkert ved at man kan legge inn negativ alder, men denne funksjonen er ikke sånn veldig vanskelig å legge til
#Vet ikke helt om det var det spørsmålet refererte til. Jeg mener dog det fungerer som det skal. 




    
    
