# coding=utf-8

#script de collecte des compétences des fiches ROME de l'ANPE
#auteur: GABRIEL Alex

import httplib

# boucle pour scanner les différents code ROME
codeLetter = "ABCDEFGHIJKLMN"
nbFiche=0
for lettre in codeLetter:
	for i in range(10 , 50):
		if len(str(i)) ==1:
			for j in range(0 , 50):
				codeROME = lettre +"0"+ str(i)
				if len(str(j)) ==1:
					codeROME = codeROME+"0"+ str(j)
					conn= httplib.HTTPConnection("candidat.pole-emploi.fr") # connection sur le site ANPE
					conn.request("GET", "/marche-du-travail/fichemetierrome?codeRome="+codeROME)
					r1 = conn.getresponse()
					if r1.status ==200:
						nbFiche += 1
						print codeROME+ "--> OK (" + str(nbFiche) +")"
					else:
						print codeROME
				else:
					codeROME = codeROME+ str(j)
					conn= httplib.HTTPConnection("candidat.pole-emploi.fr") # connection sur le site ANPE
					conn.request("GET", "/marche-du-travail/fichemetierrome?codeRome="+codeROME)
					r1 = conn.getresponse()
					if r1.status ==200:
						nbFiche += 1
						print codeROME+ "--> OK (" + str(nbFiche) +")"
					else:
						print codeROME
		else :
			for j in range(0 , 50):
				codeROME = lettre + str(i)
				if len(str(j)) ==1:
					codeROME = codeROME+"0"+ str(j)
					conn= httplib.HTTPConnection("candidat.pole-emploi.fr") # connection sur le site ANPE
					conn.request("GET", "/marche-du-travail/fichemetierrome?codeRome="+codeROME)
					r1 = conn.getresponse()
					if r1.status ==200:
						nbFiche += 1
						print codeROME+ "--> OK (" + str(nbFiche) +")"
					else:
						print codeROME
				else :
					codeROME = codeROME + str(j)
					conn= httplib.HTTPConnection("candidat.pole-emploi.fr") # connection sur le site ANPE
					conn.request("GET", "/marche-du-travail/fichemetierrome?codeRome="+codeROME)
					r1 = conn.getresponse()
					if r1.status ==200:
						nbFiche += 1
						print codeROME+ "--> OK (" + str(nbFiche) +")"
					else:
						print codeROME