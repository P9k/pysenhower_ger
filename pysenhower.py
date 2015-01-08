#! /usr/bin/python3
# coding: utf8

#
# -----------------------------------------------------------
# |                     "Pysenhower"                        |
# -----------------------------------------------------------
#
# Python3.2-Programm, mit dem Aufgaben entsprechend ihrer 
# Prioritäten organisiert werden können.
#
#
#
#  08/01/15: Version 0.1 (Alpha)
#

import os
import pickle
from prettytable import PrettyTable

# Pfad, um die Listen zu speichern
PATH = "/home/paul/.eisenhower"
# Erstelle Verzeichnis, falls nötig
if not os.path.exists(PATH):
    os.makedirs(PATH)

# Tabellenkopftitel definieren

column_name_prio_a = "A: Wichtig und dringend"
column_name_prio_b = "B: Wichtig, aber nicht dringend"
column_name_prio_c = "C: Nicht wichtig und dringend"
column_name_prio_d = "D: Nicht wichtig und nicht dringend"

try:	
# Testen, ob Listen geladen werden können
	list_prio_a = pickle.load(open(PATH + "/save.a", "rb"))
	list_prio_b = pickle.load(open(PATH + "/save.b", "rb"))
	list_prio_c = pickle.load(open(PATH + "/save.c", "rb"))
	list_prio_d = pickle.load(open(PATH + "/save.d", "rb"))
except IOError:
	list_prio_a = ["--"]
	list_prio_b = ["--"]
	list_prio_c = ["--"]
	list_prio_d = ["--"]
	pickle.dump( list_prio_a, open(PATH + "/save.a", "wb" ) )
	pickle.dump( list_prio_b, open(PATH + "/save.b", "wb" ) )
	pickle.dump( list_prio_c, open(PATH + "/save.c", "wb" ) )
	pickle.dump( list_prio_d, open(PATH + "/save.d", "wb" ) )
	print("Noch keine Datenbank vorhanden. Wurde angelegt. Bitte neustarten!")
	exit(0)
else:

