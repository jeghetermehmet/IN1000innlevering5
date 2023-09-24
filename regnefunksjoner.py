def addisjon(tall1, tall2):
    sum = tall1 + tall2
    return sum
print(addisjon(34, 78))
def subtraksjon(tall1, tall2):
    trekkfra = tall2 - tall1
    return trekkfra
def divisjon(tall1, tall2):
    if tall2 == 0:
        raise ValueError("Kan ikke deles med null")
    divisjon = tall1/tall2
    return divisjon

# Test addisjon-funksjonen med assert
assert addisjon(5, 3) == 8
assert addisjon(-5, -3) == -8
assert addisjon(0, 0) == 0

# Test subtraksjon-funksjonen med assert
assert subtraksjon(5, 3) == 2
assert subtraksjon(-5, -3) == -2
assert subtraksjon(0, 0) == 0

# Test divisjon-funksjonen med assert
assert divisjon(10, 2) == 5
assert divisjon(-10, -2) == 5
assert divisjon(0, 5) == 0

# Test håndtering av deling med null
try:
    divisjon(5, 0)
except ValueError as e:
    assert str(e) == "Kan ikke dele med null"

print("Alle tester vellykket.")

def tommerTilCm(antallTommer):
    assert antallTommer > 0, "Antall tommer må være større enn 0"
    return antallTommer*2.54

def skrivBeregningee():
    tall1 = float(input("Skriv første tall: "))
    tall2 = float(input("Skriv andre tall: "))
    print(addisjon(tall1, tall2))
    print(subtraksjon(tall1, tall2))
    print(divisjon(tall1, tall2))
    tommertall = float(input("Skriv et tall som skal konverteres til tommercm: "))
    print("Konvertering fra tommer til cm ", tommerTilCm(tommertall))

