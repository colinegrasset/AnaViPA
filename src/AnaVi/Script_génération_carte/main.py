#!/usr/bin/python

import xml.etree.ElementTree as ET
from AnaVi.Script_génération_carte.Link_svg import readmap, legende
from AnaVi.Script_génération_carte.dictionary_mutation import fillingDict


def main(fileGeno,fileECnum,strainSearch,mapM):
    listEcSouche = fillingDict(fileGeno,fileECnum)
    print("************************************")
    for i in listEcSouche:
        if i.strain == strainSearch:
            print(i.mutation.keys())
            readmap(mapM, i.mutation)

# path de coline
main("tablGeno.csv",
     "tablECnum.csv",
     "40","carte_metabolique_pentose-arginine.svg")

# path de Rachel
#fillingDict("C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablGeno.csv",
#           "C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablECnum.csv")

# path de lucie
#fillingDict("C://Users//yuibl//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "C://Users//yuibl//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablECnum.csv")

#path Claire
#fillingDict("//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablECnum.csv")