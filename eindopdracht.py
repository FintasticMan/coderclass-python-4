#!/usr/bin/env python

import os
import time
import json

DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
BESCHIKBARE_SCHERMBREEDTE = SCHERMBREEDTE - 4
SCHERMHOOGTE = 40
BESCHIKBARE_SCHERMHOOGTE = SCHERMHOOGTE - 4
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'
PRINTEN = 'p'

def main():
	woordenlijsten = lees_woordenlijst()

	gekozen_lijst = STANDAARD_LIJST

	doorgaan = True
	while doorgaan:
		print_menu(gekozen_lijst)
		if (keuze := input()) == NIEUWE_LIJST:
			woordenlijsten = nieuwe_lijst(woordenlijsten)

		elif keuze == OPSLAAN:
			opslaan(woordenlijsten)

		elif keuze == KIES_LIJST:
			gekozen_lijst = kies_lijst(woordenlijsten)

		elif keuze == PRINTEN:
			print_lijst(woordenlijsten[gekozen_lijst], '{}\nDruk op enter om door te gaan')

			input()

		elif keuze == TOEVOEGEN:
			woordenlijsten[gekozen_lijst] = voeg_woorden_toe(woordenlijsten[gekozen_lijst])

		elif keuze == DELETE:
			verwijder_woorden(woordenlijsten[gekozen_lijst])

		elif keuze == OVERHOREN:
			overhoren(woordenlijsten[gekozen_lijst])

		elif keuze == STOPPEN:
			doorgaan = False
			print_afscheid(woordenlijsten)

		else:
			print_scherm('Je hebt geen goede keuze gemaakt, probeer nog een keer!')
			time.sleep(2)

def leeg_scherm():
	if os.name == 'posix':
		os.system('clear')
	elif os.name == 'nt':
		os.system('cls')
	else:
		print('\n' * SCHERMHOOGTE)

def print_header():
	print('+' + '-' * (SCHERMBREEDTE - 2) + '+')
	print('| ' + ' ' * BESCHIKBARE_SCHERMBREEDTE + ' |')

def print_footer():
	print('| ' + ' ' * BESCHIKBARE_SCHERMBREEDTE + ' |')
	print('+' + '-' * (SCHERMBREEDTE - 2) + '+')

def print_afscheid(woordenlijsten):
	print_scherm('Wil je nog de lijst opslaan? [y/n]')

	if (keuze := input()) == 'y':
		opslaan(woordenlijsten)
		time.sleep(2)

	print_scherm('Goodbye')

def print_scherm(inhoud):
	lijstinhoud = inhoud.split('\n')
	aantal_regels = len(lijstinhoud)
	padding = (BESCHIKBARE_SCHERMHOOGTE - aantal_regels) / 2

	for i in range(BESCHIKBARE_SCHERMHOOGTE - aantal_regels):
		if i + 1 <= padding:
			lijstinhoud.insert(0, '')
		else:
			lijstinhoud.append('')

	leeg_scherm()

	print_header()

	for i in range(BESCHIKBARE_SCHERMHOOGTE):
		print_regel(lijstinhoud[i])

	print_footer()

def print_regel(inhoud):
	print(('| {0:<' + str(BESCHIKBARE_SCHERMBREEDTE) + '} |').format(inhoud))

def print_menu(gekozen_lijst):
	print_scherm('''Hier kan je kiezen wat je met dit overhoorprogramma wilt doen
De lijst die nu geselecteerd is, is ''' + gekozen_lijst + '''

Je kan:
 - Een nieuwe woordenlijst aanmaken (''' + NIEUWE_LIJST + ''')
 - De geselecteerde woordenlijst in een bestand opslaan (''' + OPSLAAN + ''')
 - Een woordenlijst kiezen (''' + KIES_LIJST + ''')
 - De geselecteerde lijst laten zien (''' + PRINTEN + ''')
 - Woorden toevoegen aan de geselecteerde lijst (''' + TOEVOEGEN + ''')
 - Woorden verwijderen van de geselecteerde lijst (''' + DELETE + ''')
 - De geselecteerde woordenlijst overhoren (''' + OVERHOREN + ''')
 - Stoppen (''' + STOPPEN + ''')''')

def print_lijst(dictionary, str):
	print_scherm(str.format(string_dict(dictionary)))

def nieuwe_lijst(woordenlijsten):
	print_scherm('De volgende woordenlijsten bestaan al:\n\n{}\nHoe heet je nieuwe lijst?'.format(string_keys(woordenlijsten)))
	naam = input()
	woordenlijsten[naam] = {}
	woordenlijsten[naam] = voeg_woorden_toe(woordenlijsten[naam])

	return woordenlijsten

def string_keys(dictionary):
	string = ''
	for key in dictionary:
		string = string + key + '\n'

	return string

