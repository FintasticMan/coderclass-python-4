#!/usr/bin/env python

naam = input("Hoe heet je? ")

print("-" * 24)
print("{}, wat leuk!".format(naam))
print("{:^24}".format(naam))
print("Je naam is:{:>13}".format(naam))
print("-" * 24)

SCHERMBREEDTE = 32
MAX_WOORD_LENGTE = 11
woord = input("Welk woord kies je? ")

print("+" + "-" * (SCHERMBREEDTE - 2) + "+")
print(("| Je gekozen woord:{:>" + str(MAX_WOORD_LENGTE) + "} |").format(woord))
print("+" + "-" * (SCHERMBREEDTE - 2) + "+")

SCHERMBREEDTE = 36
MAX_WOORD_LENGTE = 16
woord1 = input("Welk woord kies je? ")
woord2 = input("Welk woord kies je? ")
woord3 = input("Welk woord kies je? ")

def print_regel(regel):
	print(("> {:" + str(MAX_WOORD_LENGTE) + "} <").format(regel))

print("-" * SCHERMBREEDTE)
print_regel(("Je eerste woord:{:>" + str(MAX_WOORD_LENGTE) + "}").format(woord1))
print_regel(("Je tweede woord:{:>" + str(MAX_WOORD_LENGTE) + "}").format(woord2))
print_regel(("Je derde woord: {:>" + str(MAX_WOORD_LENGTE) + "}").format(woord3))
print("-" * SCHERMBREEDTE)

getal = 1

def maak_twee():
	getal = 2

maak_twee()

for _ in range(2):
	getal += 1

if getal < 5:
	getal = 10

print(getal)

getal = 1

def hoog_een_op(getal):
	getal += 1

def hoog_twee_op(getal):
 return getal + 2

for _ in range(3):
	hoog_een_op(getal)
	hoog_twee_op(getal)

print(getal)

getal = 1

def hoog_een_op(getal):
	getal += 1

def hoog_twee_op(getal):
 return getal + 2

for _ in range(3):
	hoog_een_op(getal)
	getal = hoog_twee_op(getal)

print(getal)

def voeg_woorden_toe(woordenlijst, lijst_naam):
	woordenlijst[lijst_naam[0]] = lijst_naam[1]
	return woordenlijst

woordenlijst = {}
while True:
	lijst_naam = []
	one = input("Welke woorden wil je toevoegen? ")
	if one == "fuckoff":
		break
	two = input("Welke woorden wil je toevoegen? ")
	lijst_naam.append(one)
	lijst_naam.append(two)

	woordenlijst = voeg_woorden_toe(woordenlijst, lijst_naam)
	print(woordenlijst)
