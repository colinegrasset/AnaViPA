#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import csv
from AnaVi.Script_génération_carte.classNum import Num

file="tablECnum.csv"

def __repr__(line):
    return(print ("listNumArray: ECnum({}), modif({})".format(line.ECnum, line.modif)))

def csv_ECnum (file) :
    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    listNum_array = [] #create a list which is composed by Num objects
    for row in reader:
        #list pli prendre les valeurs de la class plistruct du package PLIStruct
        line = Num()

        for column, value in row.items():#parcours le fichiers csv valeur par valeur en aller de gauche a droite puis passe a la ligne suivante
            if(column == "EC number") :
                line.ECnum = value
            if(column == "Modification") :
                line.modif = value

        listNum_array.append(line)  # commande qui ajoute une ligne a la liste pliArray

    #     file.close()

    for line in listNum_array:
        __repr__(line)

    return listNum_array

csv_ECnum(file)