def string_dict(dictionary):
	string = ''
	for key in dictionary:
		string = string + key + ' ' + SCHEIDER + ' ' + dictionary[key] + '\n'

	return string


def opslaan(woordenlijsten):
	json_woordenlijsten = json.dumps(woordenlijsten, indent='\t')

	bestand_woordenlijsten = open(('woordenlijsten' + EXTENSIE), 'wt')
	bestand_woordenlijsten.write(json_woordenlijsten)
	bestand_woordenlijsten.close()

	print_scherm('Opgeslagen in woordenlijsten' + EXTENSIE)
	time.sleep(2)

def lees_woordenlijst():
	if os.path.exists('woordenlijsten' + EXTENSIE):
		bestand_woordenlijsten = open(('woordenlijsten' + EXTENSIE), 'rt')
		json_woordenlijsten = bestand_woordenlijsten.read()
		bestand_woordenlijsten.close()
		woordenlijsten = json.loads(json_woordenlijsten)
	else:
		woordenlijsten = {
			'EN-NED': {
				'hello': 'hallo',
				'wow that\'s amazing': 'wow dat is geweldig'
			},
			'DE-NED': {
				'orangesaft': 'sinaasappelsap'
			}
		}

		print_scherm(('woordenlijsten' + EXTENSIE + ' bestaat niet\nDefault woordenlijst is gebruikt'))
		time.sleep(2)

	return woordenlijsten

def kies_lijst(woordenlijsten):
	doorgaan = True
	while doorgaan:
		print_scherm('De volgende woordenlijsten bestaan:\n\n{}\nWelke wil je kiezen?'.format(string_keys(woordenlijsten)))
		lijst_naam = input()
		try:
			test = woordenlijsten[lijst_naam]
		except Exception:
			print_scherm('Die lijst bestaat niet\nProbeer nog een keer')
			time.sleep(2)
		else:
			doorgaan = False
			return lijst_naam

def voeg_woorden_toe(woordenlijst):
	doorgaan = True
	while doorgaan:
		print_scherm('Welk woord wil je toevoegen?\nTyp ' + STOPPEN + ' om te stoppen')
		if (woord := input()) != 'q':
			print_scherm('Wat betekent {}?'.format(woord))
			betekenis = input()
			woordenlijst[woord] = betekenis
		else:
			doorgaan = False

	return woordenlijst

def verwijder_woorden(woordenlijst):
	doorgaan = True
	while doorgaan:
		print_lijst(woordenlijst, 'Welk woord wil je verwijderen?\nDe woorden in de lijst zijn:\n\n{}\nTyp ' + STOPPEN + ' om te stoppen')
		if (woord := input()) != 'q':
			try:
				del woordenlijst[woord]
			except Exception:
				print_scherm('Dat woord is niet in deze lijst\nProbeer nog een keer')
				time.sleep(2)
			else:
				print_scherm('Het woord ' + woord + ' is verwijderd uit de woordenlijst')
		else:
			doorgaan = False

def overhoren(woordenlijst):
	print_scherm('Wil je vooruit (v) of achteruit (a) overhoren?')

	goed = 0

	if (richting := input()) == 'v':
		for key in woordenlijst:
			print_scherm('Wat is \'{}\'?'.format(key))

			if (antwoord := input()) == woordenlijst[key]:
				print_scherm('Goed gedaan, \'{}\' betekent \'{}\'\nDruk op enter om door te gaan'.format(key, woordenlijst[key]))
				goed = goed + 1

			else:
				print_scherm('Nope, \'{}\' betekent \'{}\'\nJouw antwoord was \'{}\'\nDruk op enter om door te gaan'.format(key, woordenlijst[key], antwoord))

			input()

		print_scherm('Je hebt alle woorden overhoord!\nJe had {} goed van de {}\nDit is {}% goed\n\nDruk op enter om door te gaan'.format(goed, len(woordenlijst), round(goed / len(woordenlijst) * 100)))
		input()

	elif richting == 'a':
		for key in woordenlijst:
			print_scherm('Wat is \'{}\'?'.format(woordenlijst[key]))

			if (antwoord := input()) == key:
				print_scherm('Goed gedaan, \'{}\' betekent \'{}\'\nDruk op enter om door te gaan'.format(woordenlijst[key], key))
				goed = goed + 1
			else:
				print_scherm('Nope, \'{}\' betekent \'{}\'\nJouw antwoord was \'{}\'\nDruk op enter om door te gaan'.format(woordenlijst[key], key, antwoord))

			input()

		print_scherm('Je hebt alle woorden overhoord!\nJe had {} goed van de {}\nDit is {}% goed\n\nDruk op enter om door te gaan'.format(goed, len(woordenlijst), round(goed / len(woordenlijst) * 100)))
		input()

	else:
		print_scherm('Je hebt iets verkeerd ingevuld, probeer nog een keer')
		time.sleep(2)

if __name__ == '__main__':
	main()