# Backup: Aufgabenlisten definieren
#list_prio_a = ["Zeug", "Dinge", "Sachen"]
#list_prio_b = ["Krams", "Stuff"]
#list_prio_c = ["Zeug", "Dinge", "Sachen"]
#list_prio_d = ["Krams", "Stuff", "Zeug", "Dinge", "Sachen"]


	#Länge der Tabellenköpfe ermitteln und das Maximum herausfinden
	len_head_a = len(column_name_prio_a)
	len_head_b = len(column_name_prio_b)
	len_head_c = len(column_name_prio_c)
	len_head_d = len(column_name_prio_d)
	
	max_head_length = max(len_head_a, len_head_b, len_head_c, len_head_d)
	
	# Tabellenköpfe zentrieren und mit Leerzeichen auffüllen
	column_name_prio_a = column_name_prio_a.center(max_head_length, " ")
	column_name_prio_b = column_name_prio_b.center(max_head_length, " ")
	column_name_prio_c = column_name_prio_c.center(max_head_length, " ")
	column_name_prio_d = column_name_prio_d.center(max_head_length, " ")
	
	def exitProgram():
	# Programm verlassen
		print("Beende jetzt.") 
		exit(0)
	
	def errorMessage():
	# Fehlermeldung
		print("Bitte eine gültige Option wählen!")

	
	def saveChanges():
	# Listen speichern
		pickle.dump( list_prio_a, open(PATH + "/save.a", "wb" ) )
		pickle.dump( list_prio_b, open(PATH + "/save.b", "wb" ) )
		pickle.dump( list_prio_c, open(PATH + "/save.c", "wb" ) )
		pickle.dump( list_prio_d, open(PATH + "/save.d", "wb" ) )
		os.system('clear')
		print("Änderungen gespeichert.")
	
	def saveQuit():
	# Speichern und beenden
		saveChanges()
		print("Gespeichert. Beende jetzt.")
		exit(0)

	def equalize_lists():
	# Listen gleich lang machen anhand eine Abfrage ihrer Längen und setzen der Numbers-Liste

		# Leere Zellen am Ende löschen
		
		while list_prio_a[-1] == "" and list_prio_b[-1] == "":
			del list_prio_a[-1]
			del list_prio_b[-1]

		while list_prio_c[-1] == "" and list_prio_d[-1] == "":
			del list_prio_c[-1]
			del list_prio_d[-1]
	
		len_a = len(list_prio_a)
		len_b = len(list_prio_b)
		len_c = len(list_prio_c)
		len_d = len(list_prio_d)
		
		while len_b < len_a:
			list_prio_b.append("")
			len_a = len(list_prio_a)
			len_b = len(list_prio_b)
		while len_a < len_b:
			list_prio_a.append("")
			len_a = len(list_prio_a)
			len_b = len(list_prio_b)
		while len_d < len_c:
			list_prio_d.append("")
			len_c = len(list_prio_c)
			len_d = len(list_prio_d)
		while len_c < len_d:
			list_prio_c.append("")
			len_c = len(list_prio_c)
			len_d = len(list_prio_d)
		# Variablen global bekannt machen. Es reicht, wenn eine Seite 
		# betrachtet wird, da die Längen gleich sind. Allerdings bei 
		# Eins anfangen.
		global numbers_a 
		numbers_a = range(1, len_a + 1)

		global numbers_c 
		numbers_c = range(1, len_c + 1)
	

	def showAll():
		# Listen anzeigen
		#
		
		# Zuerst: Listen auf gleiche Länge bringen
		equalize_lists()

		# Listen abbilden
		x = PrettyTable(print_empty=False)
		x.add_column("#", numbers_a)
		x.add_column(column_name_prio_a, list_prio_a)
		x.add_column(column_name_prio_b, list_prio_b)
		x.align[column_name_prio_a] = "l"
		x.align[column_name_prio_b] = "l"
		print(x)
	
		y = PrettyTable(print_empty=False)
		y.add_column("#", numbers_c)
		y.add_column(column_name_prio_c, list_prio_c)
		y.add_column(column_name_prio_d, list_prio_d)
		y.align[column_name_prio_c] = "l"
		y.align[column_name_prio_d] = "l"
		print(y)

	
	def addItem():
	# Einen neuen Eintrag an einer bestimmten Position erstellen
	# 
		USERINPUT = 0
		list_names = ["A", "B", "C", "D"]
		list_dict = {"a" : list_prio_a, "b" : list_prio_b, "c" : list_prio_c, "d" : list_prio_d}
	# Checken, ob eine gültige Liste und später eine Zahl eingegeben werden.
		while True:
			LIST = input("\nIn welcher Liste (A, B, C, D) einfügen?\n").upper()
			if LIST in list_names:
				LIST = LIST.lower()
				break
			else:
				print("\nBitte eine gültige Liste (A, B, C, D) auswählen!\n")
				continue
		while True:
			try:
				USERINPUT = int(input("\nAn welcher Position einfügen?\n"))
			except ValueError:
				print("\nBitte eine Zahl eingeben!\n")
				continue
			else:
	# Hier wird die Option aus einem Dictonary herausgesucht, nachdem die Eingabe
	# kleingeschrieben wurde.
				POSITION = USERINPUT - 1
				LIST = LIST.lower()
				TASK = (input("\nWelche Aufgabe soll hinzugefügt werden?\n"))
				print(LIST)
				list_dict[LIST].insert(POSITION, TASK)
				equalize_lists()
			break

	
	def delItem():
	# Einen Eintrag an einer bestimmten Position löschen
	# 
		USERINPUT = 0
		list_names = ["A", "B", "C", "D"]
		list_dict = {"a" : list_prio_a, "b" : list_prio_b, "c" : list_prio_c, "d" : list_prio_d}
	# Checken, ob eine gültige Liste und später eine Zahl eingegeben werden.
		while True:
			LIST = input("\nIn welcher Liste (A, B, C, D) löschen?\n").upper()
			if LIST in list_names:
				LIST = LIST.lower()
				break
			else:
				print("\nBitte eine gültige Liste (A, B, C, D) auswählen!\n")
				continue
		while True:
			try:
				USERINPUT = int(input("\nWelche Position löschen?\n"))
			except ValueError:
				print("\nBitte eine Zahl eingeben!\n")
				continue
			if USERINPUT > len(list_dict[LIST]):
				print("\nBitte eine Zahl eingeben!\n")
				continue
			else:
	# Hier wird die Option aus einem Dictonary herausgesucht, nachdem die Eingabe
	# kleingeschrieben wurde.
				POSITION = USERINPUT - 1
				del list_dict[LIST][POSITION]
				equalize_lists()
			break


	#
	# Ablaufsteuerung
	#

	# Implementierte Funktionen
	fncDict = {'Q': exitProgram, 'A': addItem, 'L': delItem, 'W': saveChanges, 'WQ': saveQuit}

	RUNNING = 'yes'
	
	while RUNNING == 'yes':
		showAll()
		print('''\nBitte eine Option wählen:\n
(A): Neue Aufgabe an einer bestimmten Position eintragen
(L): Aufgabe löschen
(V): Aufgabe verschieben
(W): Speichern
(WQ): Speichern und Beenden
(Q): Beenden''')
		OPTION = input("\nOption:\n").upper()

		try:
			NUMBER = int(OPTION) -1
		except ValueError:
			fncDict.get(OPTION, errorMessage)()

