#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import numpy as np
import csv
import regex
import re
from regex import regex

from AnaVi.Script_génération_carte.Crea_list_Num import csv_ECnum
from AnaVi.Script_génération_carte.classGeno import Geno



#file = "C://Users//User//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablGeno.csv"



def __repr__(pli):
    print("pliArray: Strain({}), daughter({}), genotype({}))".format(
        pli.strain, pli.daughter, pli.genotype))

def csv_tablo_Geno(file):

    csv.register_dialect('myDialect', delimiter=';', quotechar='|')
    reader = csv.DictReader(open(file, "r"), dialect='myDialect')

    geno_array = []  # creation d'une liste qui va contenir la class claasGeno x nb de ligne du .csv

    for row in reader:
        pli = Geno()  # liste pli prendre les valeurs de la class Geno du package classGeno

        # parcours le fichiers csv valeur par valeur en aller de gauche a droite puis passe a la ligne suivante
        for column, value in row.items():
            if column == "Souche":
                pli.strain = value
            if column == "Fille de...":
                pli.daughter = value
            if column == "Genotype":
                pli.genotype = value

            geno_array.append(pli)  # commande qui ajoute un pli a la liste geno_array

    # file.close()

    for pli in geno_array:
        __repr__(pli)
    return geno_array

def fillingDict():

    ListGeno = csv_tablo_Geno("tablGeno.csv")
    ListNum=   csv_ECnum ("tablECnum.csv")
    for pli in ListGeno:
        AllGeno = pli.genotype
        print(AllGeno)
        regle=re.compile(r"\S*")
        rep= list(regle.finditer(AllGeno))
        for i in rep:
            print(i.group())
            for pli2 in ListNum:
                if i.group() == pli2.modif :
                     print(pli2.ECnum)
                     pli.mutation={i.group():pli2.ECnum}
        print(pli.mutation)
        #print(rep)
        #rep.group(1)

#csv_tablo_Geno(file)
fillingDict()