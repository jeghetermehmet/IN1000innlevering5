#Foruten tjenester gjennomgått på forelesning kan du
#benytte tjenesten split() som også tilbys av strengobjekter: om man har en variabel
#tekst="hei du" kan man skrive ordene = tekst.split() for å få en liste med hvert ord. Listen
#vil se sånn her ut: [“hei”, “du”] siden split() deler opp på mellomrom.

def bokstavTeller(ord):
    count = 0
    for bokstav in ord:
        count += 1
    return count
#I denne koden antar jeg at brukeren skriver et ord uten å bruke mellomrom.
def ordtelling(setning):
    ordbok = {}
    sentences = setning.split()
    for ord in sentences:
        if ord not in ordbok:
            ordbok[ord]=1
        else:
            ordbok[ord]+=1
    return ordbok

def telleBokstaverogOrd():
    setning = input("Skriv en setning: ")
    sentences = setning.split()
    ordcount = len(sentences)
    count = 0
    for bokstav in sentences:
        count += 1
    ordbok = {}
    for ord in sentences:
        if ord not in ordbok:
            ordbok[ord]=1
        else:
            ordbok[ord]+=1
    print("Det er", count, "bokstaver i setningen din")
    print("Det er", ordcount, "ord i setningen din")
    for key in ordbok:
        print("Ordet", key, "forekommer", ordbok[key], "ganger, og har", bokstavTeller(key), "bokstaver.")

