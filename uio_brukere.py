def lag_brukernavn(navn):
    fultnavn = navn.split()
    firstname = fultnavn[0].lower()
    lastname = fultnavn[1][0].lower()
    brukernavn = firstname + lastname
    return brukernavn
print(lag_brukernavn("Mehmet Capa"))

def lagEpost(brukernavn, suffix):
    epost = brukernavn + "@" + suffix
    return epost
print(lagEpost("mehmetc", "student.matnat.uio.no"))

def skrivUtEposter(ordbok):
    for person in ordbok:
        suffix = ordbok[person]
        print(lagEpost(person, suffix))
skrivUtEposter({"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"})

tom_ordbok = {}
verdi = input("For å lage email tast <i>, for å skrive ut eposter tast <p>, for å avslutte programmet tast <s>: ")
while(verdi != "s"):
    if verdi == "i":
        navn = input("Skriv et navn og etternavn: ")
        suffix = input("Skriv suffixet for brukernavn: ")
        brukernavn = lag_brukernavn(navn)
        tom_ordbok[brukernavn]=suffix
    elif verdi == "p":
        skrivUtEposter(tom_ordbok)
    else:
        verdi = input("For å lage email tast <i>, for å skrive ut eposter tast <p>, for å avslutte programmet tast <s>: ")

def lag_unikt_brukernavn(navn, tom_ordbok):
    lastnamecounter = 0
    fultnavn = navn.split()
    firstname = fultnavn[0].lower()
    lastname = fultnavn[1][lastnamecounter].lower()
    brukernavn = firstname + lastname
    for eksisterendenavn in tom_ordbok:
        if brukernavn == eksisterendenavn:
            while brukernavn != eksisterendenavn:
                lastname = fultnavn[1][lastnamecounter + 1].lower()
                brukernavn = firstname + lastname
                lastnamecounter += 1
    return brukernavn
##Den sjekker ikke om det finnes både navn og etternavnet til studentene samme. 



    