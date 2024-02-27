#Oppagve5
#Jeg tenker å utvide oppgave 4 litt ved at brukeren selv kan legge til nye beboere også skrive ut lista , samme funksjon blir bevart også slik at vi kan søke opp opp beboere, blir en kombinasjon av 2 og 4
#Jeg lar brukeren selv velge hvor mange bebeoere hen vil legge til ved hjelp av en if test som sørger for at antall beboere skal være 1 eller flere
#Det virker som det er et eller annet bug i koden som jeg ikke helt skjønner når jeg søker opp beboer selv om vedkommende eksisterer. For når jeg skriver ut så finner den jo før den hopper inn i hentmaltid 
#prosedyren.
ordbok={}
ordbok = {"Kari Nordmann":"Frokost: Brød Lunch: Egg Middag: Pølser", "Per Nordmann":"Frokost Bønner Lunch: Fisk Middag: Laks", "Ivar Pettersen":"Frokost: Fisk Lunch: Kjøtt Middag:Foodora"}  #Legger disse inn i ordboka
print("Her har du nåværende beboerenes måltidsplan", ordbok)




def leggtilnybeboer():
    print("Hvor mange beboere vil du legge til i dag?")
    antall=int(input())
    if antall<1:
        print ("Ingen beboere å legge til")
    else:
        i=1
        while i<=antall:
            print ("Legg inn navn og måltider, du må taste enter mellom beboer og måltid")
            ordbok.update({input():input()})
            i+=1 #Øker i med1
            print(ordbok)


def hentmaltid(): #Funksjonen hentmaltid 
    print("Tast inn navn du vil finne måltidene til") #Ber brukeren taste inn navn 
    navn=input()
    for x in ordbok: #Lager en for-løkke for å traversere ordboka 
        if x==navn: #Lager en ifsetning som printer ut måltidsplanen om man finner navnet 
            print(ordbok[x])
        else:
            print("Beboer ikke registrert") #Skriver ut en melding dersom beboeren ikke finnes i lista og hopper ut av for løkka slik at meldingen slipper å gjentas flere ganger. 
            break





leggtilnybeboer()#Kaller proseydren    
print(ordbok)
hentmaltid() #kaller Prosedyren