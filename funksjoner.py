def adder(tall1, tall2):
    result = tall1 + tall2
    return result
print("Første resultat er:", adder(23, 45))
print("Andre resultat er:", adder(12, 56))

#tekst = str(input("Skriv et tekststreng: "))
#bokstav = str(input("Skriv en bokstav: "))
#count = 0
#for letter in tekst:
#    if letter == bokstav:
#        count += 1
#print("Bokstav", bokstav, "forekommer", count, "ganger i", tekst)

def tellForekomst(minTekst, minBokstav):
    count = 0
    for letter in minTekst:
        if letter == minBokstav:
            count += 1
    return count



