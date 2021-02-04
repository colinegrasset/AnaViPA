#!/usr/bin/python

import csv

from AnaVi.Script_génération_carte.Crea_list_Geno import csv_tablo_Geno
from AnaVi.Script_génération_carte.Crea_list_Num import csv_ECnum
from AnaVi.Script_génération_carte.classGeno import Geno
from AnaVi.Script_génération_carte.classNum import Num
import re


def fillingDict(fileGeno,fileECnum):

    ListGeno = csv_tablo_Geno(fileGeno)
    ListNum = csv_ECnum(fileECnum)
    for pli in ListGeno:
       # if pli.strain =="44":
         AllGeno = pli.genotype
         #print(AllGeno)
         #print("avant regex")
         #print(pli.genotype)
         regle=re.compile(r"\S*")
         rep= list(regle.finditer(AllGeno))
         #print(rep)
         for i in rep:
            #print(i.group())
            mut=i.group()
            #print("mutation")
            #print(mut)
            for pli2 in ListNum:
                if mut == pli2.modif :
                    #print("Ecnumber")
                    #print(pli2.ECnum)
                    #pli.mutation[]
                    pli.mutation[mut]=pli2.ECnum
                    #pli.mutation = {i.group():pli2.ECnum}

         print("dictionnaire")
         #print(pli.mutation.keys())
         print(pli.mutation)
    #return ListGeno

# path de coline
#fillingDict("C://Users//User//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "C://Users//User//IdeaProjects//AnaVi//src//AnaVi//Script_génération_carte//tablECnum.csv")

# path de Rachel
#fillingDict("C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablGeno.csv",
 #           "C://Users//Utilisateur//IdeaProjects//AnaViPA//src//AnaVi//Script_génération_carte//tablECnum.csv")

fillingDict("tablGeno.csv","tablECnum.csv")

#path Claire
#fillingDict("//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablGeno.csv",
#            "//Users//claire//Desktop//M1Gphy//ProjetAnnuel//src//AnaVi//Script_génération_carte//tablECnum.csv")
