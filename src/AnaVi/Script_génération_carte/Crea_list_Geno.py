#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import numpy as np
import csv

file = "tablGeno.csv"

###########################################
 #   ça marche pas vraiment encore... #
 ##########################################

def __repr__(pli):
    print("pliArray: Strain({}), daughter({}), genotype({}))".format(
        pli.strain, pli.daughter, pli.genotype))
    return None

def csv_tablo_Geno(file):
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    geno_array = []  # creation d'une liste qui va contenir la class claasGeno x nb de ligne du .csv

    for row in reader:
        pli = __repr__.Geno()  # liste pli prendre les valeurs de la class Geno du package classGeno

        # parcours le fichiers csv valeur par valeur en aller de gauche a droite puis passe a la ligne suivante
        for column, value in row.items():
            if column == "Souche":
                pli.strain = value
            if column == "Fille de...":
                pli.daughter = value
            if column == "Genotype":
                pli.genotype = value

            geno_array.append(pli)  # commande qui ajoute un pli a la liste geno_array

    #file.close()

    for pli in geno_array:
        __repr__(pli)
    return geno_array
