# coding=utf-8

#script de collecte des compétences des fiches ROME de l'ANPE
#auteur: GABRIEL Alex

import httplib
from bs4 import BeautifulSoup

conn= httplib.HTTPConnection("candidat.pole-emploi.fr") # connection sur le site ANPE
conn.request("GET", "/marche-du-travail/fichemetierrome?codeRome=G1202")
r1 = conn.getresponse()
data1 =r1.read()
soup = BeautifulSoup(data1)
for div in soup.findAll(id = "js-tabs-unit2-body"):
	savoirfaire = div.contents[2].find(headers = "head-activ") # compétences de base 
	for savoirfairestring in savoirfaire.contents[0].findAll("li"):# savoir faire compétences de base
		print(savoirfairestring.string) # traitement des savoirs faire des compétences de base
	for savoirfairestring in savoirfaire.contents[1].findAll("li"):# savoirs compétences de base
		print(savoirfairestring.string) # traitement des savoirs des compétences de base
	savoirfaire = div.contents[4].find(headers = "head-activ") # compétences spécifiques

		