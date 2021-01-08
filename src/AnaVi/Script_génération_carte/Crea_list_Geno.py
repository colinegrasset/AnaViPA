#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import os
import csv
import classGeno

file = "classGeno"

def __repr__(listGeno):
    return(print("pliArray: Strain({}), daughter({}), genotype({}))".format(
        listGeno.strain, listGeno.daughter, listGeno.genotype)))

def csv_tablo_Geno (file):
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    geno_array = [] #creation d'une liste qui va contenir la class plistruct x nb de ligne du .csv
    for row in reader:
        pli = __repr__.Geno()#liste pli prendre les valeurs de la class plistruct du package PLIStruct

        for column, value in row.items():#parcours le fichiers csv valeur par valeur en aller de gauche a droite puis passe a la ligne suivante
            if(column == "strain") :
                pli.strain = value
            if(column == "daughter") :
                pli.daughter = value
            if(column == "genotype") :
                pli.genotype = value

        geno_array.append(pli)  # commande qui ajoute un pli a la liste pliArray

    #     file.close()

    for pli in geno_array:
        __repr__(pli)

    return geno_array