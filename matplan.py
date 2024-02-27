#Oppgave 4 
ordbok={}
ordbok = {"Kari Nordmann":"Frokost: Brød Lunch: Egg Middag: Pølser", "Per Nordmann":"Frokost Bønner Lunch: Fisk Middag: Laks", "Ivar Pettersen":"Frokost: Fisk Lunch: Kjøtt Middag:Foodora"}  #Legger disse inn i ordboka
def hentmaltid(): #Funksjonen hentmaltid 
    print("Tast inn navn du vil finne måltidene til") #Ber brukeren taste inn navn 
    navn=input()
    for x in ordbok: #Lager en for-løkke for å traversere ordboka 
        if x==navn: #Lager en ifsetning som printer ut måltidsplanen om man finner navnet 
            print(ordbok[x])
        else:
            print("Beboer ikke registrert") #Skriver ut en melding dersom beboeren ikke finnes i lista og hopper ut av for løkka slik at meldingen slipper å gjentas flere ganger. 
            break



hentmaltid() #kaller Prosedyren

#Deloppgave 3 i denne oppgaven
#1. Brukernavn på alle IN1000 studenter - her ville jeg brukt en mengde. Rekkefølgen er ikke så veldig viktig hva gjelder akkurat dette, men det er litt dumt feks hvis et brukernavn forekommer flere ganger
#2. Brukernavn og antall poeng på oblig 3 - her går det an å ha en ordbok, men den store faren her er jo om man legger inn en duplikatnøkkel- da vil jo dataen bli overskrevet. Men det er uansett en relasjon
#mellom antall poeng en student har og brukernavnet
#3. Lotto vinnere i Norge - rekkefølgen er forsåvidt ikke så viktig her, men det kan være flere som heter Per Kristiansen som har vunnet en lottopermie i sitt liv. Så selv om listen er sortert så gjør det ikke 
#så mye om de nye vinnerene blir lagt til på slutten av lista 
#4 . Maten gjester er allergisk mot - her ville jeg brukt en ordbok som i denne oppgaven -det er helt klart en sammenheng mellom maten en person er allergisk mot og navnet


            
