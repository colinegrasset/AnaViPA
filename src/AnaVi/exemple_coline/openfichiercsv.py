#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import os
import csv
 
file = open("exportBindingEnol3HNT.csv", "r")
 
try:
    # Création du ''lecteur'' CSV.
    reader = csv.reader(file)
    # Le ''lecteur'' est itérable, et peut etre utilisé
    # dans une boucle ''for'' pour extraire les
    # lignes une par une.
    for row in reader:
        print (row) 
finally:
    # Fermeture du fichier source
    file.close()