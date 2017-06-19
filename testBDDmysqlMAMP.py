# coding=utf-8

#script de collecte des compétences des fiches ROME de l'ANPE
#auteur: GABRIEL Alex

import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="root", database="ANPEKB", port="8889")
cursor = conn.cursor()
query = "INSERT INTO secteurs (s_nom) values (%s)"
cursor.execute(query, ("test",))
conn.commit()
data = cursor.lastrowid
if data is None :
	print("nothing in dbb")
else:
	print(data)
#data = cursor.fetchone()
#print "id " ,data
conn.close()